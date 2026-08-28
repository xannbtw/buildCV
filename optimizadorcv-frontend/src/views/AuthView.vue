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

const signInGoogle = async () => {
    isLoading.value = true
    errorMessage.value = ""

    try{
      const { error } = await supabase.auth.signInWithOAuth({
        provider: 'google',
        options: {
          redirectTo: `${window.location.origin}/dashboard`
        }
      })
      if (error) throw error
    } catch (error: any) {
      console.error('Error de Auth con Google:', error)
      errorMessage.value = 'Hubo un error al conectar con Google.'
      isLoading.value = false
    }
}

</script>

<template>

  <div class="flex min-h-full flex justify-center px6 py-50 lg:px8">
    <div class="bg-white text-gray-500 max-w-96 mx-4 md:p-6 p-4 text-left text-sm rounded-xl shadow-[0px_0px_10px_0px] shadow-black/10">
      <h2 class="text-2xl font-semibold mb-6 text-center text-gray-800">{{isLogin ? 'Bienvenido de nuevo': 'Crear cuenta'}}</h2>
      <form @submit.prevent="handleAuth">
          <input id="email" v-model="email" class="w-full bg-white border my-3 border-gray-500/30 outline-none rounded-full py-2.5 px-4" type="email" placeholder="Ingresa tu correo" required>
          <input id="password" v-model="password" class="w-full bg-white border mt-1 border-gray-500/30 outline-none rounded-full py-2.5 px-4" type="password" placeholder="Ingresa tu contraseña" required>
          <div class="text-center py-4">
              <a class="text-blue-600 font-medium" href="#">¿Olvidaste tu contraseña?</a>
          </div>
          <button type="submit" class="w-full mb-3 bg-blue-600 hover:bg-blue-500 py-2.5 rounded-full text-white">{{isLogin ? 'Iniciar Sesion': 'Crear Cuenta'}}</button>
      </form>
      <p class="text-center mt-4">{{isLogin ? '¿Aún no tienes una cuenta?': '¿Ya tienes una cuenta?'}} <a href="#" class="text-blue-600 font-medium cursor-pointer" @click="isLogin = !isLogin">{{isLogin ? 'Crear Cuenta': 'Inicia Sesión'}}</a></p>

      <button type="button" @click="signInGoogle" :disabled="isLoading" class="w-full flex items-center gap-2 justify-center my-3 bg-white border border-gray-500/30 py-2.5 rounded-full text-gray-800">
        <img class="h-4 w-4" src="https://raw.githubusercontent.com/prebuiltui/prebuiltui/main/assets/login/googleFavicon.png" alt="googleFavicon">
        {{ isLoading ? 'Conectando...' : 'Ingresa con Google' }}
      </button>
    </div>
  </div>
  

</template>