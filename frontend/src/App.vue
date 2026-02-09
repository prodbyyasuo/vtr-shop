<script setup>
import { RouterView } from 'vue-router'
import TheHeader from './components/TheHeader.vue'
import TheFooter from './components/TheFooter.vue'
import CartSidebar from './components/CartSidebar.vue'
import { useCartStore } from './stores/cart'

const cartStore = useCartStore()
</script>

<template>
  <div class="flex flex-col min-h-screen font-sans text-black">
    <TheHeader />

    <main class="flex-1 px-5 md:px-10 py-8 max-w-[1600px] w-full mx-auto">
      <!-- Здесь меняются страницы в зависимости от URL -->
      <RouterView />
    </main>

    <TheFooter />

    <!-- Глобальные модалки -->
    <CartSidebar />

    <!-- Затемнение фона -->
    <div v-if="cartStore.isOpen" @click="cartStore.toggleCart" class="fixed inset-0 bg-black/50 z-40 transition-opacity"></div>
  </div>
</template>