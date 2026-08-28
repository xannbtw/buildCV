import { createRouter, createWebHistory } from 'vue-router'

// Importamos las vistas
import LandingView from '../views/LandingView.vue'
import LoginView from '../views/AuthView.vue'
import DashboardView from '../views/DashboardView.vue'
import PrivacidadView from '../views/privacidad.vue'
import ServicioView from '../views/servicio.vue'
import { supabase } from '../supabase'


const router = createRouter({
  history: createWebHistory(),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    }
    return { top: 0, behavior: 'smooth' }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/privacidad',
      name: 'privacidad',
      component: PrivacidadView
    },
    {
      path: '/servicio',
      name: 'servicio',
      component: ServicioView,
      alias: ['/terminos', '/terminos-servicio']
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  // Verificamos la sesión actual en Supabase
  const { data: { session } } = await supabase.auth.getSession()

  // Si intenta ir al dashboard y NO hay sesión, lo pateamos al login
  if (to.path === '/dashboard' && !session) {
    next('/login')
  }
  // Si intenta ir al login pero YA tiene sesión, lo mandamos al dashboard
  else if (to.path === '/login' && session) {
    next('/dashboard')
  }
  // En cualquier otro caso (como la landing page), lo dejamos pasar normal
  else {
    next()
  }
})
export default router