<script setup lang="ts">


  import { ref, reactive, onMounted} from 'vue'

  import { supabase } from './supabase'


  const currentView = ref('upload')

  const selectedTemplate = ref(null)

  const isDragging = ref(false)

  const uploadedFile = ref<File | null>(null)

  const isProcessing = ref(false)

  const userPrompt = ref('')

  const savedCVs = ref<any[]>([])

  const currentCvId = ref<number | null>(null)


  const templates = ref ([

  {

  id: 'jake-ryan',

  name: 'Jake Ryan',

  description: 'Un CV moderno y minimalista ideal para2 perfiles tecnológicos. Muy limpio y fácil de leer por sistemas ATS.',


  previewBg: 'bg-gradient-to-br from-zinc-200 to-zinc-400'

  },

  {

  id: 'harvard',

  name: 'Harvard',

  description: 'Clásico, académico y elegante.',

  previewBg: 'bg-gradient-to-br from-zinc-100 to-zinc-300'

  },

  {

  id: 'modern',

  name: 'MIT',

  description: 'Basado en el curriculum vitae del Instituto de Tecnología de Massachusetts.',

  previewBg: 'bg-gradient-to-br from-zinc-300 to-zinc-500'

  },

  {

  id: 'stanford',

  name: 'Stanford',

  description: '',

  previewBg: 'bg-gradient-to-br from-zinc-200 to-zinc-300'

  }

  ])


  // Datos reactivos para el Editor (Simulando lo que devolvería la IA)

  const cvData = reactive({

  personal: { fullName: 'Tomas', jobTitle: 'Desarrollador de Software', email: 'tomas@ejemplo.com', phone: '+56 9 1234 5678' },

  experience: [ { company: 'Empresa Tech', position: 'Desarrollador Junior', description: 'Desarrollo de interfaces con Vue y Tailwind.' } ]

  })


  onMounted(async () => {

  // Pedimos todos los datos a la tabla 'cv_guardados'

  const { data, error } = await supabase

  .from('cv_guardados')

  .select('*')


  if (error) {

  console.error('Error conectando a Supabase:', error)

  } else if (data) {

  // Transformamos los datos de la nube al formato que usa nuestra app

  savedCVs.value = data.map(fila => ({

  id: fila.id,

  nombre: fila.nombre,

  date: fila.fecha,

  data: fila.datos_json

  }))

  }

  })


  const changeView = (view: string) => {

  currentView.value = view

  }


  const handleDrop = (e: DragEvent) => {

  isDragging.value = false

  if (e.dataTransfer?.files && e.dataTransfer.files.length > 0) {

  const file = e.dataTransfer.files[0]

  if (file) uploadedFile.value = file

  }

  }


  const handleFileInput = (e: Event) => {

  const target = e.target as HTMLInputElement

  if (target.files && target.files.length > 0) {

  const file = target.files[0]

  if (file) uploadedFile.value = file

  }

  }



  const processCV = async () => {

  if (!uploadedFile.value) return

  isProcessing.value = true

  const formData = new FormData()

  formData.append('file', uploadedFile.value)


  try {

  const response = await fetch('http://localhost:8000/api/procesar-pdf', { method: 'POST', body: formData })

  if (!response.ok) throw new Error('Error al procesar el archivo')


  const datosNuevos = await response.json()

  cvData.personal = datosNuevos.personal

  cvData.experience = datosNuevos.experience

  currentView.value = 'editor'

  } catch (error) {

  console.error("Error subiendo el PDF:", error)

  alert("Hubo un error al leer tu documento.")

  } finally {

  isProcessing.value = false

  }

  }


  const generarconIA = async () => {

  if (!userPrompt.value.trim()) return

  isProcessing.value = true


  try {

  // Llamada HTTP al servidor Python

  const response = await fetch('http://localhost:8000/api/generar-cv', {

  method: 'POST',

  headers: { 'Content-Type': 'application/json' },

  body: JSON.stringify({

  instruccion: userPrompt.value,

  cv_base: cvData // Enviamos el CV actual como base a la IA

  })

  })


  if (!response.ok) throw new Error('Error en la respuesta del servidor')

  const datosNuevos = await response.json()

  cvData.personal = datosNuevos.personal

  cvData.experience = datosNuevos.experience

  currentView.value = 'editor'

  } catch (error) {

  console.error("Error de conexión:", error)

  alert("No se pudo conectar con el servidor. ¿Revisaste que FastAPI esté corriendo en el puerto 8000?")

  } finally {

  isProcessing.value = false

  }

  }


  const resetUpload = () => {

  uploadedFile.value = null

  }


  const guardarCV = async () => {

  const cvAbierto = savedCVs.value.find(cv => cv.id === currentCvId.value)

  const sugerencia = cvAbierto ? cvAbierto.nombre : "CV " + cvData.personal.jobTitle


  const nombrePersonalizado = prompt("¿Con qué nombre quieres guardar este CV?", sugerencia)

  if (!nombrePersonalizado) return


  const indiceExistente = savedCVs.value.findIndex(cv => cv.nombre.toLowerCase() === nombrePersonalizado.toLowerCase())


  isProcessing.value = true // Usamos el estado de carga por si el internet está lento


  try {

  if (indiceExistente !== -1) {

  // EL NOMBRE YA EXISTE

  if (savedCVs.value[indiceExistente].id !== currentCvId.value) {

  const confirmar = confirm(`Ya existe un CV llamado "${nombrePersonalizado}". ¿Estás seguro de que deseas sobreescribirlo?`)

  if (!confirmar) return

  }

  const idActualizar = savedCVs.value[indiceExistente].id

  // 1. ACTUALIZAR EN SUPABASE (.update)

  const { error } = await supabase

  .from('cv_guardados')

  .update({

  nombre: nombrePersonalizado,

  datos_json: cvData,

  fecha: new Date().toLocaleDateString()

  })

  .eq('id', idActualizar) // Solo actualiza donde el ID coincida


  if (error) throw error


  // Actualizar en pantalla

  savedCVs.value[indiceExistente].data = JSON.parse(JSON.stringify(cvData))

  savedCVs.value[indiceExistente].date = new Date().toLocaleDateString()

  currentCvId.value = idActualizar

  } else {

  // EL NOMBRE ES NUEVO

  if (currentCvId.value) {

  // Renombrando uno que ya existía

  const { error } = await supabase

  .from('cv_guardados')

  .update({

  nombre: nombrePersonalizado,

  datos_json: cvData,

  fecha: new Date().toLocaleDateString()

  })

  .eq('id', currentCvId.value)


  if (error) throw error


  const indiceActual = savedCVs.value.findIndex(cv => cv.id === currentCvId.value)

  savedCVs.value[indiceActual].nombre = nombrePersonalizado

  savedCVs.value[indiceActual].data = JSON.parse(JSON.stringify(cvData))

  savedCVs.value[indiceActual].date = new Date().toLocaleDateString()

  } else {

  // 2. INSERTAR UNO COMPLETAMENTE NUEVO (.insert)

  // No enviamos 'id' para que Supabase genere uno único automáticamente

  const { data, error } = await supabase

  .from('cv_guardados')

  .insert([{

  nombre: nombrePersonalizado,

  datos_json: cvData,

  fecha: new Date().toLocaleDateString()

  }])

  .select() // Le pedimos que nos devuelva la fila insertada para saber qué ID le asignó


  if (error) throw error


  // Agregar a la pantalla

  const cvInsertado = data[0]

  const nuevoCV = {

  id: cvInsertado.id,

  nombre: cvInsertado.nombre,

  date: cvInsertado.fecha,

  data: cvInsertado.datos_json

  }

  savedCVs.value.push(nuevoCV)

  currentCvId.value = nuevoCV.id

  }

  }


  currentView.value = 'saved'

  } catch (error) {

  console.error("Error guardando en Supabase:", error)

  alert("Hubo un error guardando tu CV en la nube.")

  } finally {

  isProcessing.value = false

  }

  }


  const cargarCVGuardado = (cvGuardado: any) => {

  cvData.personal = cvGuardado.data.personal

  cvData.experience = cvGuardado.data.experience

  currentCvId.value = cvGuardado.id

  currentView.value = 'editor'

  }

