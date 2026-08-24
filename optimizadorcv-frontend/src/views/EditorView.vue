<script setup lang="ts">
import { supabase } from '../supabase'
import { savedCVs, cvData, currentCvId, isProcessing, currentUser } from '../store'

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
      // EL NOMBRE YA EXISTE
      if (savedCVs.value[indiceExistente].id !== currentCvId.value) {
        const confirmar = confirm(
          `Ya existe un CV llamado "${nombrePersonalizado}". ¿Estás seguro de que deseas sobreescribirlo?`
        )
        if (!confirmar) return
      }

      const idActualizar = savedCVs.value[indiceExistente].id

      // 1. ACTUALIZAR EN SUPABASE (.update)
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

      // Actualizar en pantalla
      savedCVs.value[indiceExistente].data = JSON.parse(JSON.stringify(cvData.value))
      savedCVs.value[indiceExistente].date = new Date().toLocaleDateString()
      currentCvId.value = idActualizar
      } else {
      // EL NOMBRE ES NUEVO
      let guardarComoCopia = true; // Por defecto asumimos que quiere crear uno nuevo

      if (currentCvId.value) {
        // Si tenía un CV abierto, le damos a elegir
        guardarComoCopia = confirm(
          'Has escrito un nombre diferente. ¿Quieres guardar esto como un nuevo currículum (una copia)?\n\n[Aceptar] = Crear nuevo CV\n[Cancelar] = Solo renombrar el actual'
        );
      }

      if (currentCvId.value && !guardarComoCopia) {
        // OPCIÓN A: El usuario canceló, solo quiere RENOMBRAR
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
        // OPCIÓN B: INSERTAR UNO COMPLETAMENTE NUEVO (Guardar como copia)
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
        currentCvId.value = nuevoCV.id // Ahora editamos el nuevo
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
    position: 'Nuevo Cargo',
    company: 'Nueva Empresa',
    date: 'Fecha de Inicio - Fecha Fin',
    location: 'Ciudad',
    description: 'Descripción de responsabilidades y logros.'
  })
}

const eliminarExperiencia = (index: number) => {
  if (cvData.value.experience) {
    cvData.value.experience.splice(index, 1)
  }
}

const agregarEducacion = () => {
  if (!cvData.value.education) cvData.value.education = []
  cvData.value.education.push({
    institution: 'Nueva Institución',
    degree: 'Título Obtenido',
    date: 'Fecha de Inicio - Fecha de Fin'
  })
}

const eliminarEducacion = (index: number) => {
  if (cvData.value.education) {
    cvData.value.education.splice(index, 1)
  }
}
</script>

<template>
  <div>
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
        <button class="bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-2 rounded-lg font-medium flex items-center gap-2">
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
            <div v-for="(job, index) in cvData.education" :key="index" class="bg-zinc-200 p-3 rounded-lg border border-gray-800 relative">
              
              <button @click="eliminarEducacion(index)" class="absolute top-2 right-2 text-red-500 hover:text-red-400 text-xs font-bold">✕</button>
              
              <div class="grid grid-cols-2 gap-2 mb-2 pr-4">
                <input v-model="job.institution" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Institucion" />
                <input v-model="job.degree" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Grado" />
              </div>
              
              <div class="grid grid-cols-2 gap-2 mb-2">
                <input v-model="job.date" class="bg-zinc-200 border border-gray-700 text-zinc-600 p-2 rounded text-sm" placeholder="Ej: Ene 2023 - Presente" />
              </div>
            </div>
          </div>
        </div>

      </div>

<!-- VISTA PREVIA -->
      <div class="bg-white w-full max-w-[21cm] aspect-[1/1.414] shadow-2xl p-10 text-black font-sans overflow-y-auto">
        
        <!-- Cabecera Dinámica -->
        <header class="text-center mb-6">
          <h1 class="text-4xl font-bold text-gray-900 mb-1 tracking-tight">{{ cvData.personal?.fullName || 'Tu Nombre' }}</h1>
          <p class="text-sm text-gray-600">
            {{ cvData.personal?.jobTitle || 'Título Profesional' }}
            <span v-if="cvData.personal?.email" class="mx-2">|</span> 
            {{ cvData.personal?.email || '' }}
            <span v-if="cvData.personal?.phone" class="mx-2">|</span> 
            {{ cvData.personal?.phone || '' }}
          </p>
        </header>

        <!-- Sección: Experiencia Dinámica -->
        <section class="mb-6">
          <h2 class="text-xs font-bold text-gray-900 uppercase tracking-widest border-b-[1.5px] border-gray-900 pb-1 mb-3">
            Experiencia Laboral
          </h2>
          
          <div v-for="(job, index) in cvData.experience" :key="index" class="mb-4">
            <!-- Empresa y Fechas Reales -->
            <div class="flex justify-between items-baseline">
              <h3 class="text-sm font-bold text-gray-900">{{ job.company || 'Nombre de la Empresa' }}</h3>
              <span class="text-xs text-gray-600 font-medium">{{ job.date || 'Fecha no especificada' }}</span>
            </div>
            
            <!-- Cargo y Ubicación Reales -->
            <div class="flex justify-between items-baseline mb-1">
              <p class="text-sm italic text-gray-800">{{ job.position || 'Tu Cargo' }}</p>
              <span class="text-xs text-gray-600">{{ job.location || '' }}</span>
            </div>
            
            <div class="text-sm text-gray-700 leading-relaxed mt-1 pl-4 relative">
              <span class="absolute left-0 top-[6px] w-1.5 h-1.5 bg-gray-500 rounded-full"></span>
              {{ job.description }}
            </div>
          </div>
        </section>

        <!-- Sección: Educación Dinámica (Solo se muestra si hay datos) -->
        <section v-if="cvData.education && cvData.education.length > 0" class="mb-6">
          <h2 class="text-xs font-bold text-gray-900 uppercase tracking-widest border-b-[1.5px] border-gray-900 pb-1 mb-3">
            Educación
          </h2>
          <div v-for="(edu, index) in cvData.education" :key="index" class="mb-3">
            <div class="flex justify-between items-baseline">
              <h3 class="text-sm font-bold text-gray-900">{{ edu.institution || 'Institución' }}</h3>
              <span class="text-xs text-gray-600 font-medium">{{ edu.date || '' }}</span>
            </div>
            <p class="text-sm italic text-gray-800">{{ edu.degree || 'Título obtenido' }}</p>
          </div>
        </section>

      </div>
    </div>
  </div>
</template>
