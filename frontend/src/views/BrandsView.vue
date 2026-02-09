<script setup>
const brands = [
  {
    id: 1,
    name: 'CASHER COLLECTION',
    desc: 'Российский бренд уличной одежды, начавший свой путь в 2020 году. Наша философия - свобода и деньги.',
    img: 'https://via.placeholder.com/100/00ffff/000?text=CC'
  },
  {
    id: 2,
    name: 'SEASONED',
    desc: 'Российский бренд одежды с уникальным подходом к крою и материалам.',
    img: 'https://via.placeholder.com/100/333/fff?text=S'
  },
  {
    id: 3,
    name: 'Denjewerly',
    desc: 'Футуристичные и минималистичные украшения и аксессуары. 1800+ реальных отзывов в ВК.',
    img: 'https://via.placeholder.com/100/999/fff?text=D'
  },
  {
    id: 4,
    name: 'Ravir',
    desc: 'Красивое французское слово, которое символизирует стремление радовать и вдохновлять.',
    img: 'https://via.placeholder.com/100/22c55e/fff?text=R'
  }
]
</script>

<template>
  <div class="max-w-4xl mx-auto py-5 animate-fade-in">
    <div class="flex flex-col gap-10">

      <div v-for="brand in brands" :key="brand.id" class="flex flex-col md:flex-row items-center md:items-start gap-8 pb-10 border-b border-gray-200 last:border-0">
        <!-- Логотип -->
        <div class="w-24 h-24 rounded-full bg-gray-100 overflow-hidden flex-shrink-0 shadow-sm border border-gray-100">
           <img :src="brand.img" :alt="brand.name" class="w-full h-full object-cover">
        </div>

        <!-- Инфо -->
        <div class="flex-1 text-center md:text-left">
          <h2 class="text-xl font-bold uppercase mb-3 tracking-wide">{{ brand.name }}</h2>
          <p class="text-sm text-gray-600 leading-relaxed">{{ brand.desc }}</p>
        </div>

        <!-- Кнопки -->
        <div class="flex gap-2">
           <button class="bg-black text-white text-xs font-bold px-6 py-2.5 rounded-lg hover:opacity-80 transition">
             Нравится
           </button>
           <button class="w-9 h-9 bg-gray-100 rounded-lg flex items-center justify-center hover:bg-gray-200 transition">
             <svg class="w-4 h-4 text-black" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path><polyline points="16 6 12 2 8 6"></polyline><line x1="12" y1="2" x2="12" y2="15"></line></svg>
           </button>
        </div>
      </div>

    </div>
  </div>
</template>