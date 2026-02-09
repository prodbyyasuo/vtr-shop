<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { useProductStore } from '@/stores/products' // <--- Импорт стора товаров

const cartStore = useCartStore()
const productStore = useProductStore()
const router = useRouter()

const isSearchOpen = ref(false)
const searchInput = ref(null)

// Функция переключения поиска
function toggleSearch() {
  isSearchOpen.value = !isSearchOpen.value

  if (isSearchOpen.value) {
    // Если открыли - фокус в поле и переходим в каталог
    setTimeout(() => searchInput.value?.focus(), 100)
    router.push('/')
  } else {
    // Если закрыли - очищаем строку
    productStore.clearSearch()
  }
}
</script>

<template>
  <div class="sticky top-0 z-30 bg-white">
    <header class="flex items-center justify-between px-5 md:px-10 py-5 border-b border-gray-100 relative bg-white z-20">

      <!-- Навигация -->
      <nav class="hidden md:flex gap-8 text-sm font-bold uppercase tracking-wide">
        <RouterLink to="/" class="hover:opacity-60 transition" active-class="opacity-60">Каталог</RouterLink>
        <RouterLink to="/brands" class="hover:opacity-60 transition" active-class="opacity-60">Бренды</RouterLink>
        <a href="#" class="hover:opacity-60 transition">Релизы</a>
        <a href="#" class="hover:opacity-60 transition">Карта</a>
      </nav>

      <!-- Логотип -->
      <RouterLink to="/" class="absolute left-1/2 -translate-x-1/2 flex items-center gap-2 text-xl font-bold hover:opacity-80 transition">
        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="black"><path d="M19 6h-2c0-2.76-2.24-5-5-5S7 3.24 7 6H5C3.9 6 3 6.9 3 8v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-7-3c1.66 0 3 1.34 3 3H9c0-1.66 1.34-3 3-3zm0 10c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/><path d="M12 13.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z" fill="white"/></svg>
        Витрина
      </RouterLink>

      <!-- Иконки -->
      <div class="flex items-center gap-5">
          <!-- Поиск (КЛИКАБЕЛЬНЫЙ) -->
          <svg @click="toggleSearch" class="w-6 h-6 cursor-pointer hover:opacity-60 stroke-black stroke-[1.5] fill-none transition-colors" :class="{'text-blue-600': isSearchOpen}" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>

          <RouterLink to="/profile"><svg class="w-6 h-6 cursor-pointer hover:opacity-60 stroke-black stroke-[1.5] fill-none" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></RouterLink>
          <RouterLink to="/favorites"><svg class="w-6 h-6 cursor-pointer hover:opacity-60 stroke-black stroke-[1.5] fill-none" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></RouterLink>

          <div @click="cartStore.toggleCart" class="relative cursor-pointer hover:opacity-60">
              <svg class="w-6 h-6 stroke-black stroke-[1.5] fill-none" viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
              <div v-if="cartStore.count > 0" class="absolute -top-1 -right-2 bg-red-500 text-white text-[10px] font-bold w-4 h-4 rounded-full flex items-center justify-center">{{ cartStore.count }}</div>
          </div>
      </div>
    </header>

    <!-- ВЫПАДАЮЩАЯ СТРОКА ПОИСКА -->
    <transition enter-active-class="transition duration-200 ease-out" enter-from-class="-translate-y-5 opacity-0" enter-to-class="translate-y-0 opacity-100" leave-active-class="transition duration-150 ease-in" leave-from-class="translate-y-0 opacity-100" leave-to-class="-translate-y-5 opacity-0">
      <div v-if="isSearchOpen" class="absolute top-full left-0 w-full bg-white border-b border-gray-100 px-5 md:px-10 py-4 shadow-sm z-10 flex items-center gap-4">
        <svg class="w-5 h-5 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>

        <!-- Input связан со стором через v-model -->
        <input
          ref="searchInput"
          v-model="productStore.searchQuery"
          type="text"
          placeholder="Поиск по товарам..."
          class="flex-1 outline-none text-base text-gray-800 placeholder-gray-400 h-full bg-transparent"
        >

        <button @click="toggleSearch" class="text-gray-400 hover:text-black transition">✕</button>
      </div>
    </transition>
  </div>
</template>