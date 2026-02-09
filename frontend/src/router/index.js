import { createRouter, createWebHistory } from 'vue-router'
import CatalogView from '../views/CatalogView.vue'
import ProductView from '../views/ProductView.vue'
import CheckoutView from '../views/CheckoutView.vue'
import ProfileView from '../views/ProfileView.vue'
import BrandsView from '../views/BrandsView.vue'
import FavoritesView from '../views/FavoritesView.vue' // <--- Импорт

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'catalog', component: CatalogView },
    { path: '/product/:id', name: 'product', component: ProductView, props: true },
    { path: '/checkout', name: 'checkout', component: CheckoutView },
    { path: '/profile', name: 'profile', component: ProfileView },
    { path: '/brands', name: 'brands', component: BrandsView },
    { path: '/favorites', name: 'favorites', component: FavoritesView }, // <--- Маршрут
  ],
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router