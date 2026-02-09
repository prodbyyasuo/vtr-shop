<script setup>
import { useCartStore } from '@/stores/cart'
import { RouterLink } from 'vue-router'

const cartStore = useCartStore()

const handlePayment = () => {
    alert('Переход к оплате...')
}
</script>

<template>
  <div class="animate-fade-in">
    <!-- Хлебные крошки -->
    <RouterLink to="/" class="inline-block mb-6 text-sm text-gray-500 hover:text-black transition-colors">
      ← Вернуться к покупкам
    </RouterLink>

    <h1 class="text-3xl font-bold mb-8">Оформление заказа</h1>

    <div class="grid grid-cols-1 lg:grid-cols-[1.5fr_1fr] gap-10 items-start">

      <!-- ЛЕВАЯ КОЛОНКА: ФОРМЫ -->
      <div class="flex flex-col gap-6">

        <!-- Контактные данные -->
        <div class="bg-white rounded-xl p-6 md:p-8 shadow-sm">
          <h2 class="text-lg font-bold mb-5">Контактные данные</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <input type="text" placeholder="Имя" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition">
            <input type="text" placeholder="Фамилия" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition">
          </div>
          <input type="tel" placeholder="Телефон (+7...)" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition mb-4">
          <input type="email" placeholder="Email для чека" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition">
        </div>

        <!-- Доставка -->
        <div class="bg-white rounded-xl p-6 md:p-8 shadow-sm">
          <h2 class="text-lg font-bold mb-5">Доставка</h2>
          <input type="text" placeholder="Город" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition mb-4">

          <div class="flex flex-col gap-3 mb-4">
            <label class="flex items-center gap-3 text-sm cursor-pointer p-2 rounded hover:bg-gray-50">
              <input type="radio" name="delivery" checked class="accent-black w-4 h-4">
              <span>CDEK (до пункта выдачи)</span>
            </label>
            <label class="flex items-center gap-3 text-sm cursor-pointer p-2 rounded hover:bg-gray-50">
              <input type="radio" name="delivery" class="accent-black w-4 h-4">
              <span>Почта России</span>
            </label>
          </div>

          <input type="text" placeholder="Адрес пункта выдачи или домашний адрес" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition">
        </div>

        <!-- Комментарий -->
        <div class="bg-white rounded-xl p-6 md:p-8 shadow-sm">
          <h2 class="text-lg font-bold mb-5">Комментарий к заказу</h2>
          <input type="text" placeholder="Например, код от домофона" class="w-full bg-[#f2f3f7] border-none px-4 py-3.5 rounded-lg text-sm outline-none focus:ring-2 ring-gray-200 transition">
        </div>
      </div>

      <!-- ПРАВАЯ КОЛОНКА: ИТОГО -->
      <div class="bg-white rounded-xl p-6 md:p-8 shadow-sm sticky top-24">
        <h2 class="text-lg font-bold mb-6">Ваш заказ</h2>

        <!-- Список товаров из Pinia -->
        <div v-if="cartStore.items.length > 0" class="flex flex-col gap-4 mb-6 max-h-[300px] overflow-y-auto pr-2 custom-scrollbar">
          <div v-for="(item, index) in cartStore.items" :key="index" class="flex gap-4 items-start">
            <img :src="item.img" class="w-16 h-16 rounded-md object-cover border border-gray-100 flex-shrink-0">
            <div>
              <div class="font-bold text-sm leading-tight">{{ item.title }}</div>
              <div class="text-xs text-gray-400 mt-1">XS / Оверсайз</div>
              <div class="font-bold text-sm mt-1">{{ item.price }}₽</div>
            </div>
          </div>
        </div>
        <div v-else class="text-gray-400 text-sm mb-6 text-center py-4">
            Корзина пуста
        </div>

        <!-- Расчеты -->
        <div class="space-y-3 text-sm border-t border-gray-100 pt-5">
          <div class="flex justify-between">
            <span class="text-gray-600">Товары ({{ cartStore.count }})</span>
            <span class="font-medium">{{ cartStore.total }}₽</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-600">Доставка</span>
            <span class="font-medium">0₽</span>
          </div>
          <div class="flex justify-between text-red-500">
            <span>Скидка</span>
            <span>0₽</span>
          </div>
        </div>

        <div class="flex justify-between font-bold text-lg mt-5 pt-5 border-t border-gray-100">
          <span>Итого</span>
          <span>{{ cartStore.total }}₽</span>
        </div>

        <button @click="handlePayment" class="w-full bg-black text-white font-bold py-4 rounded-lg mt-6 hover:opacity-90 transition transform active:scale-[0.98]">
          Оплатить заказ
        </button>

        <p class="text-center text-[11px] text-gray-400 mt-3">
          Нажимая кнопку, вы соглашаетесь с условиями публичной оферты
        </p>
      </div>

    </div>
  </div>
</template>

<style scoped>
/* Тонкий скроллбар для списка товаров */
.custom-scrollbar::-webkit-scrollbar { width: 4px; }
.custom-scrollbar::-webkit-scrollbar-track { background: #f1f1f1; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #ddd; border-radius: 4px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #ccc; }
</style>