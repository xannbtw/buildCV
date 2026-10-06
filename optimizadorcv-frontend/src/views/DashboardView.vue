<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../supabase'
import { savedCVs, currentUser } from '../store'

import UploadView from './UploadView.vue'
import TemplatesView from './TemplatesView.vue'
import SavedView from './SavedView.vue'
import GenerateView from './GenerateView.vue'
import EditorView from './EditorView.vue'

const router = useRouter()

const menuAbierto = ref(false)
const currentView = ref('upload')

const changeView = (view: string) => {
  currentView.value = view
}

const cerrarSesion = async () => {
  await supabase.auth.signOut()
  currentUser.value = null
  savedCVs.value = []
  router.push('/login')
}

onMounted(() => {
  if (currentUser.value) {
    cargarDatos()
  }
})

const cargarDatos = async () => {
  const { data, error } = await supabase
    .from('cv_guardados')
    .select('*')
    .eq('user_id', currentUser.value.id)
    
  if (data) {
    savedCVs.value = data.map(fila => ({
      id: fila.id, nombre: fila.nombre, date: fila.fecha, data: fila.datos_json
    }))
  }
}
</script>

<template>
  <div class="min-h-screen text-zinc-100 flex flex-col lg:flex-row font-sans">
    
    <header class="lg:hidden flex items-center justify-between bg-white p-4 w-full border-b border-zinc-200">
      <h1 class="text-xl font-bold text-black tracking-wider">
        Build<span class="text-[#89CFF0]">CV</span>
      </h1>
      <button @click="menuAbierto = !menuAbierto" class="text-zinc-500 focus:outline-none p-1">
        <svg v-if="!menuAbierto" class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
        <svg v-else class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </header>

    <div 
      v-if="menuAbierto" 
      @click="menuAbierto = false" 
      class="fixed inset-0 bg-black/40 z-40 lg:hidden"
    ></div>
    
    <aside :class="[
        'w-80 border-r border-zinc-200 p-6 flex flex-col gap-4 bg-white',
        'fixed inset-y-0 left-0 z-50 transition-transform duration-300 ease-in-out',
        'lg:relative lg:translate-x-0', 
        menuAbierto ? 'translate-x-0 shadow-2xl' : '-translate-x-full'
      ]">
      <h1 class="text-2xl font-bold text-black tracking-wider hidden lg:block">
        Build<span class="text-[#89CFF0]">CV</span>
      </h1>
      
      <nav class="mt-8 flex flex-col gap-2">
        <a href="#" @click.prevent="changeView('upload'); menuAbierto = false" :class="['px-4 py-2 cursor-pointer rounded-lg transition-colors font-medium', currentView === 'upload' ? 'bg-zinc-100 text-black' : 'text-zinc-500 hover:bg-zinc-100 hover:text-black']">Crear nuevo CV</a>
        <!-- <a href="#" @click.prevent="changeView('templates'); menuAbierto = false" :class="['px-4 py-2 cursor-pointer rounded-lg transition-colors font-medium', currentView === 'templates' ? 'bg-zinc-100 text-black' : 'text-zinc-500 hover:bg-zinc-100 hover:text-black']">Plantillas</a> -->
        <a href="#" @click.prevent="changeView('saved'); menuAbierto = false" :class="['px-4 py-2 cursor-pointer rounded-lg transition-colors font-medium', currentView === 'saved' ? 'bg-zinc-100 text-black' : 'text-zinc-500 hover:bg-zinc-100 hover:text-black']">Mis CVs guardados</a>
        <a href="#" @click.prevent="changeView('generate'); menuAbierto = false" :class="['px-4 py-2 cursor-pointer rounded-lg transition-colors font-medium', currentView === 'generate' ? 'bg-zinc-100 text-black' : 'text-zinc-500 hover:bg-zinc-100 hover:text-black']">Generar CV</a>
      </nav>
      
      <div class="mt-auto pt-6 border-t border-zinc-200">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-8 h-8 rounded-full bg-[#89CFF0] text-white flex items-center justify-center font-bold uppercase">
              {{ currentUser?.email?.charAt(0) || 'U' }}
          </div>
          <div class="overflow-hidden">
            <p class="text-sm font-medium text-zinc-500 truncate">{{ currentUser?.email || 'Usuario' }}</p>
          </div>
        </div>
        <button @click="cerrarSesion" class="w-full text-left px-4 py-2 text-sm text-red-400 hover:bg-red-500/10 rounded-lg transition-colors">
          Cerrar sesión
        </button>
      </div>
    </aside>

    <main class="flex-1 p-6 md:p-10 overflow-y-auto bg-zinc-50">
      <UploadView v-if="currentView === 'upload'" @processed="changeView('editor')" />
      
      <TemplatesView v-else-if="currentView === 'templates'" />
      
      <SavedView v-else-if="currentView === 'saved'" @select-cv="changeView('editor')" />
      
      <GenerateView v-else-if="currentView === 'generate'" @generated="changeView('editor')" />
      
      <EditorView v-else-if="currentView === 'editor'" @saved="changeView('saved')" />
    </main>
    
  </div>
</template>