// src/store.ts
import { ref, reactive } from 'vue'

// Estado global de la aplicación
export const isProcessing = ref(false)
export const savedCVs = ref<any[]>([])
export const currentCvId = ref<number | null>(null)
export const currentUser = ref<any>(null)

export const cvData = ref({
  personal: {
    fullName: '',
    jobTitle: '',
    email: '',    // <--- NUEVO
    phone: ''     // <--- NUEVO
  },
  experience: [
    {
      company: '',
      position: '',
      date: '',       // <--- NUEVO
      location: '',   // <--- NUEVO
      description: ''
    }
  ],
  education: [        // <--- NUEVO BLOQUE COMPLETO
    {
      institution: '',
      degree: '',
      date: ''
    }
  ]
})