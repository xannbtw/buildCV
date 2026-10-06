<script setup lang="ts">
import { onMounted } from 'vue'
import { supabase } from '../supabase'
import { savedCVs, cvData, currentCvId } from '../store'

const emit = defineEmits<{
  (e: 'select-cv', cv: any): void
}>()

onMounted(async () => {
  if (savedCVs.value.length === 0) {
    const { data, error } = await supabase
      .from('cv_guardados')
      .select('*')

    if (error) {
      console.error('Error conectando a Supabase:', error)
    } else if (data) {
      savedCVs.value = data.map(fila => ({
        id: fila.id,
        nombre: fila.nombre,
        date: fila.fecha,
        data: fila.datos_json
      }))
    }
  }
})

const cargarCVGuardado = (cvGuardado: any) => {
  cvData.value.personal = cvGuardado.data.personal
  cvData.value.experience = cvGuardado.data.experience
  cvData.value.education = cvGuardado.data.education || []
  cvData.value.skills = cvGuardado.data.skills || []
  cvData.value.projects = cvGuardado.data.projects || []
  
  currentCvId.value = cvGuardado.id
  
  emit('select-cv', cvGuardado)
}


const eliminarCV = async (id: number) => {
  const confirmar = window.confirm('¿Estás seguro de eliminar este CV?')
  if (!confirmar) return
  try {
    const { error } = await supabase
      .from('cv_guardados')
      .delete()
      .eq('id', id)

    if (!error) {
      savedCVs.value = savedCVs.value.filter(cv => cv.id !== id)
    }

    if (id === currentCvId.value) {
      currentCvId.value = null
    }
  } catch (error) {
    console.error('Error al eliminar el CV:', error)
  }
}

</script>

<template>
  <div>
    <header class="mb-8">
      <h2 class="text-3xl font-semibold text-zinc-900">CVs Guardados</h2>
      <p class="text-zinc-500 mt-2 text-sm">Haz clic en cualquiera para seguir editándolo.
      </p>
    </header>

    <div v-if="savedCVs.length === 0" class="text-center py-20 border border-zinc-200 rounded-xl">
      <svg class="w-16 h-16 text-zinc-700 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
      </svg>
      <p class="text-zinc-500 text-lg">Aún no tienes currículums guardados.</p>
    </div>

    <!-- Grilla estilo Plantillas -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <article 
        v-for="cv in savedCVs" 
        :key="cv.id"
        @click="cargarCVGuardado(cv)"
        class="group relative bg-zinc-900/1 hover:bg-zinc-200 border border-zinc-800/50 hover:border-zinc-200 rounded-xl overflow-hidden cursor-pointer flex flex-col transition-all duration-200"
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
          <h4 class="text-lg font-medium text-zinc-500 group-hover:text-zinc-500 transition-colors mb-1 truncate">
            {{ cv.nombre }}
          </h4>
          <p class="text-sm text-zinc-500">
            Guardado el: {{ cv.date }}
          </p>
        </div>

        <button @click.stop="eliminarCV(cv.id)" class="absolute top-3 right-3" title="Eliminar CV">
          <svg class="w-5 h-5 text-zinc-500 hover:text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </article>
    </div>
  </div>
</template>