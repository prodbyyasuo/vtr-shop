<script setup>
const footerColumns = [
  {
    title: 'Витрина Маркет',
    links: ['Главная', 'Категории', 'Бренды', 'Релизы']
  },
  {
    title: 'Документы',
    links: ['Политика конфиденциальности', 'Пользовательское соглашение', 'Публичная оферта']
  },
  {
    title: 'Помощь',
    links: ['Тех поддержка', 'Кто выкладывает товары?', 'Как осуществляется доставка?', 'Связь с брендами']
  }
]
</script>

<template>
  <footer class="mt-auto bg-white border-t border-gray-100 py-12 px-5 md:px-10">
    <div class="max-w-[1600px] mx-auto grid grid-cols-1 md:grid-cols-4 gap-10">

      <!-- Колонка 1: QR Код (Заглушка) -->
      <div class="flex items-center justify-center border border-gray-100 rounded-xl h-28 bg-white text-black hover:shadow-sm transition-shadow cursor-pointer group">
         <div class="flex flex-col items-center gap-2">
            <!-- Имитация QR-кода -->
            <svg class="w-8 h-8 opacity-80 group-hover:opacity-100 transition" viewBox="0 0 24 24" fill="currentColor"><path d="M3 3h6v6H3zM15 3h6v6h-6zM3 15h6v6H3zM15 15h6v1h-6zM15 19h1v2h-1zM18 15h1v1h-1zM18 18h2v2h-2z"/></svg>
            <span class="text-xs font-bold uppercase tracking-wider">Скачать App</span>
         </div>
      </div>

      <!-- Остальные колонки (генерируются циклом) -->
      <div v-for="col in footerColumns" :key="col.title">
        <h4 class="font-bold text-sm mb-5 text-gray-900">{{ col.title }}</h4>
        <ul class="space-y-3">
          <li v-for="link in col.links" :key="link">
            <a href="#" class="text-sm text-gray-500 hover:text-black transition-colors duration-200">
              {{ link }}
            </a>
          </li>
        </ul>
      </div>

    </div>

    <!-- Копирайт (опционально) -->
    <div class="max-w-[1600px] mx-auto mt-12 pt-8 border-t border-gray-50 text-center md:text-left text-xs text-gray-400">
      © 2026 Витрина Маркет. Все права защищены.
    </div>
  </footer>
</template>