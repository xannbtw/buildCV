// src/store.ts
import { ref, reactive } from 'vue'

export const isProcessing = ref(false)
export const savedCVs = ref<any[]>([])
export const currentCvId = ref<number | null>(null)
export const currentUser = ref<any>(null)

export const cvData = ref({
  personal: {
    fullName: '',
    portfolioUrl: '',
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
    category: string
    details: string
  }[],
  projects: [] as {
    name: string
    details: string
    description: string
  }[]
})

export const plantillaActual = ref('jake')
