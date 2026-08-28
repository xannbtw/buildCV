<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeSection = ref('seccion-1')

const sections = [
  { id: 'seccion-1', title: '1. Información que recopilamos', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
  { id: 'seccion-2', title: '2. Uso de la información', icon: 'M13 10V3L4 14h7v7l9-11h-7z' },
  { id: 'seccion-3', title: '3. Terceros y Procesamiento', icon: 'M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01' },
  { id: 'seccion-4', title: '4. Tus Derechos y Control', icon: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z' }
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
              class="px-3.5 py-1.5 rounded-lg bg-white text-zinc-900 shadow-xs border border-zinc-200/50"
            >
              Política de Privacidad
            </router-link>
            <router-link 
              to="/servicio" 
              class="px-3.5 py-1.5 rounded-lg text-zinc-600 hover:text-zinc-900 transition-colors"
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
              Documento Legal Oficial
            </div>

            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-zinc-950">
              Política de Privacidad
            </h1>
            <p class="mt-3 text-base sm:text-lg text-zinc-600 max-w-2xl leading-relaxed">
              En <span class="font-semibold text-zinc-900">BuildCV</span> protegemos tus datos personales y tu historial profesional con los más altos estándares de cifrado y transparencia.
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
              <span class="font-medium text-zinc-700">~2 minutos</span>
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
                Contenido del Documento
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

            <!-- Transparency highlight card -->
            <div class="bg-gradient-to-br from-zinc-900 to-zinc-950 text-white rounded-2xl p-5 border border-zinc-800 shadow-md">
              <div class="flex items-center gap-2 mb-2">
                <div class="w-6 h-6 rounded-md bg-[#89CFF0]/20 text-[#89CFF0] flex items-center justify-center font-bold text-xs">
                  🛡️
                </div>
                <span class="text-xs font-bold tracking-tight text-zinc-200">Garantía de Privacidad</span>
              </div>
              <p class="text-xs text-zinc-400 leading-relaxed">
                Tus currículums no son compartidos con reclutadores ni usados para entrenar modelos de IA públicos.
              </p>
              <div class="mt-4 pt-3 border-t border-zinc-800 flex items-center justify-between text-xs">
                <span class="text-zinc-400">¿Dudas?</span>
                <a href="mailto:contacto@buildcv.app" class="text-[#89CFF0] font-semibold hover:underline">Soporte Legal</a>
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
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div>
              <h4 class="text-sm font-bold text-zinc-900">Resumen en lenguaje claro</h4>
              <p class="text-xs sm:text-sm text-zinc-600 mt-1 leading-relaxed">
                Esta Política de Privacidad describe cómo <strong>BuildCV</strong> recopila, utiliza y protege los datos personales e historiales laborales de los usuarios que interactúan con nuestra plataforma web.
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
                Información que recopilamos
              </h2>
            </div>

            <p class="text-sm sm:text-base text-zinc-600 leading-relaxed mb-6">
              Para operar nuestro servicio de optimización, recopilamos los siguientes datos:
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <!-- Datos de Cuenta -->
              <div class="bg-zinc-50 border border-zinc-200/90 rounded-2xl p-5 hover:border-zinc-300 transition-colors">
                <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center mb-3">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <h3 class="text-sm font-bold text-zinc-900 mb-1.5">Datos de Cuenta</h3>
                <p class="text-xs text-zinc-600 leading-relaxed">
                  Dirección de correo electrónico, nombre y fotografía de perfil (obtenidos mediante el registro manual o a través del inicio de sesión con Google OAuth).
                </p>
              </div>

              <!-- Datos del Currículum -->
              <div class="bg-zinc-50 border border-zinc-200/90 rounded-2xl p-5 hover:border-zinc-300 transition-colors">
                <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center mb-3">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <h3 class="text-sm font-bold text-zinc-900 mb-1.5">Datos del Currículum</h3>
                <p class="text-xs text-zinc-600 leading-relaxed">
                  Historial laboral, formación académica, datos de contacto y cualquier texto proporcionado dentro de los documentos PDF subidos o ingresados manualmente en nuestro editor.
                </p>
              </div>
            </div>
          </section>

          <!-- Section 2 -->
          <section id="seccion-2" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                2
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Uso de la información
              </h2>
            </div>

            <p class="text-sm sm:text-base text-zinc-600 leading-relaxed mb-6">
              Utilizamos tus datos personales exclusivamente para los siguientes fines legítimos:
            </p>

            <ul class="space-y-3.5">
              <li class="flex items-start gap-3 p-4 rounded-2xl bg-zinc-50 border border-zinc-200/80">
                <div class="mt-0.5 w-5 h-5 rounded-full bg-[#89CFF0]/20 text-[#89CFF0] flex items-center justify-center shrink-0">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <span class="text-xs sm:text-sm text-zinc-700 font-medium leading-relaxed">
                  Proveer, mantener y mejorar el servicio continuo de optimización de CVs.
                </span>
              </li>

              <li class="flex items-start gap-3 p-4 rounded-2xl bg-zinc-50 border border-zinc-200/80">
                <div class="mt-0.5 w-5 h-5 rounded-full bg-[#89CFF0]/20 text-[#89CFF0] flex items-center justify-center shrink-0">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <span class="text-xs sm:text-sm text-zinc-700 font-medium leading-relaxed">
                  Autenticar tu acceso seguro a la plataforma y mantener tu sesión activa de manera protegida.
                </span>
              </li>

              <li class="flex items-start gap-3 p-4 rounded-2xl bg-zinc-50 border border-zinc-200/80">
                <div class="mt-0.5 w-5 h-5 rounded-full bg-[#89CFF0]/20 text-[#89CFF0] flex items-center justify-center shrink-0">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <span class="text-xs sm:text-sm text-zinc-700 font-medium leading-relaxed">
                  Procesar tus textos mediante Inteligencia Artificial para generar versiones adaptadas a ofertas laborales específicas según tus instrucciones.
                </span>
              </li>
            </ul>
          </section>

          <!-- Section 3 -->
          <section id="seccion-3" class="bg-white border border-zinc-200 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-28">
            <div class="flex items-center gap-3 mb-6">
              <span class="w-9 h-9 rounded-xl bg-zinc-100 text-zinc-800 font-bold flex items-center justify-center text-sm border border-zinc-200">
                3
              </span>
              <h2 class="text-xl sm:text-2xl font-black text-zinc-950 tracking-tight">
                Terceros y Procesamiento de Datos
              </h2>
            </div>

            <p class="text-sm sm:text-base text-zinc-600 leading-relaxed mb-6">
              Para que la plataforma funcione, compartimos datos estrictamente necesarios con los siguientes proveedores de infraestructura de clase mundial:
            </p>

            <div class="space-y-4">
              <!-- Google Cloud -->
              <div class="border border-zinc-200 rounded-2xl p-5 bg-gradient-to-br from-zinc-50 to-white hover:border-[#89CFF0]/50 transition-colors">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-blue-50 border border-blue-100 flex items-center justify-center font-bold text-blue-600">
                      <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM19 18H6c-2.21 0-4-1.79-4-4 0-2.05 1.53-3.76 3.56-3.97l1.07-.11.5-.95C8.08 7.14 9.94 6 12 6c2.62 0 4.88 1.86 5.39 4.43l.3 1.5 1.53.11c1.56.1 2.78 1.41 2.78 2.96 0 1.65-1.35 3-3 3z"/>
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-sm sm:text-base font-bold text-zinc-950">Google Cloud (API de Gemini)</h3>
                      <span class="text-xs text-zinc-500 font-medium">Motor de Inteligencia Artificial</span>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 text-2xs font-bold border border-emerald-200">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> API Segura
                  </span>
                </div>
                <p class="mt-3 text-xs sm:text-sm text-zinc-600 leading-relaxed">
                  Utilizamos esta API para procesar y optimizar los textos de tu currículum. 
                </p>
                <!-- Key Privacy Highlight -->
                <div class="mt-3 p-3 rounded-xl bg-emerald-50/60 border border-emerald-200/80 text-xs text-emerald-900 flex items-start gap-2">
                  <span class="font-bold shrink-0">🔒 Cláusula de no entrenamiento:</span>
                  <span>Google <strong>no utiliza</strong> los datos enviados a través de su API comercial para entrenar ni mejorar sus modelos de IA públicos.</span>
                </div>
              </div>

              <!-- Supabase -->
              <div class="border border-zinc-200 rounded-2xl p-5 bg-gradient-to-br from-zinc-50 to-white hover:border-[#89CFF0]/50 transition-colors">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-emerald-50 border border-emerald-100 flex items-center justify-center font-bold text-emerald-600">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2 1 3 3 3h10c2 0 3-1 3-3V7c0-2-1-3-3-3H7C5 4 4 5 4 7zM9 12h6m-6-4h6m-6 8h4" />
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-sm sm:text-base font-bold text-zinc-950">Supabase</h3>
                      <span class="text-xs text-zinc-500 font-medium">Base de datos y Autenticación Cifrada</span>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-50 text-blue-700 text-2xs font-bold border border-blue-200">
                    Cifrado en reposo
                  </span>
                </div>
                <p class="mt-3 text-xs sm:text-sm text-zinc-600 leading-relaxed">
                  Gestiona nuestra base de datos relacional y la autenticación cifrada de usuarios con políticas de seguridad a nivel de fila (Row Level Security).
                </p>
              </div>

              <!-- Vercel y Railway -->
              <div class="border border-zinc-200 rounded-2xl p-5 bg-gradient-to-br from-zinc-50 to-white hover:border-[#89CFF0]/50 transition-colors">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-purple-50 border border-purple-100 flex items-center justify-center font-bold text-purple-600">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2" />
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-sm sm:text-base font-bold text-zinc-950">Vercel y Railway</h3>
                      <span class="text-xs text-zinc-500 font-medium">Infraestructura y Alojamiento Cloud</span>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-purple-50 text-purple-700 text-2xs font-bold border border-purple-200">
                    Certificación SSL
                  </span>
                </div>
                <p class="mt-3 text-xs sm:text-sm text-zinc-600 leading-relaxed">
                  Proveen el alojamiento de nuestra plataforma web y los servidores de procesamiento con alta disponibilidad y transferencia segura HTTPS/TLS.
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
                Tus Derechos y Control de Datos
              </h2>
            </div>

            <div class="bg-zinc-50 border border-zinc-200/80 rounded-2xl p-5 mb-6">
              <div class="flex items-center gap-2 mb-2">
                <span class="text-base">🇨🇱</span>
                <h3 class="text-sm font-bold text-zinc-900">Legislación de Protección de Datos de Chile (Ley 19.628)</h3>
              </div>
              <p class="text-xs sm:text-sm text-zinc-600 leading-relaxed">
                De acuerdo con la legislación de protección de datos de Chile (Ley 19.628), tienes derecho a <strong>acceder, rectificar, cancelar u oponerte</strong> al tratamiento de tus datos personales en cualquier momento.
              </p>
            </div>

            <!-- Self-service deletion notice -->
            <div class="border border-zinc-200 rounded-2xl p-5 bg-white space-y-3">
              <div class="flex items-center gap-2.5 text-zinc-900 font-bold text-sm">
                <div class="w-6 h-6 rounded-lg bg-rose-50 text-rose-600 flex items-center justify-center">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </div>
                <span>Eliminación definitiva y permanente</span>
              </div>
              <p class="text-xs sm:text-sm text-zinc-600 leading-relaxed">
                Puedes eliminar tu cuenta y todos los currículums asociados de forma permanente y sin demoras directamente desde la configuración de tu cuenta en la plataforma. Una vez confirmada la eliminación, tus datos son purgados irreversiblemente de nuestras bases de datos.
              </p>
            </div>
          </section>

          <!-- Bottom Banner CTA -->
          <div class="bg-gradient-to-r from-zinc-900 to-zinc-950 border border-zinc-800 rounded-3xl p-6 sm:p-8 text-white flex flex-col sm:flex-row items-center justify-between gap-6 shadow-xl">
            <div>
              <h3 class="text-lg sm:text-xl font-bold tracking-tight">
                ¿Tienes preguntas adicionales?
              </h3>
              <p class="text-xs sm:text-sm text-zinc-400 mt-1 max-w-md">
                Nuestro equipo está disponible para responder cualquier inquietud sobre la privacidad y seguridad de tus datos.
              </p>
            </div>
            <div class="flex items-center gap-3 shrink-0 w-full sm:w-auto">
              <router-link
                to="/servicio"
                class="w-full sm:w-auto text-center px-4 py-2.5 rounded-xl text-xs font-semibold text-zinc-300 bg-white/10 hover:bg-white/20 transition-colors"
              >
                Ver Términos
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
            <router-link to="/privacidad" class="text-zinc-950 font-semibold transition-colors">Política de Privacidad</router-link>
            <router-link to="/servicio" class="hover:text-zinc-950 transition-colors">Términos de Servicio</router-link>
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
