<script setup>
import { useFavoritesStore } from '@/stores/favorites'
import { useRouter } from 'vue-router'

const favoritesStore = useFavoritesStore()
const router = useRouter()

function openProduct(id) {
    router.push({ name: 'product', params: { id } })
}
</script>

<template>
  <div class="animate-fade-in">
    <h1 class="text-3xl font-bold mb-8">Избранное</h1>

    <!-- Если есть товары -->
    <div v-if="favoritesStore.items.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-5 gap-y-14">
        <div v-for="product in favoritesStore.items" :key="product.id" class="flex flex-col gap-3 group relative">

            <!-- Карточка товара -->
            <div @click="openProduct(product.id)" class="w-full aspect-square bg-white rounded flex items-center justify-center overflow-hidden cursor-pointer">
                <img :src="product.img" class="max-w-full max-h-full object-cover transition duration-500 group-hover:scale-105">
            </div>

            <div class="flex justify-between items-start">
                <div @click="openProduct(product.id)" class="cursor-pointer">
                    <div class="font-bold text-base flex gap-2">
                        {{ product.price }}₽
                        <span v-if="product.oldPrice" class="text-gray-400 font-normal line-through text-sm">{{ product.oldPrice }}₽</span>
                    </div>
                    <div class="text-[15px] text-gray-800 mt-1">{{ product.title }}</div>
                </div>

                <!-- Кнопка удаления (закрашенное сердце) -->
                <button @click="favoritesStore.toggleFavorite(product)" class="hover:opacity-60 transition">
                    <svg class="w-6 h-6 fill-black stroke-black" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                </button>
            </div>
        </div>
    </div>

    <!-- Пустое состояние -->
    <div v-else class="flex flex-col items-center justify-center py-20 text-center bg-white rounded-xl">
        <svg class="w-16 h-16 text-gray-300 mb-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
        <h2 class="text-xl font-bold mb-2">В избранном пока пусто</h2>
        <p class="text-gray-500 mb-6">Добавляйте товары, чтобы не потерять их</p>
        <RouterLink to="/" class="bg-black text-white px-8 py-3 rounded-lg font-bold hover:opacity-90 transition">
            Перейти в каталог
        </RouterLink>
    </div>
  </div>
</template>