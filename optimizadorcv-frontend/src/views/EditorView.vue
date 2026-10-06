<script setup lang="ts">
import { supabase } from '../supabase'
import { savedCVs, cvData, currentCvId, isProcessing, currentUser, plantillaActual } from '../store'
import JakeTemplate from '../components/templates/jake.vue'

const emit = defineEmits<{
  (e: 'saved'): void
}>()

  const guardarCV = async () => {
  const cvAbierto = savedCVs.value.find(cv => cv.id === currentCvId.value)
  const sugerencia = cvAbierto ? cvAbierto.nombre : 'CV ' + cvData.value.personal.jobTitle

  const nombrePersonalizado = prompt('¿Con qué nombre quieres guardar este CV?', sugerencia)
  if (!nombrePersonalizado) return

  const indiceExistente = savedCVs.value.findIndex(
    cv => cv.nombre.toLowerCase() === nombrePersonalizado.toLowerCase()
  )

  isProcessing.value = true

  try {
    if (indiceExistente !== -1) {
      if (savedCVs.value[indiceExistente].id !== currentCvId.value) {
        const confirmar = confirm(
          `Ya existe un CV llamado "${nombrePersonalizado}". ¿Estás seguro de que deseas sobreescribirlo?`
        )
        if (!confirmar) return
      }

      const idActualizar = savedCVs.value[indiceExistente].id

      const { error } = await supabase
        .from('cv_guardados')
        .update({
          nombre: nombrePersonalizado,
          datos_json: cvData.value,
          fecha: new Date().toLocaleDateString(),
          user_id: currentUser.value.id
        })
        .eq('id', idActualizar)

      if (error) throw error

      savedCVs.value[indiceExistente].data = JSON.parse(JSON.stringify(cvData.value))
      savedCVs.value[indiceExistente].date = new Date().toLocaleDateString()
      currentCvId.value = idActualizar
      } else {
      let guardarComoCopia = true;

      if (currentCvId.value) {
        guardarComoCopia = confirm(
          'Has escrito un nombre diferente. ¿Quieres guardar esto como un nuevo currículum (una copia)?\n\n[Aceptar] = Crear nuevo CV\n[Cancelar] = Solo renombrar el actual'
        );
      }

      if (currentCvId.value && !guardarComoCopia) {
        const { error } = await supabase
          .from('cv_guardados')
          .update({
            nombre: nombrePersonalizado,
            datos_json: cvData.value,
            fecha: new Date().toLocaleDateString(),
            user_id: currentUser.value.id
          })
          .eq('id', currentCvId.value)

        if (error) throw error

        const indiceActual = savedCVs.value.findIndex(cv => cv.id === currentCvId.value)
        if (indiceActual !== -1) {
          savedCVs.value[indiceActual].nombre = nombrePersonalizado
          savedCVs.value[indiceActual].data = JSON.parse(JSON.stringify(cvData.value))
          savedCVs.value[indiceActual].date = new Date().toLocaleDateString()
        }
      } else {
        const { data, error } = await supabase
          .from('cv_guardados')
          .insert([
            {
              nombre: nombrePersonalizado,
              datos_json: cvData.value,
              fecha: new Date().toLocaleDateString(),
              user_id: currentUser.value.id
            }
          ])
          .select()

        if (error) throw error

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

    emit('saved')
  } catch (error) {
    console.error('Error guardando en Supabase:', error)
    alert('Hubo un error guardando tu CV en la nube.')
  } finally {
    isProcessing.value = false
  }
}

const agregarExperiencia = () => {
  if (!cvData.value.experience) cvData.value.experience = []
  cvData.value.experience.push({
    position: '',
    company: '',
    date: '',
    location: '',
    description: ''
  })
}

const eliminarExperiencia = (index: number) => {
  if (cvData.value.experience) {
    cvData.value.experience.splice(index, 1)
  }
}

const eliminarSkill = (index: number) => {
  if (cvData.value.skills) {
    cvData.value.skills.splice(index, 1)
  }
}

const agregarEducacion = () => {
  if (!cvData.value.education) cvData.value.education = []
  cvData.value.education.push({
    institution: '',
    degree: '',
    date: ''
  })
}

const agregarSkill = () => {
  if (!cvData.value.skills) cvData.value.skills = []
  cvData.value.skills.push({
    category: '',
    details: ''
  })
}

const eliminarEducacion = (index: number) => {
  if (cvData.value.education) {
    cvData.value.education.splice(index, 1)
  }
}

const agregarProyecto = () => {
  if (!cvData.value.projects) cvData.value.projects = []
  cvData.value.projects.push({
    name: '',
    details: '',
    description: ''
  })
}

const eliminarProyecto = (index: number) => {
  if (cvData.value.projects) {
    cvData.value.projects.splice(index, 1)
  }
}

const descargarPDF = () => {
  const elementoCV = document.getElementById('cv-preview')
  if (!elementoCV) return

  const iframe = document.createElement('iframe')
  iframe.style.display = 'none'
  document.body.appendChild(iframe)

  const estilos = Array.from(document.querySelectorAll('style, link[rel="stylesheet"]'))
    .map(etiqueta => etiqueta.outerHTML)
    .join('\n')

  const iframeDoc = iframe.contentWindow?.document
  if (iframeDoc) {
    iframeDoc.open()
    iframeDoc.write(`
      <html>
        <head>
          <title>${cvData.value.personal?.fullName || 'CV'}</title>
          ${estilos}
          <style>
            @page { margin: 0; size: A4; }
            body { 
              margin: 0; 
              padding: 0; 
              background: white; 
              -webkit-print-color-adjust: exact; 
              print-color-adjust: exact; 
            }
            #cv-preview { 
              transform: scale(1) !important; 
              box-shadow: none !important; 
              width: 210mm !important; 
              min-height: 297mm !important;
              margin: 0 !important;
              padding: 20mm 20mm !important; 
              box-sizing: border-box !important; 
            }
          </style>
        </head>
        <body>
          ${elementoCV.outerHTML}
        </body>
      </html>
    `)
    iframeDoc.close()

    setTimeout(() => {
      iframe.contentWindow?.focus()
      iframe.contentWindow?.print()
      
      setTimeout(() => document.body.removeChild(iframe), 1000)
    }, 500)
  }
}

</script>

<template>
  <header class="mb-6 flex justify-between items-center">
    <div>
      <h2 class="text-2xl font-semibold text-zinc-900">Revisa tu CV</h2>
    </div>
    <div class="flex gap-3">
        <button
          @click="guardarCV"
          class="bg-zinc-800 hover:bg-zinc-700 text-white border border-zinc-700 px-6 py-2 rounded-lg font-medium flex items-center gap-2 transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path>
          </svg>
          Guardar CV
        </button>
        <button @click="descargarPDF" class="bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-2 rounded-lg font-medium flex items-center gap-2">
          Descargar PDF
        </button>
      </div>
    </header>

    <div class="grid grid-cols-1 xl:grid-cols-2 gap-6">
      <div class="bg-zinc-200 border border-zinc-800 rounded-xl p-6 h-[700px] overflow-y-auto">
        <h3 class="text-lg font-medium mb-4 text-zinc-500">Datos Personales</h3>
        <div class="space-y-4 mb-8">
          <div>
            <label class="text-xs text-zinc-600">Nombre Completo</label>
            <input v-model="cvData.personal.fullName" class="w-full bg-zinc-200 border border-zinc-800 rounded p-2 text-zinc-600" />
          </div>
          <div>
            <label class="text-xs text-zinc-600">Título Profesional</label>
            <input v-model="cvData.personal.jobTitle" class="w-full bg-zinc-200 border border-zinc-800 rounded p-2 text-zinc-600" />
          </div>
          <div>
            <label class="text-xs text-zinc-600">Correo Electronico</label>
            <input v-model="cvData.personal.email" class="w-full bg-zinc-200 border border-zinc-800 rounded p-2 text-zinc-600" />
          </div>
          <div>
            <label class="text-xs text-zinc-600">Telefono</label>
            <input v-model="cvData.personal.phone" class="w-full bg-zinc-200 border border-zinc-800 rounded p-2 text-zinc-600" />
          </div>
          <div>
            <label class="text-xs text-zinc-600">Resumen Profesional</label>
            <input v-model="cvData.personal.summary" class="w-full bg-zinc-200 border border-zinc-800 rounded p-2 text-zinc-600" />
          </div>
        </div>
        <div class="mb-6">
          <div class="flex justify-between items-center mb-3">
            <h3 class="text-sm text-zinc-600">Experiencia Laboral</h3>
            <button @click="agregarExperiencia" class="text-xs bg-zinc-200 hover:bg-zinc-200 text-zinc-600 px-2 py-1 rounded transition-colors">+ Añadir experiencia</button>
          </div>
          
          <div class="flex flex-col gap-4">
            <div v-for="(job, index) in cvData.experience" :key="index" class="bg-zinc-200 p-3 rounded-lg border border-gray-800 relative">
              
              <button @click="eliminarExperiencia(index)" class="absolute top-2 right-2 text-red-500 hover:text-red-400 text-xs font-bold">✕</button>
              
              <div class="grid grid-cols-2 gap-2 mb-2 pr-4">
                <input v-model="job.company" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Empresa" />
                <input v-model="job.position" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Cargo" />
              </div>
              
              <div class="grid grid-cols-2 gap-2 mb-2">
                <input v-model="job.date" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Ej: Ene 2023 - Presente" />
                <input v-model="job.location" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Ubicación" />
              </div>
              
              <textarea v-model="job.description" class="w-full bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm min-h-[80px]" placeholder="Descripción de tus responsabilidades..."></textarea>
            </div>
          </div>
        </div>
        <div class="mb-6">
          <div class="flex justify-between items-center mb-3">
            <h3 class="text-sm text-zinc-600">Educacion</h3>
            <button @click="agregarEducacion" class="text-xs bg-zinc-200 hover:bg-zinc-200 text-zinc-600 px-2 py-1 rounded transition-colors">+ Añadir educacion</button>
          </div>
          
          <div class="flex flex-col gap-4">
            <div v-for="(edu, index) in cvData.education" :key="index" class="bg-zinc-200 p-3 rounded-lg border border-gray-800 relative">
              
              <button @click="eliminarEducacion(index)" class="absolute top-2 right-2 text-red-500 hover:text-red-400 text-xs font-bold">✕</button>
              
              <div class="grid grid-cols-2 gap-2 mb-2 pr-4">
                <input v-model="edu.institution" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Institucion" />
                <input v-model="edu.degree" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Grado" />
              </div>
              
              <div class="grid grid-cols-2 gap-2 mb-2">
                <input v-model="edu.date" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Ej: Ene 2023 - Presente" />
              </div>
            </div>
          </div>
        </div>

        <div class="mb-6">
          <div class="flex justify-between items-center mb-3">
            <h3 class="text-sm text-zinc-600">Proyectos</h3>
            <button @click="agregarProyecto" class="text-xs bg-zinc-200 hover:bg-zinc-200 text-zinc-600 px-2 py-1 rounded transition-colors">+ Añadir proyecto</button>
          </div>
          
          <div class="flex flex-col gap-4">
            <div v-for="(project, index) in cvData.projects" :key="index" class="bg-zinc-200 p-3 rounded-lg border border-gray-800 relative">
              
              <button @click="eliminarProyecto(index)" class="absolute top-2 right-2 text-red-500 hover:text-red-400 text-xs font-bold">✕</button>
              
              <div class="grid grid-cols-2 gap-2 mb-2 pr-4">
                <input v-model="project.name" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Nombre del proyecto" />
                <input v-model="project.details" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Habilidades utilizadas en el proyecto..."></input>
              </div>
              
              <textarea v-model="project.description" class="w-full bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm min-h-[80px]" placeholder="Descripción del proyecto..."></textarea>
            </div>
          </div>
        </div>

        <div class="mb-6">
          <div class="flex justify-between items-center mb-3">
            <h3 class="text-sm text-zinc-600">Habilidades</h3>
            <button @click="agregarSkill" class="text-xs bg-zinc-200 hover:bg-zinc-200 text-zinc-600 px-2 py-1 rounded transition-colors">+ Añadir habilidad</button>
          </div>
          
          <div class="flex flex-col gap-4">
            <div v-for="(skill, index) in cvData.skills" :key="index" class="bg-zinc-200 p-3 rounded-lg border border-gray-800 relative">
              
              <button @click="eliminarSkill(index)" class="absolute top-2 right-2 text-red-500 hover:text-red-400 text-xs font-bold">✕</button>
              
              <div class="grid grid-cols-2 gap-2 mb-2 pr-4">
                <input v-model="skill.category" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Ej: Idiomas" />
                <input v-model="skill.details" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Ej: Ingles, Español..." />
              </div>
            </div>
          </div>
        </div>

      </div>

      <div class="w-full max-w-[21cm] h-full max-h-[85vh] overflow-y-auto shadow-2xl mx-auto">          
        <div class="w-full origin-top scale-[0.85] md:scale-100">

          <div id="cv-preview" class="bg-white">
            <JakeTemplate v-if="plantillaActual === 'jake' || plantillaActual === 'clasica'" />
          </div>

        </div>
      </div>
    </div>
</template>
