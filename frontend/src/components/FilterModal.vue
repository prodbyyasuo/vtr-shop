<!--<script setup>-->
<!--defineProps({-->
<!--  isOpen: Boolean-->
<!--})-->
<!--defineEmits(['close'])-->
<!--</script>-->

<!--<template>-->
<!--  <div>-->
<!--    &lt;!&ndash; Затемнение фона &ndash;&gt;-->
<!--    <transition enter-active-class="transition-opacity duration-300" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition-opacity duration-300" leave-from-class="opacity-100" leave-to-class="opacity-0">-->
<!--      <div v-if="isOpen" @click="$emit('close')" class="fixed inset-0 bg-black/50 z-40"></div>-->
<!--    </transition>-->

<!--    &lt;!&ndash; Сайдбар слева &ndash;&gt;-->
<!--    <transition enter-active-class="transition transform duration-300" enter-from-class="-translate-x-full" enter-to-class="translate-x-0" leave-active-class="transition transform duration-300" leave-from-class="translate-x-0" leave-to-class="-translate-x-full">-->
<!--      <div v-if="isOpen" class="fixed top-0 left-0 h-full w-[320px] bg-white z-50 p-6 shadow-2xl overflow-y-auto">-->
<!--        <div class="flex justify-between items-center mb-6">-->
<!--            <h2 class="text-xl font-bold">Фильтры</h2>-->
<!--            <button @click="$emit('close')" class="text-2xl text-gray-400 hover:text-black">✕</button>-->
<!--        </div>-->

<!--        &lt;!&ndash; Сортировка &ndash;&gt;-->
<!--        <div class="mb-6">-->
<!--            <h3 class="font-bold text-sm mb-3">Сортировка</h3>-->
<!--            <div class="flex flex-col gap-2">-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" checked class="accent-black w-4 h-4"> Популярные</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> Новинки</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> По акции</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> Дешевле</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> Дороже</label>-->
<!--            </div>-->
<!--        </div>-->

<!--        &lt;!&ndash; Категории &ndash;&gt;-->
<!--        <div class="mb-6">-->
<!--            <h3 class="font-bold text-sm mb-3">Категория</h3>-->
<!--            <div class="flex flex-col gap-2">-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Выбрать всё</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Куртки</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Толстовки</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Футболки</label>-->
<!--                <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Аксессуары</label>-->
<!--            </div>-->
<!--        </div>-->

<!--        &lt;!&ndash; Цена &ndash;&gt;-->
<!--        <div class="mb-6">-->
<!--            <h3 class="font-bold text-sm mb-3">Цена</h3>-->
<!--            <div class="flex gap-3">-->
<!--                <input type="number" placeholder="0" class="w-1/2 border border-gray-200 rounded p-2 text-center text-sm outline-none focus:border-black">-->
<!--                <input type="number" placeholder="99999" class="w-1/2 border border-gray-200 rounded p-2 text-center text-sm outline-none focus:border-black">-->
<!--            </div>-->
<!--        </div>-->

<!--        <button @click="$emit('close')" class="w-full bg-black text-white py-3.5 rounded-lg font-bold hover:opacity-90 transition">Применить</button>-->
<!--      </div>-->
<!--    </transition>-->
<!--  </div>-->
<!--</template>-->

<script setup>
import { useFiltersStore } from '@/stores/filters'

const filtersStore = useFiltersStore()
</script>

<template>
  <div>
    <!-- Затемнение фона -->
    <transition enter-active-class="transition-opacity duration-300" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition-opacity duration-300" leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="filtersStore.isOpen" @click="filtersStore.toggleFilters" class="fixed inset-0 bg-black/50 z-40"></div>
    </transition>

    <!-- Сайдбар слева -->
    <transition enter-active-class="transition transform duration-300" enter-from-class="-translate-x-full" enter-to-class="translate-x-0" leave-active-class="transition transform duration-300" leave-from-class="translate-x-0" leave-to-class="-translate-x-full">
      <div v-if="filtersStore.isOpen" class="fixed top-0 left-0 h-full w-[380px] max-w-full bg-white z-50 p-6 shadow-2xl flex flex-col">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold">Фильтры</h2>
            <button @click="filtersStore.toggleFilters" class="text-2xl text-gray-400 hover:text-black">✕</button>
        </div>

        <!-- Контент с прокруткой -->
        <div class="flex-1 overflow-y-auto no-scrollbar">
          <!-- Сортировка -->
          <div class="mb-6">
              <h3 class="font-bold text-sm mb-3">Сортировка</h3>
              <div class="flex flex-col gap-2">
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" checked class="accent-black w-4 h-4"> Популярные</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> Новинки</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> По акции</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> Дешевле</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="radio" name="sort" class="accent-black w-4 h-4"> Дороже</label>
              </div>
          </div>

          <!-- Категории -->
          <div class="mb-6">
              <h3 class="font-bold text-sm mb-3">Категория</h3>
              <div class="flex flex-col gap-2">
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Выбрать всё</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Куртки</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Толстовки</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Футболки</label>
                  <label class="flex items-center gap-3 text-sm text-gray-600 cursor-pointer"><input type="checkbox" class="accent-black w-4 h-4 rounded"> Аксессуары</label>
              </div>
          </div>

          <!-- Цена -->
          <div class="mb-6">
              <h3 class="font-bold text-sm mb-3">Цена</h3>
              <div class="flex gap-3">
                  <input type="number" placeholder="0" class="w-1/2 border border-gray-200 rounded p-2 text-center text-sm outline-none focus:border-black">
                  <input type="number" placeholder="99999" class="w-1/2 border border-gray-200 rounded p-2 text-center text-sm outline-none focus:border-black">
              </div>
          </div>
        </div>

        <!-- Кнопка применить (прижата к низу) -->
        <div class="border-t border-gray-100 pt-5 mt-auto">
          <button @click="filtersStore.toggleFilters" class="w-full bg-black text-white py-3.5 rounded-lg font-bold hover:opacity-90 transition">Применить</button>
        </div>
      </div>
    </transition>
  </div>
</template>