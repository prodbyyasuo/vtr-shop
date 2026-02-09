<script setup>
// Здесь можно добавить логику (например, logout)
</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-[280px_1fr] gap-6 items-start animate-fade-in">

    <!-- САЙДБАР (Меню) -->
    <aside class="flex flex-col gap-4">

      <!-- Карточка пользователя -->
      <div class="bg-white p-4 rounded-xl shadow-sm flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center text-white overflow-hidden">
             <!-- Аватарка заглушка -->
             <svg class="w-5 h-5 stroke-white stroke-2" viewBox="0 0 24 24" fill="none"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          </div>
          <span class="font-bold text-sm text-gray-900">user97308</span>
        </div>
        <button class="text-gray-400 hover:text-black transition">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
        </button>
      </div>

      <!-- Группы меню -->
      <div class="bg-white p-2 rounded-xl shadow-sm flex flex-col">
        <div v-for="item in ['Мои заказы', 'Мои сообщения', 'Нужна помощь?']" :key="item" class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg cursor-pointer group transition-colors">
          <div class="flex items-center gap-3 text-sm font-medium text-gray-700 group-hover:text-black">
             <!-- Иконка заглушка (квадратик) -->
             <span class="w-5 h-5 bg-gray-100 rounded flex items-center justify-center">
                <svg class="w-3 h-3 text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle></svg>
             </span>
             {{ item }}
          </div>
          <svg class="w-4 h-4 text-gray-300 group-hover:text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
      </div>

      <div class="bg-white p-2 rounded-xl shadow-sm flex flex-col">
        <div v-for="item in ['Мои данные', 'Стать продавцом']" :key="item" class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg cursor-pointer group transition-colors">
          <div class="flex items-center gap-3 text-sm font-medium text-gray-700 group-hover:text-black">
             <span class="w-5 h-5 bg-gray-100 rounded flex items-center justify-center">
                <svg class="w-3 h-3 text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg>
             </span>
             {{ item }}
          </div>
          <svg class="w-4 h-4 text-gray-300 group-hover:text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
      </div>

      <div class="bg-white p-2 rounded-xl shadow-sm flex flex-col">
         <div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg cursor-pointer group transition-colors">
          <div class="flex items-center gap-3 text-sm font-medium text-red-500">
             <span class="w-5 h-5 bg-red-50 rounded flex items-center justify-center">
                <svg class="w-3 h-3 text-red-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
             </span>
             Выйти из аккаунта
          </div>
        </div>
      </div>

    </aside>

    <!-- КОНТЕНТ (Пустое состояние) -->
    <div class="bg-white rounded-xl shadow-sm min-h-[500px] flex flex-col items-center justify-center text-center p-10">
        <div class="mb-6 opacity-80">
            <!-- SVG Глаза -->
            <svg width="120" height="80" viewBox="0 0 120 80" fill="none">
                <ellipse cx="35" cy="40" rx="25" ry="30" stroke="#9daeb8" stroke-width="6" fill="white"/>
                <circle cx="45" cy="40" r="10" fill="#222"/>
                <ellipse cx="85" cy="40" rx="25" ry="30" stroke="#9daeb8" stroke-width="6" fill="white"/>
                <circle cx="95" cy="40" r="10" fill="#222"/>
            </svg>
        </div>
        <div class="text-gray-500 font-medium text-sm">Выбери раздел слева</div>
    </div>
  </div>
</template>