</script>


<template>

  <div class="min-h-screen bg-zinc-950 text-zinc-100 flex font-sans">

  <aside class="w-80 border-r border-zinc-800 p-6 hidden lg:flex flex-col gap-4">

  <h1 class="text-2xl font-bold text-white tracking-wider">

  Optimizador<span class="text-blue-500">CV</span>

  </h1>

  <nav class="mt-8 flex flex-col gap-2">

  <a href="#" @click="changeView('upload')" class="px-4 py-2 cursor-pointer hover:bg-zinc-900 rounded-lg text-zinc-400 font-medium active">Crear nuevo CV</a>

  <a href="#" @click="changeView('templates')" class="px-4 py-2 cursor-pointer hover:bg-zinc-900 rounded-lg text-zinc-400 hover:text-zinc-200 transition-colors">Plantillas</a>

  <a href="#" @click="changeView('saved')" :class="['px-4 py-2 cursor-pointer rounded-lg transition-colors', currentView === 'saved' ? 'bg-zinc-900 border border-zinc-800 text-zinc-200' : 'text-zinc-400 hover:bg-zinc-900']">Mis CVs guardados</a>

  <a href="#" @click="changeView('generate')" class="px-4 py-2 cursor-pointer hover:bg-zinc-900 rounded-lg text-zinc-400 hover:text-zinc-200 transition-colors">Generar CV</a>

  </nav>

  <div class="mt-auto pt-6 border-t border-zinc-800">

  <div class="flex items-center gap-3">

  <div class="w-8 h-8 rounded-full bg-blue-900 text-blue-400 flex items-center justify-center font-bold">T</div>

  <div>

  <p class="text-sm font-medium text-zinc-200">Tomas</p>

  <p class="text-xs text-zinc-500">tomas@ejemplo.com</p>

  </div>

  </div>

  </div>

  </aside>


    <main class="flex-1 p-6 md:p-10 overflow-y-auto">

    <!-- VISTA 1: CREAR NUEVO CV -->

      <div v-if="currentView === 'upload'" class="max-w-3xl mx-auto mt-4">

      <!-- ... (Código de drag & drop intacto) ... -->

        <div class="text-center mb-10">
          <h2 class="text-3xl font-semibold text-white mb-2">Comienza tu optimización</h2>
          <p class="text-zinc-400">Sube tu currículum actual en formato PDF.</p>
        </div>

        <div @dragover.prevent="isDragging = true" @dragleave.prevent="isDragging = false" @drop.prevent="handleDrop" :class="['border-2 border-dashed rounded-2xl p-12 text-center transition-all duration-200', isDragging ? 'border-blue-500 bg-blue-500/10' : 'border-zinc-700 bg-zinc-900/50 hover:border-zinc-500 hover:bg-zinc-900']">

          <div v-if="!uploadedFile">

            <svg class="w-12 h-12 text-zinc-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>

            <p class="text-lg text-zinc-300 font-medium mb-1">Arrastra tu documento aquí</p>

            <label class="cursor-pointer bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-lg font-medium transition-colors mt-4 inline-block">

            Seleccionar archivo

              <input type="file" class="hidden" accept=".pdf" @change="handleFileInput">

            </label>

          </div>

          <div v-else class="flex flex-col items-center">

            <div v-if="!isProcessing">

              <p class="text-xl text-zinc-200 font-medium mb-2">{{ uploadedFile.name }}</p>

              <div class="flex gap-4 mt-6 justify-center">

                <button @click="resetUpload" class="text-zinc-400 hover:text-white px-4 py-2 transition-colors">Cambiar archivo</button>

                <button @click="processCV" class="bg-blue-600 hover:bg-blue-500 text-white px-8 py-2 rounded-xl font-medium transition-colors">Procesar con IA</button>

              </div>
            </div>

            <div v-else class="py-8"><p class="text-blue-400 font-medium animate-pulse">Analizando estructura y optimizando viñetas...</p></div>

          </div>

      </div>

      </div>


      <!-- VISTA 2: PLANTILLAS -->

      <div v-else-if="currentView === 'templates'">

        <header class="mb-8">

          <h2 class="text-3xl font-semibold text-white">Galería de Plantillas</h2>

          <p class="text-zinc-400 mt-2 text-sm">Explora nuestros diseños optimizados para superar los filtros ATS.</p>

        </header>


        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

          <article

            v-for="template in templates"

            :key="template.id"

            class="group relative bg-zinc-900/1 hover:bg-zinc-800 border border-zinc-800/50 hover:border-zinc-700 rounded-xl overflow-hidden flex flex-col transition-all duration-200"

          >

            <div class="h-64 p-6 flex items-center justify-center relative overflow-hidden">

              <div :class="['w-3/4 h-full shadow-2xl rounded-t-md transform transition-transform duration-300 group-hover:-translate-y-2', template.previewBg]"></div>

            </div>

            <div class="p-5">

              <h4 class="text-lg font-medium text-zinc-200 group-hover:text-white transition-colors mb-1">

              {{ template.name }}

              </h4>

              <p class="text-sm text-zinc-500">

              {{ template.description }}

              </p>

            </div>

          </article>

        </div>

      </div>


      <!-- VISTA 3: MIS CVS GUARDADOS -->

      <div v-else-if="currentView === 'saved'">

        <header class="mb-8">

          <h2 class="text-3xl font-semibold text-white">Mis CVs Guardados</h2>

          <p class="text-zinc-400 mt-2 text-sm">Tu historial de currículums optimizados. Haz clic en cualquiera para seguir editándolo.</p>

        </header>


        <div v-if="savedCVs.length === 0" class="text-center py-20 bg-zinc-900 border border-zinc-800 rounded-xl">

          <svg class="w-16 h-16 text-zinc-700 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>

          <p class="text-zinc-500 text-lg">Aún no tienes currículums guardados.</p>

        </div>


        <!-- Grilla estilo Plantillas -->

        <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">

          <article

            v-for="cv in savedCVs"

            :key="cv.id"

            @click="cargarCVGuardado(cv)"

            class="group relative bg-zinc-900/1 hover:bg-zinc-800 border border-zinc-800/50 hover:border-zinc-700 rounded-xl overflow-hidden cursor-pointer flex flex-col transition-all duration-200"

          >

          <!-- Contenedor visual de la hoja -->

          <div class="h-64 p-6 flex items-center justify-center relative overflow-hidden">

            <div class="w-3/4 h-full shadow-2xl rounded-t-md transform transition-transform duration-300 group-hover:-translate-y-2 bg-gradient-to-br from-zinc-200 to-zinc-400">

              <!-- Diseño miniatura del CV simulado -->

              <div class="p-4 flex flex-col gap-2 opacity-50">

                <div class="h-3 w-1/2 bg-zinc-500 rounded"></div>

                <div class="h-2 w-1/3 bg-zinc-500 rounded"></div>

                <div class="h-px w-full bg-zinc-400 my-2"></div>

                <div class="h-2 w-full bg-zinc-500 rounded"></div>

                <div class="h-2 w-5/6 bg-zinc-500 rounded"></div>

                <div class="h-2 w-4/5 bg-zinc-500 rounded"></div>

              </div>


            </div>

          </div>


          <!-- Textos de la tarjeta -->

      <div class="p-5">

      <h4 class="text-lg font-medium text-zinc-200 group-hover:text-white transition-colors mb-1 truncate">

      {{ cv.nombre }}

      </h4>

      <p class="text-sm text-zinc-500">

      Guardado el: {{ cv.date }}

      </p>

      </div>

      </article>

      </div>

      </div>

      <!-- VISTA 4: GENERAR CV CON INSTRUCCIÓN -->

      <div v-else-if="currentView === 'generate'" class="max-w-3xl mx-auto mt-4">

      <header class="mb-8">

      <h2 class="text-3xl font-semibold text-white">Instrucción Personalizada</h2>

      <p class="text-zinc-400 mt-2 text-sm">Usaremos el último CV que procesaste como base para adaptarlo a esta oferta específica.</p>

      </header>

      <div class="bg-zinc-900 border border-zinc-800 rounded-xl p-6 shadow-xl">

      <textarea v-model="userPrompt" rows="5" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg p-4 text-zinc-200 focus:outline-none focus:border-blue-500 transition-colors resize-none mb-6" placeholder="Ej: Postulo a desarrollador backend. Destaca mi experiencia con APIs."></textarea>

      <div class="flex justify-end">

      <button @click="generarconIA" :disabled="isProcessing || !userPrompt" class="bg-blue-600 hover:bg-blue-500 text-white px-8 py-3 rounded-xl font-medium transition-colors disabled:opacity-50">

      {{ isProcessing ? 'Adaptando...' : 'Adaptar mi CV' }}

      </button>

      </div>

      </div>

      </div>


      <!-- VISTA 5: EL EDITOR -->

      <div v-else-if="currentView === 'editor'">

      <header class="mb-6 flex justify-between items-center">

      <div>

      <h2 class="text-2xl font-semibold text-white">Revisa tu CV optimizado</h2>

      </div>

      <div class="flex gap-3">

      <!-- NUEVO: Botón de Guardar CV -->

      <button @click="guardarCV" class="bg-zinc-800 hover:bg-zinc-700 text-white border border-zinc-700 px-6 py-2 rounded-lg font-medium flex items-center gap-2 transition-colors">

      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path></svg>

      Guardar CV

      </button>

      <button class="bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-2 rounded-lg font-medium flex items-center gap-2">

      Descargar PDF

      </button>

      </div>

      </header>


      <!-- ... (Código del Editor dividido intacto) ... -->

      <div class="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <div class="bg-zinc-900 border border-zinc-800 rounded-xl p-6 h-[700px] overflow-y-auto">

      <h3 class="text-lg font-medium mb-4 text-blue-400">Datos Personales</h3>

      <div class="space-y-4 mb-8">

      <div><label class="text-xs text-zinc-400">Nombre Completo</label><input v-model="cvData.personal.fullName" class="w-full bg-zinc-950 border border-zinc-800 rounded p-2 text-white"></div>

      <div><label class="text-xs text-zinc-400">Título Profesional</label><input v-model="cvData.personal.jobTitle" class="w-full bg-zinc-950 border border-zinc-800 rounded p-2 text-white"></div>

      </div>

      <h3 class="text-lg font-medium mb-4 text-blue-400">Experiencia Laboral</h3>

      <div v-for="(job, index) in cvData.experience" :key="index" class="bg-zinc-950/50 p-4 border border-zinc-800 rounded mb-4">

      <input v-model="job.position" class="w-full bg-zinc-900 border border-zinc-800 rounded p-2 text-white mb-2" placeholder="Cargo">

      <input v-model="job.company" class="w-full bg-zinc-900 border border-zinc-800 rounded p-2 text-white mb-2" placeholder="Empresa">

      <textarea v-model="job.description" class="w-full bg-zinc-900 border border-zinc-800 rounded p-2 text-white text-sm" rows="3"></textarea>

      </div>

      </div>


      <div class="bg-zinc-800/50 rounded-xl p-4 flex items-center justify-center">

      <div class="bg-white w-full max-w-[21cm] aspect-[1/1.414] shadow-2xl p-8 text-black">

      <h1 class="text-3xl font-bold uppercase">{{ cvData.personal.fullName }}</h1>

      <p class="text-lg text-blue-700">{{ cvData.personal.jobTitle }}</p>

      <hr class="my-4 border-gray-300">

      <div v-for="(job, index) in cvData.experience" :key="index" class="mb-4">

      <h3 class="font-bold">{{ job.position }} <span class="font-normal text-blue-700">| {{ job.company }}</span></h3>

      <p class="text-sm text-gray-700 mt-1">{{ job.description }}</p>

      </div>

      </div>

      </div>

      </div>

      </div>



    </main>

  </div> 
</template>