<script setup lang="ts">
import { cvData } from '../../store'
</script>


<template>
  <div id="cv-preview" class="bg-white p-10 max-w-4xl mx-auto text-black font-serif text-sm shadow-xl min-h-[1056px]">
    
    <header class="text-center mb-6">
      <h1 class="text-4xl font-bold mb-1">{{ cvData.personal?.fullName || 'Tu Nombre' }}</h1>
      <div class="flex flex-wrap justify-center items-center gap-2 text-sm mt-2">
        <span v-if="cvData.personal?.phone">{{cvData.personal?.phone}}</span>
        <span v-if="cvData.personal?.jobTitle">| {{ cvData.personal.jobTitle }} |</span>
        <span v-if="cvData.personal?.email">{{ cvData.personal.email }}</span>
      </div>
    </header>

    <section class="mb-6">
      <h2 class="text-lg font-bold border-b-2 border-black uppercase mb-3 pb-1">RESUMEN PROFESIONAL</h2>
      <div class="mb-4">
        <div class="flex justify-between items-baseline mb-1">
          <div>
            <p class="text-sm text-gray-800">
              {{ cvData.personal?.summary || 'Resumen Profesional...' }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="mb-6">
      <h2 class="text-lg font-bold border-b-2 border-black uppercase mb-3 pb-1">Experiencia Laboral</h2>
      
      <div v-if="!cvData.experience || cvData.experience.length === 0" class="text-gray-400 italic">
        Añade tu experiencia laboral en el panel izquierdo.
      </div>

      <div v-for="(exp, index) in cvData.experience" :key="index" class="mb-4">
        <div class="flex justify-between items-start gap-4 mb-1">
          <div>
            <div class="flex-1">
              <span class="font-bold text-base">{{ exp.company || 'Empresa' }}</span>
              <span class="italic"> — {{ exp.position || 'Cargo' }}</span>
            </div>
          </div>
          <div class="text-right text-sm shrink-0 whitespace-nowrap">
            <span v-if="exp.location">{{ exp.location }}</span>
            <span v-if="exp.location && exp.date"> | </span>
            <span v-if="exp.date">{{ exp.date }}</span>
          </div>
        </div>
        <p class="text-sm whitespace-pre-line text-gray-800 ml-4 list-disc">
          {{ exp.description || 'Descripción de tus responsabilidades y logros...' }}
        </p>
      </div>
    </section>

    <section class="mb-6">
      <h2 class="text-lg font-bold border-b-2 border-black uppercase mb-3 pb-1">Educación</h2>
      
      <div v-if="!cvData.education || cvData.education.length === 0" class="text-gray-400 italic">
        Añade tu educación en el panel izquierdo.
      </div>

      <div v-for="(edu, index) in cvData.education" :key="index" class="mb-3">
        <div class="flex justify-between items-baseline mb-1">
          <div>
            <span class="font-bold text-base">{{ edu.institution || 'Institución' }}</span>
          </div>
          <div class="text-right text-sm">
            <span>{{ edu.date || 'Fecha' }}</span>
          </div>
        </div>
        <p class="text-sm italic text-gray-800">{{ edu.degree || 'Título obtenido' }}</p>
      </div>
    </section>

    <section class="mb-6">
      <h2 class="text-lg font-bold border-b-2 border-black uppercase mb-3 pb-1">Habilidades</h2>

      <div v-if="!cvData.skills || cvData.skills.length === 0" class="text-gray-400 italic">
        Añade tus habilidades en el panel izquierdo.
      </div>

      <div v-for="(skill, index) in cvData.skills" :key="index" class="mb-3">
        <div class="flex justify-between items-baseline mb-1">
          <div>
            <span class="font-bold text-base">{{ skill.name || 'Habilidad' }}</span>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>