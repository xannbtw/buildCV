<script setup lang="ts">
import { ref } from 'vue'
import { supabase } from '../supabase'
import { currentUser } from '../store'
import { useRouter } from 'vue-router'
const router = useRouter()

const email = ref('')
const password = ref('')
const isLogin = ref(true)
const isLoading = ref(false)
const errorMessage = ref('')

const emit = defineEmits<{
    (e: 'logged-in'): void
}>()

const handleAuth = async () => {
    if (!email.value ||  !password.value) {
        errorMessage.value = "Por favor completa todos los campos.";
        return;
    }

    isLoading.value = true
    errorMessage.value = ""

    try {
    if (isLogin.value) {
      // PROCESO DE INICIO DE SESIÓN
      const { data, error } = await supabase.auth.signInWithPassword({
        email: email.value,
        password: password.value,
      })
      if (error) throw error
      
      currentUser.value = data.user
      router.push('/dashboard')
      emit('logged-in')
      
    } else {
      // PROCESO DE REGISTRO
      const { data, error } = await supabase.auth.signUp({
        email: email.value,
        password: password.value,
      })
      if (error) throw error
      
      alert('¡Cuenta creada con éxito! Ya puedes iniciar sesión.')
      isLogin.value = true // Lo devolvemos al login para que entre
    }
  } catch (error: any) {
    console.error('Error de Auth:', error)
    // Mensajes de error amigables
    if (error.message.includes('Invalid login credentials')) {
      errorMessage.value = 'Correo o contraseña incorrectos.'
    } else if (error.message.includes('User already registered')) {
      errorMessage.value = 'Este correo ya tiene una cuenta. Inicia sesión.'
    } else if (error.message.includes('Password should be at least')) {
      errorMessage.value = 'La contraseña debe tener al menos 6 caracteres.'
    } else {
      errorMessage.value = 'Hubo un error. Revisa tus datos e intenta de nuevo.'
    }
  } finally {
    isLoading.value = false
  }
}

</script>

<template>
    <div class="flex min-h-full flex-col justify-center px6 py-50 lg:px8">
        <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-zinc-900">
            {{ isLogin ? 'Bienvenido de nuevo' : 'Crear cuenta' }}
        </h2>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form @submit.prevent="handleAuth" class="space-y-6">
            <input 
                v-model="email" 
                type="email" 
                placeholder="Correo electrónico" 
                class="w-full px-4 py-3 bg-zinc-100 border border-zinc-200 rounded-lg text-zinc-700 placeholder-zinc-500 focus:border-[#89CFF0] focus:outline-none"
                required
            />
            
            <input 
                v-model="password" 
                type="password" 
                placeholder="Contraseña" 
                class="w-full px-4 py-3 bg-zinc-100 border border-zinc-200 rounded-lg text-zinc-700 placeholder-zinc-500 focus:border-[#89CFF0] focus:outline-none"
                required
                minlength="6"
            />

            <div v-if="errorMessage" class="bg-red-900/10 border border-red-700/50 text-red-400 p-3 rounded-lg text-sm">
                {{ errorMessage }}
            </div>

            <button 
                type="submit" 
                :disabled="isLoading" 
                class="w-full py-3 px-4 bg-[#89CFF0] hover:bg-[#89CFF0] text-white font-bold rounded-lg disabled:opacity-50 disabled:cursor-not-allowed transition-colors">
                {{ isLoading ? (isLogin ? 'Iniciando sesión...' : 'Creando cuenta...') : (isLogin ? 'Iniciar sesión' : 'Registrarse') }}
            </button>
        </form>

        <p class="mt-6 text-center text-zinc-500 text-sm">
            {{ isLogin ? '¿No tienes cuenta?' : '¿Ya tienes cuenta?' }}
            <a href="#" @click="isLogin = !isLogin; errorMessage = '';" class="text-[#89CFF0] hover:text-[#89CFF0] font-bold ml-1">
                {{ isLogin ? 'Regístrate aquí' : 'Inicia sesión aquí' }}
            </a>
        </p>
      </div>
    </div>

</template>