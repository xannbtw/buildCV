<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from './supabase'
import { currentUser } from './store'

const router = useRouter()

onMounted(async () => {
  const { data: { session } } = await supabase.auth.getSession()

  if (session) {
    currentUser.value = session.user
  }
  
  supabase.auth.onAuthStateChange((event, session) => {
    currentUser.value = session?.user || null

    if (event === 'SIGNED_IN') {
      router.push('/dashboard')
    }
  })
})
</script>

<template>
  <router-view></router-view>
</template>