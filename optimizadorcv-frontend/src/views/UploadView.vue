<script setup lang="ts">
import { ref } from 'vue'
import { cvData } from '../store'

const isDragging = ref(false)
const uploadedFile = ref<File | null>(null)
const isProcessing = ref(false)

const emit = defineEmits<{
  (e: 'processed'): void
}>()

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

const resetUpload = () => {
  uploadedFile.value = null
}

const processCV = async () => {
  if (!uploadedFile.value) return
  isProcessing.value = true

  const formData = new FormData()
  formData.append('file', uploadedFile.value)

  try {
    const response = await fetch('https://buildcv-production-f12c.up.railway.app/api/procesar-pdf', {
      method: 'POST',
      body: formData
    })
    if (!response.ok) throw new Error('Error al procesar el archivo')

    const datosNuevos = await response.json()
    
    if (datosNuevos.error) {
      alert("La Inteligencia Artificial dice: " + datosNuevos.error)
      return
    }

    cvData.value.personal = datosNuevos.personal
    cvData.value.experience = datosNuevos.experience
    cvData.value.education = datosNuevos.education || []
    
    emit('processed')
  } catch (error) {
    console.error('Error subiendo el PDF:', error)
    alert('Hubo un error al leer tu documento.')
  } finally {
    isProcessing.value = false
  }
}

const iniciarCVEnBlanco = () => {
  cvData.value = {
    personal: { fullName: '', jobTitle: '', email: '', phone: '' },
    experience: [],
    education: []
  }
  emit('processed')
}
</script>

<template>
  <div> 
    <div class="text-center mb-10">
      <h2 class="text-3xl font-semibold text-zinc-900 mb-2">Comienza tu optimización</h2>
      <p class="text-zinc-500">Sube tu currículum actual en formato PDF.</p>
    </div>
    <div class="flex flex-col md:flex-row justify-center items-stretch gap-6 max-w-4xl mx-auto">
      <div class="w-full md:w-1/2 border-2 border-[#89CFF0] hover:border-[#89CFF0]/80 rounded-lg p-12 flex flex-col justify-center items-center text-center">
          <svg class="w-12 h-12 text-zinc-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
          </svg>
          <p class="text-lg text-zinc-500 font-medium mb-1">Crea tu CV</p>
          <button @click="iniciarCVEnBlanco" class="cursor-pointer bg-[#89CFF0] hover:bg-[#89CFF0]/50 text-white px-6 py-2 rounded-lg font-medium transition-colors mt-4 inline-block">
            Abrir Editor
          </button>
        </div>

      <div
        @dragover.prevent="isDragging = true"
        @dragleave.prevent="isDragging = false"
        @drop.prevent="handleDrop"
        :class="[
          'w-full md:w-1/2 border-2 border-dashed rounded-lg p-12 flex flex-col justify-center items-center text-center transition-all duration-200',
          isDragging
            ? 'border-[#89CFF0] bg-[#89CFF0]'
            : 'border-zinc-300 hover:border-zinc-500 hover:bg-zinc-100'
        ]"
      >
        <div v-if="!uploadedFile">
          <svg class="w-12 h-12 text-zinc-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
          </svg>
          <p class="text-lg text-zinc-500 font-medium mb-1">Arrastra tu documento aquí</p>
          <label class="cursor-pointer bg-[#89CFF0] hover:bg-[#89CFF0]/80 text-white px-6 py-2 rounded-lg font-medium transition-colors mt-4 inline-block">
            Seleccionar archivo
            <input type="file" class="hidden" accept=".pdf" @change="handleFileInput">
          </label>
        </div>

        <div v-else class="flex flex-col items-center">
          <div v-if="!isProcessing">
            <p class="text-xl text-zinc-600 font-medium mb-2">{{ uploadedFile.name }}</p>
            <div class="flex gap-4 mt-6 justify-center">
              <button @click="resetUpload" class="text-zinc-500 hover:text-zinc-400 px-4 py-2 transition-colors">
                Cambiar archivo
              </button>
              <button @click="processCV" class="bg-[#89CFF0] hover:bg-[#89CFF0]/80 text-zinc-100 px-8 py-2 rounded-xl font-medium transition-colors">
                Procesar con IA
              </button>
            </div>
          </div>
          <div v-else class="py-8">
            <p class="text-[#89CFF0] font-medium animate-pulse">Analizando estructura y optimizando viñetas...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>