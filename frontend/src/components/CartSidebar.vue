<script setup>
import { useCartStore } from '@/stores/cart'
import { useRouter } from 'vue-router'

const cartStore = useCartStore()
const router = useRouter()

function goToCheckout() {
    cartStore.toggleCart()
    router.push('/checkout')
}
</script>

<template>
    <transition enter-active-class="transition transform duration-300" enter-from-class="translate-x-full" enter-to-class="translate-x-0" leave-active-class="transition transform duration-300" leave-from-class="translate-x-0" leave-to-class="translate-x-full">
        <div v-if="cartStore.isOpen" class="fixed top-0 right-0 h-full w-[380px] max-w-full bg-white z-50 p-6 shadow-2xl flex flex-col">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-xl font-bold">Корзина</h2>
                <button @click="cartStore.toggleCart" class="text-2xl text-gray-400 hover:text-black">✕</button>
            </div>

            <div class="flex-1 overflow-y-auto no-scrollbar">
                <div v-for="(item, index) in cartStore.items" :key="index" class="flex gap-4 border-b border-gray-100 py-4 last:border-0 relative">
                    <img :src="item.img" class="w-[70px] h-[70px] object-contain border border-gray-100 rounded">
                    <div class="flex-1 flex flex-col justify-center">
                        <div class="font-bold text-sm">{{ item.title }}</div>
                        <div class="font-bold mt-1">{{ item.price }}₽</div>
                    </div>
                    <button @click="cartStore.removeFromCart(index)" class="absolute right-0 top-1/2 -translate-y-1/2 w-8 h-8 flex items-center justify-center border border-gray-300 rounded hover:bg-red-50">🗑️</button>
                </div>
            </div>

            <div class="border-t border-gray-100 pt-5 mt-auto">
                <div class="flex justify-between items-center mb-3">
                    <span class="text-sm text-gray-500">Ваша корзина</span>
                    <span class="font-bold text-lg">{{ cartStore.total }}₽</span>
                </div>
                <button @click="goToCheckout" class="w-full bg-black text-white font-bold py-3.5 rounded-lg hover:opacity-90">Далее</button>
            </div>
        </div>
    </transition>
</template>