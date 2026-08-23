<script setup lang="ts">
import { ref } from 'vue'

const templates = ref ([
    {
      id: 'jake-ryan',
      name: 'Jake Ryan',
      description: 'Un CV moderno y minimalista ideal para2 perfiles tecnológicos. Muy limpio y fácil de leer por sistemas ATS.',

      previewBg: 'bg-gradient-to-br from-zinc-200 to-zinc-400'
    },
    {
      id: 'harvard',
      name: 'Harvard',
      description: 'Clásico, académico y elegante.',
      previewBg: 'bg-gradient-to-br from-zinc-100 to-zinc-300'
    },
    {
      id: 'modern',
      name: 'MIT',
      description: 'Basado en el curriculum vitae del Instituto de Tecnología de Massachusetts.',
      previewBg: 'bg-gradient-to-br from-zinc-300 to-zinc-500'
    },
    {
      id: 'stanford',
      name: 'Stanford',
      description: '',
      previewBg: 'bg-gradient-to-br from-zinc-200 to-zinc-300'
    }
  ])
</script>

<template>
  <div>
    <header class="mb-8">
          <h2 class="text-3xl font-semibold text-zinc-900">Plantillas</h2>
          <p class="text-zinc-500 mt-2 text-sm">Explora nuestros diseños optimizados para superar los filtros ATS.</p>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <article 
            v-for="template in templates" 
            :key="template.id"
            class="group relative bg-zinc-900/1 hover:bg-zinc-200 border border-zinc-800/50 hover:border-zinc-100 rounded-xl overflow-hidden flex flex-col transition-all duration-200"
          >
            <div class="h-64 p-6 flex items-center justify-center relative overflow-hidden">
              <div :class="['w-3/4 h-full shadow-2xl rounded-t-md transform transition-transform duration-300 group-hover:-translate-y-2', template.previewBg]"></div>
            </div>
            <div class="p-5">
              <h4 class="text-lg font-medium text-zinc-500 group-hover:text-zinc-500 transition-colors mb-1">
                {{ template.name }}
              </h4>
              <p class="text-sm text-zinc-500">
                {{ template.description }}
              </p>
            </div>
          </article>
        </div>
      </div>
</template>