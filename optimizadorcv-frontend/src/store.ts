// src/store.ts
import { ref, reactive } from 'vue'

export const isProcessing = ref(false)
export const savedCVs = ref<any[]>([])
export const currentCvId = ref<number | null>(null)
export const currentUser = ref<any>(null)

export const cvData = ref({
  personal: {
    fullName: '',
    jobTitle: '',
    email: '',
    phone: '',
    summary: ''
  },
  experience: [
    {
      company: '',
      position: '',
      date: '',
      location: '',
      description: ''
    }
  ],
  education: [
    {
      institution: '',
      degree: '',
      date: ''
    }
  ],
  skills: [] as {
    name: string
  }[]
})

export const plantillaActual = ref('jake')
