<!--<script setup>-->
<!--import { ref } from 'vue'-->
<!--import { useRouter } from 'vue-router'-->
<!--import { useFavoritesStore } from '@/stores/favorites'-->
<!--import { useProductStore } from '@/stores/products' // <-&#45;&#45; Импорт стора-->
<!--import FilterModal from '../components/FilterModal.vue'-->

<!--const router = useRouter()-->
<!--const favoritesStore = useFavoritesStore()-->
<!--const productStore = useProductStore() // <-&#45;&#45; Инициализация-->
<!--const isFiltersOpen = ref(false)-->

<!--function openProduct(id) {-->
<!--    router.push({ name: 'product', params: { id } })-->
<!--}-->
<!--</script>-->

<!--<template>-->
<!--    <div class="animate-fade-in">-->
<!--        <div class="flex justify-between items-center mb-8">-->
<!--            <button @click="isFiltersOpen = true" class="bg-black text-white px-6 py-2.5 rounded-lg text-sm font-bold hover:opacity-80 transition">Фильтры</button>-->

<!--            &lt;!&ndash; Показываем кол-во найденных товаров &ndash;&gt;-->
<!--            <div class="text-sm text-gray-500">-->
<!--                {{ productStore.searchQuery ? `Найдено: ${productStore.filteredProducts.length}` : 'Все товары' }}-->
<!--            </div>-->
<!--        </div>-->

<!--        &lt;!&ndash; Если товары есть &ndash;&gt;-->
<!--        <div v-if="productStore.filteredProducts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-5 gap-y-14">-->
<!--            &lt;!&ndash; Используем filteredProducts для отображения &ndash;&gt;-->
<!--            <div v-for="product in productStore.filteredProducts" :key="product.id" class="flex flex-col gap-3 group relative">-->

<!--                <div @click="openProduct(product.id)" class="w-full aspect-square bg-white rounded flex items-center justify-center overflow-hidden cursor-pointer">-->
<!--                    <img :src="product.img" class="max-w-full max-h-full object-cover transition duration-500 group-hover:scale-105">-->
<!--                </div>-->

<!--                <div class="flex justify-between items-start">-->
<!--                    <div @click="openProduct(product.id)" class="cursor-pointer">-->
<!--                        <div class="font-bold text-base flex gap-2">-->
<!--                            {{ product.price }}₽-->
<!--                            <span v-if="product.oldPrice" class="text-gray-400 font-normal line-through text-sm">{{ product.oldPrice }}₽</span>-->
<!--                        </div>-->
<!--                        &lt;!&ndash; Подсветка текста при поиске (опционально, но красиво) &ndash;&gt;-->
<!--                        <div class="text-[15px] text-gray-800 mt-1">{{ product.title }}</div>-->
<!--                    </div>-->

<!--                    <button @click.stop="favoritesStore.toggleFavorite(product)" class="hover:opacity-60 transition">-->
<!--                        <svg v-if="favoritesStore.isFavorite(product.id)" class="w-6 h-6 fill-black stroke-black" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>-->
<!--                        <svg v-else class="w-6 h-6 stroke-black stroke-[1.5] fill-none" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>-->
<!--                    </button>-->
<!--                </div>-->
<!--            </div>-->
<!--        </div>-->

<!--        &lt;!&ndash; Если ничего не найдено &ndash;&gt;-->
<!--        <div v-else class="flex flex-col items-center justify-center py-20 text-center">-->
<!--             <div class="text-4xl mb-2">🔍</div>-->
<!--             <h3 class="text-lg font-bold">Ничего не найдено</h3>-->
<!--             <p class="text-gray-500">Попробуйте изменить запрос</p>-->
<!--             <button @click="productStore.clearSearch()" class="mt-4 text-black underline">Сбросить поиск</button>-->
<!--        </div>-->

<!--        <FilterModal :isOpen="isFiltersOpen" @close="isFiltersOpen = false" />-->
<!--    </div>-->
<!--</template>-->

<script setup>
import { useRouter } from 'vue-router'
import { useFavoritesStore } from '@/stores/favorites'
import { useProductStore } from '@/stores/products'
import { useFiltersStore } from '@/stores/filters'

const router = useRouter()
const favoritesStore = useFavoritesStore()
const productStore = useProductStore()
const filtersStore = useFiltersStore()

function openProduct(id) {
    router.push({ name: 'product', params: { id } })
}
</script>

<template>
    <div class="animate-fade-in">
        <div class="flex justify-between items-center mb-8">
            <button @click="filtersStore.toggleFilters" class="bg-black text-white px-6 py-2.5 rounded-lg text-sm font-bold hover:opacity-80 transition">Фильтры</button>

            <!-- Показываем кол-во найденных товаров -->
            <div class="text-sm text-gray-500">
                {{ productStore.searchQuery ? `Найдено: ${productStore.filteredProducts.length}` : 'Все товары' }}
            </div>
        </div>

        <!-- Если товары есть -->
        <div v-if="productStore.filteredProducts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-5 gap-y-14">
            <!-- Используем filteredProducts для отображения -->
            <div v-for="product in productStore.filteredProducts" :key="product.id" class="flex flex-col gap-3 group relative">

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

                    <button @click.stop="favoritesStore.toggleFavorite(product)" class="hover:opacity-60 transition">
                        <svg v-if="favoritesStore.isFavorite(product.id)" class="w-6 h-6 fill-black stroke-black" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                        <svg v-else class="w-6 h-6 stroke-black stroke-[1.5] fill-none" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Если ничего не найдено -->
        <div v-else class="flex flex-col items-center justify-center py-20 text-center">
             <div class="text-4xl mb-2">🔍</div>
             <h3 class="text-lg font-bold">Ничего не найдено</h3>
             <p class="text-gray-500">Попробуйте изменить запрос</p>
             <button @click="productStore.clearSearch()" class="mt-4 text-black underline">Сбросить поиск</button>
        </div>
    </div>
</template>