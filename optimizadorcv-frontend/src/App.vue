<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { supabase } from './supabase'
import { savedCVs, currentUser } from './store' // Importamos la memoria central

// Importamos las nuevas vistas
import AuthView from './views/AuthView.vue'
import UploadView from './views/UploadView.vue'
import TemplatesView from './views/TemplatesView.vue'
import SavedView from './views/SavedView.vue'
import GenerateView from './views/GenerateView.vue'
import EditorView from './views/EditorView.vue'

const currentView = ref('upload')

const changeView = (view: string) => {
  currentView.value = view
}

const cerrarSesion = async () => {
  await supabase.auth.signOut()
  currentUser.value = null
  savedCVs.value = []
}

// Carga inicial de Supabase (Se queda aquí porque es global)
onMounted(async () => {
  const { data: { session } } = await supabase.auth.getSession()

  if (session) {
    currentUser.value = session.user
    cargarDatos()
  }
  supabase.auth.onAuthStateChange((_event, session) => {
    currentUser.value = session?.user || null
    if (currentUser.value) {
      cargarDatos()
    }
  })
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

  <AuthView v-if="!currentUser" @logged-in="changeView('upload')" />
  
  <div v-else class="min-h-screen text-zinc-100 flex font-sans">
    
    <aside class="w-80 border-r border-zinc-200 p-6 hidden lg:flex flex-col gap-4">
      <h1 class="text-2xl font-bold text-black tracking-wider">
        Build<span class="text-[#89CFF0]">CV</span>
      </h1>
      
      <nav class="mt-8 flex flex-col gap-2">
        <a href="#" @click="changeView('upload')" class="px-4 py-2 cursor-pointer hover:bg-zinc-100 hover:text-black rounded-lg text-zinc-400 font-medium active transition-colors">Crear nuevo CV</a>
        <a href="#" @click="changeView('templates')" class="px-4 py-2 cursor-pointer hover:bg-zinc-100 hover:text-black rounded-lg text-zinc-400 font-medium transition-colors">Plantillas</a>
        <a href="#" @click="changeView('saved')" :class="['px-4 py-2 cursor-pointer rounded-lg transition-colors', currentView === 'saved' ? 'bg-zinc-100 text-black' : 'text-zinc-400 hover:bg-zinc-100 hover:text-black']">Mis CVs guardados</a>
        <a href="#" @click="changeView('generate')" class="px-4 py-2 cursor-pointer hover:bg-zinc-100 hover:text-black rounded-lg text-zinc-400 transition-colors">Generar CV</a>
      </nav>
      
      <div class="mt-auto pt-6 border-t border-zinc-200">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-8 h-8 rounded-full bg-[#89CFF0] text-white flex items-center justify-center font-bold uppercase">
             {{ currentUser.email?.charAt(0) }}
          </div>
          <div class="overflow-hidden">
            <p class="text-sm font-medium text-zinc-500 truncate">{{ currentUser.email }}</p>
          </div>
        </div>
        <button @click="cerrarSesion" class="w-full text-left px-4 py-2 text-sm text-red-400 hover:bg-red-500/10 rounded-lg transition-colors">
          Cerrar sesión
        </button>
      </div>
    </aside>

    <main class="flex-1 p-6 md:p-10 overflow-y-auto">
      <!-- Cuando termine de procesar, llévame al editor -->
      <UploadView v-if="currentView === 'upload'" @processed="changeView('editor')" />
      
      <TemplatesView v-else-if="currentView === 'templates'" />
      
      <!-- Cuando seleccione un CV, llévame al editor -->
      <SavedView v-else-if="currentView === 'saved'" @select-cv="changeView('editor')" />
      
      <!-- Cuando termine de generar, llévame al editor -->
      <GenerateView v-else-if="currentView === 'generate'" @generated="changeView('editor')" />
      
      <!-- Cuando guarde, devuélveme a la galería de guardados -->
      <EditorView v-else-if="currentView === 'editor'" @saved="changeView('saved')" />
    </main>
  </div>
</template>