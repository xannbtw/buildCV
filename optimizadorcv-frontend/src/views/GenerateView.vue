<script setup lang="ts">
import { ref } from 'vue'
import { cvData, isProcessing } from '../store'

const userPrompt = ref('')

const emit = defineEmits<{
  (e: 'generated'): void
}>()

const generarconIA = async () => {
  if (!userPrompt.value.trim()) return

  if (!cvData.value.personal?.fullName && (!cvData.value.experience || cvData.value.experience.length === 0)) {
    alert('Por favor, sube un CV primero antes de usar la IA.')
    return
  }

  isProcessing.value = true

  try {
    const response = await fetch('https://buildcv-production-f12c.up.railway.app/api/generar-cv', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        instruccion: userPrompt.value,
        cv_base: cvData.value
      })
    })

    if (!response.ok) throw new Error('Error en la respuesta del servidor')

    const datosNuevos = await response.json()
    
    if (datosNuevos.error) {
      alert("La IA dice: " + datosNuevos.error)
      return
    }

    cvData.value.personal = datosNuevos.personal
    cvData.value.experience = datosNuevos.experience
    cvData.value.education = datosNuevos.education || []
    
    emit('generated')
  } catch (error) {
    console.error('Error de conexión:', error)
    alert('No se pudo conectar con el servidor. ¿Revisaste que FastAPI esté corriendo en el puerto 8000?')
  } finally {
    isProcessing.value = false
  }
}
</script>

<template>
  <div class="max-w-3xl mx-auto mt-4">
    <header class="mb-8">
      <h2 class="text-3xl font-semibold text-zinc-900">Genera tu CV</h2>
      <p class="text-zinc-500 mt-2 text-sm">
        Usaremos el último CV que procesaste como base para adaptarlo a esta oferta específica.
      </p>
    </header>
    <div class="border border-zinc-200 rounded-xl p-6 shadow-xl">
      <textarea
        v-model="userPrompt"
        rows="5"
        class="w-full bg-zinc-100 border border-zinc-200 rounded-lg p-4 text-zinc-700 focus:outline-none focus:border-[#89CFF0] transition-colors resize-none mb-6"
        placeholder="Ej: Postulo a desarrollador backend. Destaca mi experiencia con APIs."
      ></textarea>
      <div class="flex justify-end">
        <button
          @click="generarconIA"
          :disabled="isProcessing || !userPrompt"
          class="bg-[#89CFF0] hover:bg-[#89CFF0] text-white px-8 py-3 rounded-xl font-medium transition-colors disabled:opacity-50"
        >
          {{ isProcessing ? 'Adaptando...' : 'Generar mi CV' }}
        </button>
      </div>
    </div>
  </div>
</template>
