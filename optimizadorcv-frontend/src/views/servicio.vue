<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeSection = ref('seccion-1')

const sections = [
  { id: 'seccion-1', title: '1. Descripción del Servicio', icon: 'M13 10V3L4 14h7v7l9-11h-7z' },
  { id: 'seccion-2', title: '2. Uso Aceptable y Responsabilidad', icon: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z' },
  { id: 'seccion-3', title: '3. Naturaleza de la IA', icon: 'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z' },
  { id: 'seccion-4', title: '4. Propiedad y Licencia', icon: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z' },
  { id: 'seccion-5', title: '5. Limitación de Responsabilidad', icon: 'M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z' },
  { id: 'seccion-6', title: '6. Ley Aplicable', icon: 'M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3' }
]

const scrollToSection = (id: string) => {
  activeSection.value = id
  const element = document.getElementById(id)
  if (element) {
    const yOffset = -100
    const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset
    window.scrollTo({ top: y, behavior: 'smooth' })
  }
}

const printDocument = () => {
  window.print()
}

const irALogin = () => {
  router.push('/login')
}
</script>

<template>
  <div class="min-h-screen bg-[#FAFAFA] text-zinc-900 font-sans selection:bg-[#89CFF0]/30 selection:text-zinc-900 flex flex-col">
    <!-- Navbar -->
    <header class="sticky top-0 left-0 w-full z-50 bg-white/85 backdrop-blur-md border-b border-zinc-200/80 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 sm:h-20">
          
          <!-- Logo & Back Button -->
          <div class="flex items-center gap-4 sm:gap-6">
            <router-link to="/" class="text-2xl font-black tracking-tight text-zinc-900 flex items-center gap-1 group">
              <span>Build<span class="text-[#89CFF0]">CV</span></span>
            </router-link>

            <div class="h-5 w-[1px] bg-zinc-200 hidden sm:block"></div>

            <router-link 
              to="/" 
              class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-medium text-zinc-600 hover:text-zinc-950 transition-colors group"
            >
              <svg class="w-4 h-4 text-zinc-400 group-hover:-translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
              <span>Volver a inicio</span>
            </router-link>
          </div>

          <!-- Document Navigation Switcher -->
          <div class="hidden md:flex items-center bg-zinc-100/90 p-1 rounded-xl border border-zinc-200/70 text-xs font-semibold">
            <router-link 
              to="/privacidad" 
              class="px-3.5 py-1.5 rounded-lg text-zinc-600 hover:text-zinc-900 transition-colors"
            >
              Política de Privacidad
            </router-link>
            <router-link 
              to="/servicio" 
              class="px-3.5 py-1.5 rounded-lg bg-white text-zinc-900 shadow-xs border border-zinc-200/50"
            >
              Términos de Servicio
            </router-link>
          </div>

          <!-- Actions -->
          <div class="flex items-center gap-2 sm:gap-3">
            <button 
              @click="printDocument" 
              type="button" 
              class="hidden sm:inline-flex items-center gap-1.5 px-3 py-2 text-xs font-semibold text-zinc-700 bg-white hover:bg-zinc-100 border border-zinc-200 rounded-xl transition-all shadow-2xs"
              title="Imprimir documento"
            >
              <svg class="w-3.5 h-3.5 text-zinc-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
              </svg>
              <span>Imprimir</span>
            </button>
            <button 
              @click="irALogin" 
              class="inline-flex items-center justify-center px-4 py-2 text-xs sm:text-sm font-semibold rounded-xl text-white bg-[#89CFF0] hover:bg-[#78bee0] active:scale-[0.98] transition-all shadow-sm shadow-[#89CFF0]/40"
            >
              Acceso Usuario
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- Hero Header -->
    <section class="relative bg-gradient-to-b from-white via-white to-[#FAFAFA] border-b border-zinc-200/70 pt-12 pb-14 sm:pb-16 overflow-hidden">
      <!-- Glow ambient light -->
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[700px] h-[300px] bg-[#89CFF0]/15 rounded-full blur-3xl pointer-events-none -z-10"></div>

      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div>
            <!-- Badge -->
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#89CFF0]/15 border border-[#89CFF0]/40 text-xs font-semibold text-zinc-800 mb-4">
              <span class="w-2 h-2 rounded-full bg-[#89CFF0] animate-pulse"></span>
              Acuerdo de Uso y Términos Legales
            </div>

            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-zinc-950">
              Términos y Condiciones de Servicio
            </h1>
            <p class="mt-3 text-base sm:text-lg text-zinc-600 max-w-2xl leading-relaxed">
              Bienvenido a <span class="font-semibold text-zinc-900">BuildCV</span>. Al acceder o utilizar nuestra plataforma, aceptas cumplir con los siguientes términos y condiciones.
            </p>
          </div>

          <!-- Metadata card -->
          <div class="bg-zinc-50 border border-zinc-200/80 rounded-2xl p-4 sm:p-5 flex flex-col gap-2.5 text-xs text-zinc-600 sm:w-64 self-stretch sm:self-auto">
            <div class="flex items-center justify-between">
              <span class="text-zinc-500">Última actualización:</span>
              <span class="font-bold text-zinc-900">28 de agosto, 2026</span>
            </div>
            <div class="h-[1px] bg-zinc-200/70"></div>
            <div class="flex items-center justify-between">
              <span class="text-zinc-500">Tiempo de lectura:</span>
              <span class="font-medium text-zinc-700">~2.5 minutos</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Main Content Container -->
    <main class="flex-1 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-16 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
        
        <!-- Sticky Sidebar Navigation (Desktop) -->
        <aside class="hidden lg:block lg:col-span-4">
          <div class="sticky top-28 space-y-4">
            <div class="bg-white border border-zinc-200 rounded-2xl p-4 shadow-xs">
              <h3 class="text-xs font-bold uppercase tracking-wider text-zinc-400 px-3 mb-3">
                Secciones del Acuerdo
              </h3>
              <nav class="space-y-1">
                <button
                  v-for="section in sections"
                  :key="section.id"
                  @click="scrollToSection(section.id)"
                  :class="[
                    'w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-left text-xs font-semibold transition-all duration-150',
                    activeSection === section.id
                      ? 'bg-[#89CFF0]/20 text-zinc-950 font-bold border border-[#89CFF0]/40'
                      : 'text-zinc-600 hover:text-zinc-900 hover:bg-zinc-100/70'
                  ]"
                >
                  <svg class="w-4 h-4 text-zinc-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="section.icon" />
                  </svg>
                  <span class="truncate">{{ section.title }}</span>
                </button>
              </nav>
            </div>

            <!-- Ownership guarantee card -->
            <div class="bg-gradient-to-br from-zinc-900 to-zinc-950 text-white rounded-2xl p-5 border border-zinc-800 shadow-md">
              <div class="flex items-center gap-2 mb-2">
                <div class="w-6 h-6 rounded-md bg-[#89CFF0]/20 text-[#89CFF0] flex items-center justify-center font-bold text-xs">
                  ✨
                </div>
                <span class="text-xs font-bold tracking-tight text-zinc-200">Tu Información es Tuya</span>
              </div>
              <p class="text-xs text-zinc-400 leading-relaxed">
                Tú mantienes el 100% de la propiedad intelectual de tus currículums y datos profesionales creados en la plataforma.
              </p>
              <div class="mt-4 pt-3 border-t border-zinc-800 flex items-center justify-between text-xs">
                <span class="text-zinc-400">¿Consultas?</span>
                <a href="mailto:contacto@buildcv.app" class="text-[#89CFF0] font-semibold hover:underline">Contacto Legal</a>
              </div>
            </div>
          </div>
        </aside>

        <!-- Document Body -->
        <div class="lg:col-span-8 space-y-10">
          
          <!-- Introduction Notice -->
          <div class="bg-[#89CFF0]/10 border border-[#89CFF0]/30 rounded-2xl p-5 flex items-start gap-4">
            <div class="p-2 bg-white rounded-xl text-[#89CFF0] shrink-0 border border-[#89CFF0]/30 shadow-2xs">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <div>
              <h4 class="text-sm font-bold text-zinc-900">Términos Clave y Compromiso</h4>
              <p class="text-xs sm:text-sm text-zinc-600 mt-1 leading-relaxed">
                Estos términos rigen el uso del software y las herramientas de optimización con Inteligencia Artificial provistas por <strong>BuildCV</strong>.
              </p>
            </div>
          </div>

          <!-- Section 1 -->
          <section id="seccion-1" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                1
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Descripción del Servicio
              </h2>
            </div>

            <div class="p-5 rounded-2xl bg-zinc-50 border border-zinc-200/80">
              <p class="text-sm sm:text-base text-zinc-700 leading-relaxed font-normal">
                <strong>BuildCV</strong> es una plataforma de software como servicio (SaaS) que proporciona herramientas basadas en Inteligencia Artificial para estructurar, redactar y optimizar currículums vitae.
              </p>
            </div>
          </section>

          <!-- Section 2 -->
          <section id="seccion-2" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                2
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Uso Aceptable y Responsabilidad
              </h2>
            </div>

            <p class="text-sm sm:text-base text-zinc-600 leading-relaxed mb-6">
              El usuario es el único responsable de la veracidad, exactitud y legalidad de la información ingresada.
            </p>

            <div class="bg-rose-50/60 border border-rose-200/80 rounded-2xl p-5 mb-4">
              <div class="flex items-center gap-2 mb-2 text-rose-900 font-bold text-sm">
                <svg class="w-4 h-4 text-rose-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                </svg>
                <span>Conductas Estrictamente Prohibidas</span>
              </div>
              <p class="text-xs sm:text-sm text-rose-800 leading-relaxed">
                Queda estrictamente prohibido utilizar la plataforma para generar historiales laborales falsos, suplantar la identidad de terceros o abusar de los límites de peticiones del servidor.
              </p>
            </div>
          </section>

          <!-- Section 3 -->
          <section id="seccion-3" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                3
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Naturaleza de la Inteligencia Artificial
              </h2>
            </div>

            <p class="text-sm sm:text-base text-zinc-600 leading-relaxed mb-6">
              Los textos generados por BuildCV son procesados por modelos de lenguaje de Inteligencia Artificial de terceros.
            </p>

            <div class="space-y-4">
              <div class="p-5 rounded-2xl bg-amber-50/60 border border-amber-200/80">
                <div class="flex items-center gap-2 mb-2 text-amber-900 font-bold text-sm">
                  <svg class="w-4 h-4 text-amber-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                  <span>Revisión Obligatoria por parte del Usuario</span>
                </div>
                <p class="text-xs sm:text-sm text-amber-900 leading-relaxed">
                  Aunque la herramienta está diseñada para optimizar la redacción, el usuario acepta que debe revisar, editar y validar siempre el currículum final antes de descargarlo o enviarlo a un empleador.
                </p>
              </div>

              <div class="p-5 rounded-2xl bg-zinc-50 border border-zinc-200/80">
                <p class="text-xs sm:text-sm text-zinc-600 leading-relaxed">
                  BuildCV no garantiza entrevistas, contrataciones ni la precisión absoluta de los textos generados.
                </p>
              </div>
            </div>
          </section>

          <!-- Section 4 -->
          <section id="seccion-4" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                4
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Propiedad y Licencia
              </h2>
            </div>

            <div class="p-6 rounded-2xl bg-emerald-50/50 border border-emerald-200/80 space-y-3">
              <div class="flex items-center gap-2.5 text-emerald-950 font-bold text-sm">
                <svg class="w-5 h-5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
                <span>Propiedad Intelectual del Usuario</span>
              </div>
              <p class="text-xs sm:text-sm text-emerald-900 leading-relaxed">
                El usuario mantiene todos los derechos de propiedad intelectual sobre los datos personales y el contenido de los currículums que suba a la plataforma. BuildCV no reclama la propiedad de tus documentos profesionales.
              </p>
            </div>
          </section>

          <!-- Section 5 -->
          <section id="seccion-5" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                5
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Limitación de Responsabilidad
              </h2>
            </div>

            <div class="space-y-4">
              <p class="text-sm sm:text-base text-zinc-600 leading-relaxed">
                El servicio se proporciona <strong>"tal cual"</strong> y <strong>"según disponibilidad"</strong>.
              </p>

              <div class="p-5 rounded-2xl bg-zinc-50 border border-zinc-200/80">
                <p class="text-xs sm:text-sm text-zinc-600 leading-relaxed">
                  BuildCV no asume responsabilidad por interrupciones del servicio derivadas de fallos en proveedores externos (Supabase, Railway, Vercel), pérdida accidental de datos, o los resultados de procesos de selección laboral en los que el usuario participe utilizando documentos generados en la plataforma.
                </p>
              </div>
            </div>
          </section>

          <!-- Section 6 -->
          <section id="seccion-6" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                6
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Ley Aplicable
              </h2>
            </div>

            <div class="p-5 rounded-2xl bg-zinc-50 border border-zinc-200/80 flex items-start gap-3">
              <span class="text-xl">🇨🇱</span>
              <p class="text-xs sm:text-sm text-zinc-700 leading-relaxed font-medium">
                Estos términos se rigen e interpretan de acuerdo con las leyes de la República de Chile. Cualquier controversia será sometida a los tribunales ordinarios de justicia competentes.
              </p>
            </div>
          </section>

          <!-- Bottom Banner CTA -->
          <div class="bg-gradient-to-r from-zinc-900 to-zinc-950 border border-zinc-800 rounded-3xl p-6 sm:p-8 text-white flex flex-col sm:flex-row items-center justify-between gap-6 shadow-xl">
            <div>
              <h3 class="text-lg sm:text-xl font-bold tracking-tight">
                Empieza a optimizar tu CV hoy
              </h3>
              <p class="text-xs sm:text-sm text-zinc-400 mt-1 max-w-md">
                Únete de forma gratuita y crea currículums adaptados a cualquier postulación.
              </p>
            </div>
            <div class="flex items-center gap-3 shrink-0 w-full sm:w-auto">
              <router-link
                to="/privacidad"
                class="w-full sm:w-auto text-center px-4 py-2.5 rounded-xl text-xs font-semibold text-zinc-300 bg-white/10 hover:bg-white/20 transition-colors"
              >
                Ver Privacidad
              </router-link>
              <button
                @click="irALogin"
                class="w-full sm:w-auto px-5 py-2.5 rounded-xl text-xs font-bold text-white bg-[#89CFF0] hover:bg-[#78bee0] transition-colors shadow-sm shadow-[#89CFF0]/40"
              >
                Comenzar Gratis
              </button>
            </div>
          </div>

        </div>

      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-zinc-200 py-10 mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-2">
            <span class="w-7 h-7 rounded-lg bg-[#89CFF0]/20 flex items-center justify-center text-[#89CFF0] font-bold text-sm border border-[#89CFF0]/40">
              B
            </span>
            <span class="text-xl font-black text-zinc-900 tracking-tight">Build<span class="text-[#89CFF0]">CV</span></span>
          </div>

          <div class="flex flex-wrap justify-center gap-6 text-sm text-zinc-600">
            <router-link to="/" class="hover:text-zinc-950 transition-colors">Inicio</router-link>
            <router-link to="/privacidad" class="hover:text-zinc-950 transition-colors">Política de Privacidad</router-link>
            <router-link to="/servicio" class="text-zinc-950 font-semibold transition-colors">Términos de Servicio</router-link>
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
@media print {
  header, aside, footer, button, .no-print {
    display: none !important;
  }
  main {
    max-width: 100% !important;
    padding: 0 !important;
  }
}
</style>
