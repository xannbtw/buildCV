<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const isOpen = ref(false)

const activeFaq = ref<number | null>(0)

const activeComparisonTab = ref<'after' | 'before'>('after')

const navItems = [
  { name: 'El Problema', href: '#problema' },
  { name: 'Beneficios', href: '#beneficios' },
  { name: 'Cómo Funciona', href: '#como-funciona' },
  { name: 'Plantillas', href: '#plantillas' },
  { name: 'FAQ', href: '#faq' }
]

const toggleFaq = (index: number) => {
  activeFaq.value = activeFaq.value === index ? null : index
}

const irALogin = () => {
  router.push('/login')
}
</script>

<template>
  <div class="min-h-screen bg-[#FAFAFA] text-zinc-900 font-sans selection:bg-[#89CFF0]/30 selection:text-zinc-900">
    <header class="fixed top-0 left-0 w-full z-50 bg-white/80 backdrop-blur-lg border-b border-zinc-200/80 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 sm:h-20">
          
          <div class="flex-shrink-0 flex items-center">
            <a href="#" class="text-2xl font-black tracking-tight text-zinc-900 flex items-center gap-1 group">
              <span class="w-8 h-8 rounded-xl bg-[#89CFF0]/20 flex items-center justify-center text-[#89CFF0] font-bold text-lg border border-[#89CFF0]/40 group-hover:scale-105 transition-transform">
                B
              </span>
              <span>uild<span class="text-[#89CFF0]">CV</span></span>
            </a>
          </div>

          <nav class="hidden md:flex items-center space-x-1 lg:space-x-2 bg-zinc-100/80 px-4 py-1.5 rounded-full border border-zinc-200/60">
            <a 
              v-for="item in navItems" 
              :key="item.name" 
              :href="item.href" 
              class="text-xs lg:text-sm font-medium text-zinc-600 hover:text-zinc-950 px-3 py-1 rounded-full hover:bg-white transition-all duration-150"
            >
              {{ item.name }}
            </a>
          </nav>

          <div class="hidden md:flex items-center gap-3">
            <button 
              @click="irALogin" 
              class="text-sm font-semibold text-zinc-700 hover:text-zinc-950 px-4 py-2 rounded-xl transition-colors duration-150"
            >
              Iniciar Sesión
            </button>
            <button 
              @click="irALogin" 
              class="inline-flex items-center justify-center px-4 py-2.5 text-sm font-semibold rounded-xl text-white bg-[#89CFF0] hover:bg-[#78bee0] active:scale-[0.98] transition-all duration-200 shadow-sm shadow-[#89CFF0]/40"
            >
              Comenzar Gratis
            </button>
          </div>

          <div class="md:hidden flex items-center">
            <button 
              @click="isOpen = !isOpen" 
              type="button" 
              class="p-2 rounded-xl text-zinc-600 hover:text-zinc-900 hover:bg-zinc-100 focus:outline-none transition-colors"
              aria-label="Abrir menú"
            >
              <svg v-if="!isOpen" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
              <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div v-show="isOpen" class="md:hidden bg-white/95 backdrop-blur-lg border-b border-zinc-200 px-4 pt-3 pb-6 space-y-2">
        <a 
          v-for="item in navItems" 
          :key="item.name" 
          :href="item.href" 
          @click="isOpen = false" 
          class="block px-3 py-2.5 rounded-lg text-base font-medium text-zinc-700 hover:text-zinc-950 hover:bg-zinc-100 transition-colors"
        >
          {{ item.name }}
        </a>
        <div class="pt-4 border-t border-zinc-100 flex flex-col gap-2">
          <button 
            @click="irALogin" 
            class="w-full py-2.5 text-center text-sm font-semibold text-zinc-700 bg-zinc-100 rounded-xl"
          >
            Iniciar Sesión
          </button>
          <button 
            @click="irALogin" 
            class="w-full py-2.5 text-center text-sm font-semibold text-white bg-[#89CFF0] rounded-xl shadow-sm"
          >
            Comenzar Gratis
          </button>
        </div>
      </div>
    </header>

    <section class="relative pt-32 sm:pt-40 pb-20 sm:pb-28 overflow-hidden">
      <div class="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-[#89CFF0]/20 rounded-full blur-3xl pointer-events-none -z-10"></div>
      <div class="absolute top-1/3 left-1/4 w-[300px] h-[200px] bg-zinc-200/50 rounded-full blur-2xl pointer-events-none -z-10"></div>

      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-zinc-200 shadow-sm text-xs font-semibold text-zinc-800 mb-8 animate-fade-in">
          <span class="flex h-2 w-2 relative">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#89CFF0] opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-[#89CFF0]"></span>
          </span>
          Potenciado con IA · Diseñado para superar filtros ATS
        </div>

        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-zinc-950 tracking-tight max-w-4xl mx-auto leading-[1.12]">
          Deja de enviar el mismo CV a todas las vacantes.
          <span class="block mt-2 text-transparent bg-clip-text bg-gradient-to-r from-zinc-900 via-zinc-700 to-[#89CFF0]">
            Adáptalo en segundos con IA.
          </span>
        </h1>

        <p class="mt-6 text-lg sm:text-xl text-zinc-600 max-w-2xl mx-auto font-normal leading-relaxed">
          Sube tu currículum, pega la descripción de la oferta y genera una versión quirúrgicamente adaptada con formato ATS profesional. Multiplica tus entrevistas sin horas de trabajo manual.
        </p>

        <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4 max-w-md mx-auto">
          <button 
            @click="irALogin" 
            class="w-full sm:w-auto px-8 py-3.5 rounded-xl font-semibold text-white bg-[#89CFF0] hover:bg-[#78bee0] transition-all shadow-md shadow-[#89CFF0]/30 hover:shadow-lg hover:shadow-[#89CFF0]/40 active:scale-[0.98] flex items-center justify-center gap-2"
          >
            <span>Crear mi CV Gratis</span>
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </button>
          
          <a 
            href="#como-funciona" 
            class="w-full sm:w-auto px-6 py-3.5 rounded-xl font-medium text-zinc-700 bg-white hover:bg-zinc-50 border border-zinc-200 transition-all shadow-sm flex items-center justify-center gap-2"
          >
            <svg class="w-4 h-4 text-zinc-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>Ver cómo funciona</span>
          </a>
        </div>

        <div class="mt-14 pt-8 border-t border-zinc-200/80 grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto text-left">
          <div class="flex flex-col">
            <span class="text-2xl sm:text-3xl font-bold text-zinc-950">+85%</span>
            <span class="text-xs sm:text-sm text-zinc-500 font-medium mt-0.5">Tasa de respuesta de reclutadores</span>
          </div>
          <div class="flex flex-col">
            <span class="text-2xl sm:text-3xl font-bold text-zinc-950">&lt; 30s</span>
            <span class="text-xs sm:text-sm text-zinc-500 font-medium mt-0.5">Para adaptar a una nueva oferta</span>
          </div>
          <div class="flex flex-col">
            <span class="text-2xl sm:text-3xl font-bold text-zinc-950">100%</span>
            <span class="text-xs sm:text-sm text-zinc-500 font-medium mt-0.5">Formatos ATS-Friendly estándar</span>
          </div>
          <div class="flex flex-col">
            <span class="text-2xl sm:text-3xl font-bold text-[#89CFF0]">Gratis</span>
            <span class="text-xs sm:text-sm text-zinc-500 font-medium mt-0.5">Comienza sin tarjeta de crédito</span>
          </div>
        </div>

        <div class="mt-16 relative mx-auto max-w-5xl">
          <div class="relative rounded-2xl p-2 sm:p-4 bg-zinc-900/5 border border-zinc-200 shadow-2xl backdrop-blur-sm">
            
            <div class="bg-white rounded-xl border border-zinc-200/90 overflow-hidden shadow-inner">
              <div class="px-4 py-3 bg-zinc-50 border-b border-zinc-200 flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <span class="w-3 h-3 rounded-full bg-red-400"></span>
                  <span class="w-3 h-3 rounded-full bg-amber-400"></span>
                  <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
                </div>
                <div class="text-xs font-mono text-zinc-400 bg-white px-3 py-1 rounded-md border border-zinc-200">
                  buildcv.lat/dashboard
                </div>
                <div class="flex items-center gap-2">
                  <span class="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200 flex items-center gap-1">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                    ATS Match: 98%
                  </span>
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-12 bg-white text-left text-zinc-800">
                <div class="lg:col-span-5 p-5 bg-zinc-50/60 border-r border-zinc-200 flex flex-col justify-between">
                  <div>
                    <div class="flex items-center gap-2 mb-4">
                      <span class="p-1.5 rounded-lg bg-[#89CFF0]/20 text-[#89CFF0]">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                        </svg>
                      </span>
                      <span class="text-xs font-bold uppercase tracking-wider text-zinc-700">Instrucción / Oferta</span>
                    </div>

                    <div class="bg-white p-3.5 rounded-xl border border-zinc-200 text-xs text-zinc-700 space-y-2 mb-4 shadow-sm">
                      <div class="flex justify-between items-center text-[11px] text-zinc-400 border-b border-zinc-100 pb-1.5">
                        <span>Puesto objetivo:</span>
                        <span class="font-semibold text-zinc-700">Senior Full-Stack Engineer</span>
                      </div>
                      <p class="italic text-zinc-600">
                        "Optimiza mi experiencia para destacar arquitectura de microservicios, liderazgo técnico y optimización de rendimiento SQL."
                      </p>
                    </div>

                    <div class="space-y-2">
                      <div class="text-[11px] font-semibold text-zinc-500 uppercase tracking-wider">Palabras Clave Detectadas</div>
                      <div class="flex flex-wrap gap-1.5">
                        <span class="px-2 py-1 bg-white border border-zinc-200 rounded-md text-[11px] font-medium text-zinc-700 flex items-center gap-1">
                          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> TypeScript
                        </span>
                        <span class="px-2 py-1 bg-white border border-zinc-200 rounded-md text-[11px] font-medium text-zinc-700 flex items-center gap-1">
                          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> Vue.js / React
                        </span>
                        <span class="px-2 py-1 bg-white border border-zinc-200 rounded-md text-[11px] font-medium text-zinc-700 flex items-center gap-1">
                          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> Fast API
                        </span>
                        <span class="px-2 py-1 bg-white border border-zinc-200 rounded-md text-[11px] font-medium text-zinc-700 flex items-center gap-1">
                          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> PostgreSQL
                        </span>
                      </div>
                    </div>
                  </div>

                  <div class="mt-6 pt-4 border-t border-zinc-200 flex items-center justify-between">
                    <span class="text-xs text-zinc-500">Plantilla: <strong class="text-zinc-800">Jake Ryan (ATS Standard)</strong></span>
                    <button @click="irALogin" class="text-xs font-semibold px-3 py-1.5 bg-[#89CFF0] text-white rounded-lg shadow-sm hover:bg-[#78bee0] transition-colors">
                      Exportar PDF
                    </button>
                  </div>
                </div>

                <div class="lg:col-span-7 p-6 sm:p-8 bg-white flex flex-col justify-center">
                  <div class="border border-zinc-200 rounded-lg p-6 bg-white shadow-sm font-sans space-y-4">
                    <div class="text-center border-b border-zinc-200 pb-3">
                      <h2 class="text-xl font-bold text-zinc-950 tracking-tight">Alejandro Morales</h2>
                      <p class="text-xs text-zinc-500 mt-0.5">
                        Senior Full-Stack Engineer · alejandro@email.com · +34 600 000 000 · Madrid, España
                      </p>
                    </div>

                    <div>
                      <div class="text-xs font-bold text-zinc-900 uppercase tracking-widest border-b border-zinc-900 pb-0.5 mb-2">
                        Experiencia Laboral
                      </div>
                      
                      <div class="space-y-3 text-xs">
                        <div>
                          <div class="flex justify-between font-semibold text-zinc-900">
                            <span>Tech Lead & Senior Developer — SaaS Global</span>
                            <span class="text-zinc-500 text-[11px]">2022 - Presente</span>
                          </div>
                          <ul class="list-disc list-inside mt-1 text-zinc-600 space-y-1 pl-1">
                            <li>Lideró la migración de arquitectura monolítica a microservicios, <strong class="text-zinc-900 font-medium">reduciendo la latencia de respuesta en un 42%</strong>.</li>
                            <li>Diseñó pipelines de CI/CD automatizados y optimizó consultas en PostgreSQL para soportar +500k usuarios activos diarios.</li>
                          </ul>
                        </div>
                      </div>
                    </div>

                    <div>
                      <div class="text-xs font-bold text-zinc-900 uppercase tracking-widest border-b border-zinc-900 pb-0.5 mb-2">
                        Educación & Habilidades
                      </div>
                      <div class="flex justify-between text-xs text-zinc-700 font-medium">
                        <span>Grado en Ingeniería Informática — Universidad Politécnica</span>
                        <span class="text-zinc-500 text-[11px]">2017 - 2021</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="problema" class="py-20 sm:py-28 bg-zinc-900 text-white relative overflow-hidden">
      <div class="absolute -right-20 top-1/2 -translate-y-1/2 w-96 h-96 bg-[#89CFF0]/10 rounded-full blur-3xl pointer-events-none"></div>

      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl text-left sm:text-center sm:mx-auto mb-16">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-500/10 text-red-400 border border-red-500/20 text-xs font-semibold uppercase tracking-wider mb-4">
            El Obstáculo Invisible
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-white">
            ¿Por qué el 75% de los CVs son descartados antes de que una persona los lea?
          </h2>
          <p class="mt-4 text-base sm:text-lg text-zinc-400">
            La mayoría de candidatos no fallan por falta de talento, sino por enviar currículums genéricos que chocan contra los filtros automáticos ATS (Applicant Tracking Systems).
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
          
          <div class="bg-zinc-800/60 border border-zinc-700/60 rounded-2xl p-6 sm:p-8 hover:border-zinc-500 transition-colors">
            <div class="w-12 h-12 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 flex items-center justify-center mb-6">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">Filtros ATS Inflexibles</h3>
            <p class="text-sm text-zinc-400 leading-relaxed">
              Las empresas utilizan software que escanea palabras clave específicas. Si tu CV no está calibrado a la descripción exacta del puesto, tu postulación se descarta en segundos.
            </p>
          </div>

          <div class="bg-zinc-800/60 border border-zinc-700/60 rounded-2xl p-6 sm:p-8 hover:border-zinc-500 transition-colors">
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center mb-6">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">Horas Perdidas Reescribiendo</h3>
            <p class="text-sm text-zinc-400 leading-relaxed">
              Adaptar manualmente tu currículum para cada oferta toma entre 45 y 90 minutos por postulación. Un proceso agotador e insostenible cuando aplicas a decenas de vacantes.
            </p>
          </div>

          <div class="bg-zinc-800/60 border border-zinc-700/60 rounded-2xl p-6 sm:p-8 hover:border-zinc-500 transition-colors">
            <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-400 flex items-center justify-center mb-6">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">Formatos Rotos e Incompatibles</h3>
            <p class="text-sm text-zinc-400 leading-relaxed">
              Diseños gráficos recargados (como plantillas con barras de habilidades, tablas complejas o iconos) confunden a los parsers automáticos y destruyen tu legibilidad.
            </p>
          </div>

        </div>
      </div>
    </section>

    <!-- SECCIÓN: BENEFICIOS -->
    <section id="beneficios" class="py-20 sm:py-28 bg-white border-b border-zinc-200/80">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-2xl text-left sm:text-center sm:mx-auto mb-16">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#89CFF0]/20 text-[#3b93bf] border border-[#89CFF0]/40 text-xs font-semibold uppercase tracking-wider mb-4">
            La Solución BuildCV
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-zinc-950">
            Todo lo que necesitas para que tu CV destaque de verdad
          </h2>
          <p class="mt-4 text-base sm:text-lg text-zinc-600">
            Una plataforma minimalista pensada en velocidad, precisión y resultados comprobados.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <div class="md:col-span-2 bg-zinc-50 border border-zinc-200 rounded-3xl p-8 flex flex-col justify-between hover:shadow-lg transition-all duration-200">
            <div>
              <div class="w-12 h-12 rounded-2xl bg-[#89CFF0] text-white flex items-center justify-center mb-6 shadow-sm shadow-[#89CFF0]/30">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 class="text-2xl font-bold text-zinc-950 mb-3">Adaptación Quirúrgica con IA</h3>
              <p class="text-zinc-600 max-w-xl leading-relaxed text-sm sm:text-base">
                Nuestra IA analiza tu trayectoria real y la reformula para resaltar los logros, habilidades y tecnologías exactas que solicita cada vacante, sin inventar información falsa.
              </p>
            </div>
            
            <div class="mt-8 pt-6 border-t border-zinc-200/80 flex flex-wrap gap-2">
              <span class="px-3 py-1 bg-white border border-zinc-200 rounded-full text-xs font-medium text-zinc-700">Extracción inteligente de PDF</span>
              <span class="px-3 py-1 bg-white border border-zinc-200 rounded-full text-xs font-medium text-zinc-700">Verbos de acción cuantificables</span>
              <span class="px-3 py-1 bg-white border border-zinc-200 rounded-full text-xs font-medium text-zinc-700">Alineación con ATS</span>
            </div>
          </div>

          <div class="bg-zinc-50 border border-zinc-200 rounded-3xl p-8 flex flex-col justify-between hover:shadow-lg transition-all duration-200">
            <div>
              <div class="w-12 h-12 rounded-2xl bg-zinc-900 text-white flex items-center justify-center mb-6 shadow-sm">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="text-xl font-bold text-zinc-950 mb-3">100% ATS-Friendly</h3>
              <p class="text-zinc-600 text-sm leading-relaxed">
                Plantillas limpias aprobadas por estándares de Harvard y Jake Ryan. Sin columnas rotas ni gráficos indescifrables.
              </p>
            </div>
            <div class="mt-6 text-xs font-semibold text-zinc-900 flex items-center gap-1">
              <span>Supera escáneres automáticos</span>
              <svg class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
          </div>

          <div class="bg-zinc-50 border border-zinc-200 rounded-3xl p-8 flex flex-col justify-between hover:shadow-lg transition-all duration-200">
            <div>
              <div class="w-12 h-12 rounded-2xl bg-zinc-900 text-white flex items-center justify-center mb-6 shadow-sm">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </div>
              <h3 class="text-xl font-bold text-zinc-950 mb-3">Editor en Tiempo Real</h3>
              <p class="text-zinc-600 text-sm leading-relaxed">
                Visualiza los cambios al instante en un lienzo fiel A4. Edita cada viñeta, empresa o dato con total libertad.
              </p>
            </div>
            <div class="mt-6 text-xs font-semibold text-zinc-900 flex items-center gap-1">
              <span>Control total de tu contenido</span>
            </div>
          </div>

          <div class="md:col-span-2 bg-zinc-50 border border-zinc-200 rounded-3xl p-8 flex flex-col justify-between hover:shadow-lg transition-all duration-200">
            <div>
              <div class="w-12 h-12 rounded-2xl bg-[#89CFF0] text-white flex items-center justify-center mb-6 shadow-sm shadow-[#89CFF0]/30">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2 1 3 3 3h10c2 0 3-1 3-3V7c0-2-1-3-3-3H7c-2 0-3 1-3 3zm0 5h16" />
                </svg>
              </div>
              <h3 class="text-2xl font-bold text-zinc-950 mb-3">Gestor de Versiones en la Nube</h3>
              <p class="text-zinc-600 max-w-xl leading-relaxed text-sm sm:text-base">
                Mantén un historial organizado con todas tus variantes de currículum ("CV Frontend", "CV Tech Lead", "CV Fintech"). Descarga o actualiza cualquiera de ellos en un solo clic.
              </p>
            </div>
            
            <div class="mt-8 pt-6 border-t border-zinc-200/80 flex items-center justify-between">
              <span class="text-xs text-zinc-500 font-medium">Exportación en PDF directo y nítido</span>
              <button @click="irALogin" class="text-xs font-bold text-zinc-900 hover:text-[#89CFF0] transition-colors flex items-center gap-1">
                Explorar Dashboard
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- SECCIÓN: CÓMO FUNCIONA -->
    <section id="como-funciona" class="py-20 sm:py-28 bg-[#FAFAFA] relative">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-2xl text-left sm:text-center sm:mx-auto mb-16">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zinc-200/80 text-zinc-800 border border-zinc-300 text-xs font-semibold uppercase tracking-wider mb-4">
            Flujo en 3 Pasos
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-zinc-950">
            De un CV genérico a una postulación ganadora en 30 segundos
          </h2>
          <p class="mt-4 text-base sm:text-lg text-zinc-600">
            Sin curvas de aprendizaje complejas. Sube, adapta y postula.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
          
          <div class="bg-white border border-zinc-200 rounded-3xl p-8 shadow-sm flex flex-col justify-between relative group hover:border-[#89CFF0] transition-colors">
            <div class="absolute -top-4 left-8 bg-zinc-950 text-white text-xs font-bold px-3 py-1 rounded-full border border-zinc-700">
              PASO 01
            </div>
            <div>
              <div class="w-12 h-12 rounded-2xl bg-zinc-100 text-zinc-800 flex items-center justify-center mb-6 mt-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
              </div>
              <h3 class="text-xl font-bold text-zinc-950 mb-2">Sube tu CV actual</h3>
              <p class="text-sm text-zinc-600 leading-relaxed">
                Arrastra tu PDF base. Nuestro motor de IA extrae automáticamente tu experiencia laboral, educación y datos clave sin desordenar nada.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-zinc-100 text-xs text-zinc-400">
              Formatos soportados: PDF estándar
            </div>
          </div>

          <div class="bg-white border border-zinc-200 rounded-3xl p-8 shadow-sm flex flex-col justify-between relative group hover:border-[#89CFF0] transition-colors">
            <div class="absolute -top-4 left-8 bg-[#89CFF0] text-white text-xs font-bold px-3 py-1 rounded-full border border-[#89CFF0]">
              PASO 02
            </div>
            <div>
              <div class="w-12 h-12 rounded-2xl bg-[#89CFF0]/20 text-[#3b93bf] flex items-center justify-center mb-6 mt-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 class="text-xl font-bold text-zinc-950 mb-2">Indica la vacante deseada</h3>
              <p class="text-sm text-zinc-600 leading-relaxed">
                Pega el texto de la oferta de trabajo o dale una instrucción específica (ej. "Enfocar para puesto de DevOps Lead"). La IA adaptará las viñetas.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-zinc-100 text-xs text-zinc-400">
              Optimización de keywords en tiempo real
            </div>
          </div>

          <div class="bg-white border border-zinc-200 rounded-3xl p-8 shadow-sm flex flex-col justify-between relative group hover:border-[#89CFF0] transition-colors">
            <div class="absolute -top-4 left-8 bg-zinc-950 text-white text-xs font-bold px-3 py-1 rounded-full border border-zinc-700">
              PASO 03
            </div>
            <div>
              <div class="w-12 h-12 rounded-2xl bg-zinc-100 text-zinc-800 flex items-center justify-center mb-6 mt-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </div>
              <h3 class="text-xl font-bold text-zinc-950 mb-2">Revisa y Descarga tu PDF</h3>
              <p class="text-sm text-zinc-600 leading-relaxed">
                Verifica la vista previa, ajusta cualquier detalle en el editor en vivo y descarga tu PDF listo para postular y captar la atención de Recursos Humanos.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-zinc-100 text-xs text-zinc-400">
              Descarga sin marcas de agua molestas
            </div>
          </div>

        </div>

        <div class="mt-14 bg-white border border-zinc-200 rounded-2xl p-6 sm:p-8 flex flex-col sm:flex-row items-center justify-between gap-6 shadow-sm">
          <div class="text-left">
            <h4 class="text-lg font-bold text-zinc-950">¿Listo para probarlo con tu currículum?</h4>
            <p class="text-sm text-zinc-600 mt-1">Crea tu cuenta gratuita y genera tu primera versión en menos de un minuto.</p>
          </div>
          <button 
            @click="irALogin" 
            class="px-6 py-3 rounded-xl font-semibold text-white bg-[#89CFF0] hover:bg-[#78bee0] transition-colors whitespace-nowrap shadow-sm"
          >
            Optimizar mi CV ahora
          </button>
        </div>

      </div>
    </section>

    <!-- SECCIÓN: COMPARATIVA INTERACTIVA (ANTES VS DESPUÉS) -->
    <section class="py-20 sm:py-28 bg-white border-y border-zinc-200/80">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-2xl text-center mx-auto mb-12">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#89CFF0]/20 text-[#3b93bf] border border-[#89CFF0]/40 text-xs font-semibold uppercase tracking-wider mb-4">
            Comparativa Real
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-zinc-950">
            La diferencia entre un CV rechazado y uno llamado a entrevista
          </h2>
        </div>

        <div class="flex justify-center mb-8">
          <div class="inline-flex p-1 bg-zinc-100 rounded-xl border border-zinc-200">
            <button 
              @click="activeComparisonTab = 'after'"
              :class="[
                'px-5 py-2.5 rounded-lg text-xs sm:text-sm font-semibold transition-all duration-150 flex items-center gap-2',
                activeComparisonTab === 'after' 
                  ? 'bg-white text-zinc-900 shadow-sm border border-zinc-200/80' 
                  : 'text-zinc-500 hover:text-zinc-900'
              ]"
            >
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              Con BuildCV (ATS Optimizado)
            </button>
            <button 
              @click="activeComparisonTab = 'before'"
              :class="[
                'px-5 py-2.5 rounded-lg text-xs sm:text-sm font-semibold transition-all duration-150 flex items-center gap-2',
                activeComparisonTab === 'before' 
                  ? 'bg-white text-zinc-900 shadow-sm border border-zinc-200/80' 
                  : 'text-zinc-500 hover:text-zinc-900'
              ]"
            >
              <span class="w-2 h-2 rounded-full bg-red-500"></span>
              CV Genérico Tradicional
            </button>
          </div>
        </div>

        <div class="border border-zinc-200 rounded-2xl p-6 sm:p-8 bg-zinc-50 shadow-sm text-left transition-all">
          
          <div v-if="activeComparisonTab === 'after'" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-zinc-200 pb-4">
              <div>
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                  Aprobado por ATS & Reclutador (Score: 98/100)
                </span>
                <h3 class="text-lg font-bold text-zinc-950 mt-2">Viñetas orientadas a impacto, métricas y palabras clave de la oferta</h3>
              </div>
              <span class="text-xs text-zinc-400 font-mono">Formato Jake Ryan Clean</span>
            </div>

            <div class="space-y-4">
              <div class="bg-white p-4 rounded-xl border border-zinc-200">
                <div class="flex justify-between items-baseline font-bold text-sm text-zinc-900 mb-1">
                  <span>Senior Software Engineer — Plataforma Fintech</span>
                  <span class="text-xs text-zinc-500 font-normal">2021 - Presente</span>
                </div>
                <ul class="space-y-2 text-xs text-zinc-700 mt-2">
                  <li class="flex items-start gap-2">
                    <span class="text-emerald-600 font-bold mt-0.5">✓</span>
                    <span>Lideró la refactorización del motor de pagos con <strong>Node.js y PostgreSQL</strong>, disminuyendo los tiempos de transacción en un <strong>35%</strong> para +1.2M de operaciones mensuales.</span>
                  </li>
                  <li class="flex items-start gap-2">
                    <span class="text-emerald-600 font-bold mt-0.5">✓</span>
                    <span>Implementó pruebas de integración automatizadas alcanzando un <strong>94% de cobertura de código</strong> y reduciendo bugs en producción en un <strong>28%</strong>.</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div v-else class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-zinc-200 pb-4">
              <div>
                <span class="text-xs font-bold uppercase tracking-wider text-red-600 bg-red-50 px-2.5 py-1 rounded-full border border-red-200">
                  Descartado por ATS (Score: 42/100)
                </span>
                <h3 class="text-lg font-bold text-zinc-950 mt-2">Descripciones vagas sin métricas ni relación con los requisitos de la vacante</h3>
              </div>
              <span class="text-xs text-zinc-400 font-mono">Formato Genérico</span>
            </div>

            <div class="space-y-4 opacity-75">
              <div class="bg-white p-4 rounded-xl border border-red-200/80">
                <div class="flex justify-between items-baseline font-bold text-sm text-zinc-900 mb-1">
                  <span>Desarrollador — Empresa</span>
                  <span class="text-xs text-zinc-500 font-normal">2021 - Presente</span>
                </div>
                <ul class="space-y-2 text-xs text-zinc-600 mt-2">
                  <li class="flex items-start gap-2">
                    <span class="text-red-500 font-bold mt-0.5">✕</span>
                    <span>Responsable de programar nuevas funcionalidades para la web y dar soporte al equipo.</span>
                  </li>
                  <li class="flex items-start gap-2">
                    <span class="text-red-500 font-bold mt-0.5">✕</span>
                    <span>Mantenimiento de bases de datos y tareas generales asignadas por el líder técnico.</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- SECCIÓN: SHOWCASE DE PLANTILLAS -->
    <section id="plantillas" class="py-20 sm:py-28 bg-[#FAFAFA]">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-2xl text-left sm:text-center sm:mx-auto mb-16">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zinc-200 text-zinc-800 text-xs font-semibold uppercase tracking-wider mb-4">
            Formatos Estándar de la Industria
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-zinc-950">
            Plantillas diseñadas para ser leídas por máquinas y humanos
          </h2>
          <p class="mt-4 text-base sm:text-lg text-zinc-600">
            Diseños limpios basados en los estándares de las mejores universidades y empresas tecnológicas.
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          
          <div class="bg-white border border-zinc-200 rounded-2xl p-5 flex flex-col justify-between hover:shadow-md hover:border-zinc-400 transition-all">
            <div>
              <div class="h-44 bg-gradient-to-br from-zinc-100 to-zinc-200 rounded-xl mb-4 border border-zinc-200/80 p-3 flex flex-col justify-between overflow-hidden shadow-inner">
                <div class="w-1/2 h-2.5 bg-zinc-400 rounded-sm mb-2"></div>
                <div class="space-y-1.5 opacity-60">
                  <div class="w-full h-1.5 bg-zinc-400 rounded-sm"></div>
                  <div class="w-4/5 h-1.5 bg-zinc-300 rounded-sm"></div>
                  <div class="w-3/4 h-1.5 bg-zinc-300 rounded-sm"></div>
                </div>
                <div class="space-y-1 opacity-60">
                  <div class="w-full h-1.5 bg-zinc-400 rounded-sm"></div>
                  <div class="w-2/3 h-1.5 bg-zinc-300 rounded-sm"></div>
                </div>
              </div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-bold text-zinc-950 text-base">Jake Ryan</h4>
                <span class="text-[10px] font-bold text-[#3b93bf] bg-[#89CFF0]/20 px-2 py-0.5 rounded-md">Tech & Devs</span>
              </div>
              <p class="text-xs text-zinc-500 leading-relaxed">
                El diseño preferido por reclutadores en el sector tecnológico. Máxima legibilidad y alta densidad de información.
              </p>
            </div>
          </div>

          <div class="bg-white border border-zinc-200 rounded-2xl p-5 flex flex-col justify-between hover:shadow-md hover:border-zinc-400 transition-all">
            <div>
              <div class="h-44 bg-gradient-to-br from-zinc-50 to-zinc-150 rounded-xl mb-4 border border-zinc-200/80 p-3 flex flex-col justify-between overflow-hidden shadow-inner">
                <div class="w-2/3 mx-auto h-2.5 bg-zinc-500 rounded-sm mb-2"></div>
                <div class="space-y-1.5 opacity-60">
                  <div class="w-full h-1.5 bg-zinc-400 rounded-sm"></div>
                  <div class="w-full h-1.5 bg-zinc-300 rounded-sm"></div>
                  <div class="w-5/6 h-1.5 bg-zinc-300 rounded-sm"></div>
                </div>
                <div class="space-y-1 opacity-60">
                  <div class="w-full h-1.5 bg-zinc-400 rounded-sm"></div>
                  <div class="w-1/2 h-1.5 bg-zinc-300 rounded-sm"></div>
                </div>
              </div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-bold text-zinc-950 text-base">Harvard</h4>
                <span class="text-[10px] font-bold text-zinc-700 bg-zinc-100 px-2 py-0.5 rounded-md">Corporativo</span>
              </div>
              <p class="text-xs text-zinc-500 leading-relaxed">
                Elegante, académico y sobrio. Ideal para finanzas, consultoría, gestión de proyectos y roles ejecutivos.
              </p>
            </div>
          </div>

          <div class="bg-white border border-zinc-200 rounded-2xl p-5 flex flex-col justify-between hover:shadow-md hover:border-zinc-400 transition-all">
            <div>
              <div class="h-44 bg-gradient-to-br from-zinc-200 to-zinc-300 rounded-xl mb-4 border border-zinc-200/80 p-3 flex flex-col justify-between overflow-hidden shadow-inner">
                <div class="w-1/3 h-2.5 bg-zinc-700 rounded-sm mb-2"></div>
                <div class="space-y-1.5 opacity-70">
                  <div class="w-full h-1.5 bg-zinc-600 rounded-sm"></div>
                  <div class="w-11/12 h-1.5 bg-zinc-500 rounded-sm"></div>
                  <div class="w-3/4 h-1.5 bg-zinc-500 rounded-sm"></div>
                </div>
                <div class="space-y-1 opacity-70">
                  <div class="w-full h-1.5 bg-zinc-600 rounded-sm"></div>
                  <div class="w-2/3 h-1.5 bg-zinc-500 rounded-sm"></div>
                </div>
              </div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-bold text-zinc-950 text-base">MIT</h4>
                <span class="text-[10px] font-bold text-zinc-700 bg-zinc-100 px-2 py-0.5 rounded-md">Ingeniería</span>
              </div>
              <p class="text-xs text-zinc-500 leading-relaxed">
                Estructura balanceada que resalta habilidades técnicas duras, publicaciones y proyectos destacados.
              </p>
            </div>
          </div>

          <div class="bg-white border border-zinc-200 rounded-2xl p-5 flex flex-col justify-between hover:shadow-md hover:border-zinc-400 transition-all">
            <div>
              <div class="h-44 bg-gradient-to-br from-zinc-100 to-zinc-200 rounded-xl mb-4 border border-zinc-200/80 p-3 flex flex-col justify-between overflow-hidden shadow-inner">
                <div class="w-2/5 h-2.5 bg-zinc-600 rounded-sm mb-2"></div>
                <div class="space-y-1.5 opacity-60">
                  <div class="w-full h-1.5 bg-zinc-400 rounded-sm"></div>
                  <div class="w-4/5 h-1.5 bg-zinc-300 rounded-sm"></div>
                </div>
                <div class="space-y-1 opacity-60">
                  <div class="w-full h-1.5 bg-zinc-400 rounded-sm"></div>
                  <div class="w-3/4 h-1.5 bg-zinc-300 rounded-sm"></div>
                </div>
              </div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-bold text-zinc-950 text-base">Stanford</h4>
                <span class="text-[10px] font-bold text-zinc-700 bg-zinc-100 px-2 py-0.5 rounded-md">Innovación</span>
              </div>
              <p class="text-xs text-zinc-500 leading-relaxed">
                Diseño contemporáneo ideal para startups, agencias digitales, producto y perfiles creativos técnicos.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <section id="faq" class="py-20 sm:py-28 bg-white border-t border-zinc-200/80">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="max-w-2xl text-left sm:text-center sm:mx-auto mb-16">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zinc-100 text-zinc-800 text-xs font-semibold uppercase tracking-wider mb-4">
            Resolviendo Dudas
          </div>
          <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-zinc-950">
            Preguntas Frecuentes
          </h2>
          <p class="mt-4 text-base text-zinc-600">
            Todo lo que necesitas saber sobre BuildCV y el proceso de optimización.
          </p>
        </div>

        <div class="space-y-4">
          
          <div class="border border-zinc-200 rounded-2xl p-5 sm:p-6 transition-colors bg-zinc-50/50">
            <button 
              @click="toggleFaq(0)" 
              class="w-full flex items-center justify-between text-left font-bold text-base sm:text-lg text-zinc-950 focus:outline-none"
            >
              <span>¿Es BuildCV completamente gratuito?</span>
              <span class="ml-4 p-1 rounded-lg bg-zinc-200/70 text-zinc-700">
                <svg :class="['w-4 h-4 transition-transform duration-200', activeFaq === 0 ? 'rotate-180' : '']" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </button>
            <div v-show="activeFaq === 0" class="mt-4 text-sm text-zinc-600 leading-relaxed pt-2 border-t border-zinc-200/60">
              Sí, puedes crear tu cuenta de forma gratuita, subir tu CV base, procesar tu documento y descargar tus currículums optimizados en formato PDF sin coste ni marcas de agua.
            </div>
          </div>

          <div class="border border-zinc-200 rounded-2xl p-5 sm:p-6 transition-colors bg-zinc-50/50">
            <button 
              @click="toggleFaq(1)" 
              class="w-full flex items-center justify-between text-left font-bold text-base sm:text-lg text-zinc-950 focus:outline-none"
            >
              <span>¿Qué es un sistema ATS y por qué es tan importante?</span>
              <span class="ml-4 p-1 rounded-lg bg-zinc-200/70 text-zinc-700">
                <svg :class="['w-4 h-4 transition-transform duration-200', activeFaq === 1 ? 'rotate-180' : '']" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </button>
            <div v-show="activeFaq === 1" class="mt-4 text-sm text-zinc-600 leading-relaxed pt-2 border-t border-zinc-200/60">
              Un ATS (Applicant Tracking System) es el software que usan más del 90% de empresas medianas y grandes para filtrar postulaciones automáticamente. Si tu CV no contiene las palabras clave requeridas o tiene un formato complejo, es descartado antes de que un reclutador lo vea. BuildCV asegura que tu currículum sea 100% legible y relevante para estos sistemas.
            </div>
          </div>

          <div class="border border-zinc-200 rounded-2xl p-5 sm:p-6 transition-colors bg-zinc-50/50">
            <button 
              @click="toggleFaq(2)" 
              class="w-full flex items-center justify-between text-left font-bold text-base sm:text-lg text-zinc-950 focus:outline-none"
            >
              <span>¿La IA inventa experiencia que no tengo?</span>
              <span class="ml-4 p-1 rounded-lg bg-zinc-200/70 text-zinc-700">
                <svg :class="['w-4 h-4 transition-transform duration-200', activeFaq === 2 ? 'rotate-180' : '']" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </button>
            <div v-show="activeFaq === 2" class="mt-4 text-sm text-zinc-600 leading-relaxed pt-2 border-t border-zinc-200/60">
              No. Nuestro modelo está calibrado para actuar como un asesor experto de carrera: toma tu trayectoria auténtica y la reformula con verbos de impacto, métricas claras y palabras clave alineadas a la oferta laboral. Además, tienes un editor en tiempo real donde puedes revisar y ajustar cada palabra antes de descargar.
            </div>
          </div>

          <div class="border border-zinc-200 rounded-2xl p-5 sm:p-6 transition-colors bg-zinc-50/50">
            <button 
              @click="toggleFaq(3)" 
              class="w-full flex items-center justify-between text-left font-bold text-base sm:text-lg text-zinc-950 focus:outline-none"
            >
              <span>¿Puedo guardar varios CVs para diferentes tipos de empleo?</span>
              <span class="ml-4 p-1 rounded-lg bg-zinc-200/70 text-zinc-700">
                <svg :class="['w-4 h-4 transition-transform duration-200', activeFaq === 3 ? 'rotate-180' : '']" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </button>
            <div v-show="activeFaq === 3" class="mt-4 text-sm text-zinc-600 leading-relaxed pt-2 border-t border-zinc-200/60">
              ¡Totalmente! En tu panel de control puedes guardar tantas versiones como desees (por ejemplo: "CV Frontend", "CV Fullstack", "CV Fintech"), renombrarlas y volver a editarlas o descargarlas cuando las necesites.
            </div>
          </div>

        </div>

      </div>
    </section>

    <section class="py-20 sm:py-28 bg-[#FAFAFA] relative overflow-hidden">
      <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[500px] h-[300px] bg-[#89CFF0]/20 rounded-full blur-3xl pointer-events-none -z-10"></div>

      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-gradient-to-b from-zinc-900 to-zinc-950 border border-zinc-800 rounded-3xl p-8 sm:p-14 text-center text-white relative shadow-2xl overflow-hidden">
          
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/10 border border-white/10 text-xs font-semibold text-zinc-200 mb-6">
            <span class="w-2 h-2 rounded-full bg-[#89CFF0]"></span>
            Comienza en menos de 1 minuto
          </div>

          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-white max-w-2xl mx-auto">
            Tu próximo trabajo empieza con un CV adaptado.
          </h2>

          <p class="mt-4 text-base sm:text-lg text-zinc-400 max-w-xl mx-auto">
            Únete a cientos de profesionales que ya han optimizado su currículum para superar los filtros ATS y conseguir más entrevistas.
          </p>

          <div class="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
            <button 
              @click="irALogin" 
              class="w-full sm:w-auto px-8 py-4 rounded-xl font-bold text-white bg-[#89CFF0] hover:bg-[#78bee0] transition-all shadow-lg shadow-[#89CFF0]/30 active:scale-[0.98]"
            >
              Comenzar a optimizar gratis
            </button>
          </div>

          <p class="mt-4 text-xs text-zinc-500">
            Sin tarjeta de crédito · Exportación en PDF directo · 100% Privado
          </p>
        </div>
      </div>
    </section>

    <footer class="bg-white border-t border-zinc-200 py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-2">
            <span class="w-7 h-7 rounded-lg bg-[#89CFF0]/20 flex items-center justify-center text-[#89CFF0] font-bold text-sm border border-[#89CFF0]/40">
              B
            </span>
            <span class="text-xl font-black text-zinc-900 tracking-tight">Build<span class="text-[#89CFF0]">CV</span></span>
          </div>

          <div class="flex flex-wrap justify-center gap-6 text-sm text-zinc-600">
            <a href="#problema" class="hover:text-zinc-950 transition-colors">El Problema</a>
            <a href="#beneficios" class="hover:text-zinc-950 transition-colors">Beneficios</a>
            <a href="#como-funciona" class="hover:text-zinc-950 transition-colors">Cómo Funciona</a>
            <a href="#plantillas" class="hover:text-zinc-950 transition-colors">Plantillas</a>
            <a href="#faq" class="hover:text-zinc-950 transition-colors">FAQ</a>
            <button @click="irALogin" class="hover:text-zinc-950 transition-colors font-medium">Acceso Usuario</button>
          </div>

          <div class="text-xs text-zinc-400">
            &copy; {{ new Date().getFullYear() }} BuildCV. Todos los derechos reservados.
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(6px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>