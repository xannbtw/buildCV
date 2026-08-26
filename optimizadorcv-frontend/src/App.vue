<script setup lang="ts">
import { onMounted } from 'vue'
import { supabase } from './supabase'
import { currentUser } from './store'

onMounted(async () => {
  const { data: { session } } = await supabase.auth.getSession()

  if (session) {
    currentUser.value = session.user
  }
  
  supabase.auth.onAuthStateChange((_event, session) => {
    currentUser.value = session?.user || null
  })
})
</script>

<template>
  <router-view></router-view>
</template>