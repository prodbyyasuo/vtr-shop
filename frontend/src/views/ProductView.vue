<script setup>
import { ref, computed } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { useFavoritesStore } from '@/stores/favorites'

const route = useRoute()
const cartStore = useCartStore()
const favoritesStore = useFavoritesStore()
const id = Number(route.params.id)

// Полные данные товара
const product = ref({
    id: id,
    title: 'zip-худи /mezu//',
    price: 5000,
    oldPrice: 5000,
    img: 'https://placehold.co/400x400/111/fff?text=Zip-Hoodie',
    brand: 'KOBERKOT Not Found',
    // Вернули описание бренда
    desc: '«KOBERKOT NF»... создано для тех, кто имеет отношение к моде и показывает индивидуальность в своих образах.',
    // Вернули характеристики
    specs: {
        'Артикул': '2359302103',
        'Материал': 'Футер 3-нитка петля, Состав: 85% хлопок',
        'Принт': 'Нет',
        'Лекала': 'Оверсайз',
        'Пол': 'Унисекс',
        'Цвет': 'Черный',
        'Отправка': 'до 14 дней'
    }
})

// Логика выбора размера
const activeSize = ref('XS')
const sizes = ['XS', 'S', 'M', 'L']

const isFav = computed(() => favoritesStore.isFavorite(product.value.id))

function handleAddToCart() {
    // Добавляем в корзину с выбранным размером
    cartStore.addToCart({
        ...product.value,
        selectedSize: activeSize.value
    })
}
</script>

<template>
    <div class="animate-fade-in">
        <RouterLink to="/" class="inline-block mb-6 text-sm text-gray-500 hover:text-black transition">← Назад в каталог</RouterLink>

        <div class="bg-white rounded-xl p-6 md:p-10 grid grid-cols-1 md:grid-cols-[1.2fr_1fr] gap-12 shadow-sm">

            <!-- ЛЕВАЯ КОЛОНКА: Галерея -->
            <div class="relative">
                <div class="w-full aspect-square bg-[#f9f9f9] rounded-lg flex items-center justify-center mb-4 overflow-hidden">
                    <img :src="product.img" class="max-w-[95%] max-h-[95%] object-contain hover:scale-105 transition duration-500">
                </div>
                <!-- Точки навигации (вернули) -->
                <div class="flex justify-center gap-2 mt-4">
                    <div class="w-2 h-2 rounded-full bg-black cursor-pointer"></div>
                    <div class="w-2 h-2 rounded-full bg-gray-200 cursor-pointer hover:bg-gray-400"></div>
                    <div class="w-2 h-2 rounded-full bg-gray-200 cursor-pointer hover:bg-gray-400"></div>
                </div>
            </div>

            <!-- ПРАВАЯ КОЛОНКА: Информация -->
            <div class="flex flex-col gap-6">
                <!-- Заголовок и цена -->
                <div>
                    <h1 class="text-2xl font-medium text-gray-900">{{ product.title }}</h1>
                    <div class="text-2xl font-bold mt-2 flex items-center gap-3">
                        {{ product.price }}₽
                        <span v-if="product.oldPrice" class="text-base text-gray-400 font-normal line-through">{{ product.oldPrice }}₽</span>
                    </div>
                </div>

                <!-- Выбор размера (ВЕРНУЛИ) -->
                <div>
                    <div class="text-sm font-bold text-gray-400 mb-2">Размер:</div>
                    <div class="flex flex-wrap gap-2">
                        <button
                            v-for="size in sizes"
                            :key="size"
                            @click="activeSize = size"
                            :class="activeSize === size ? 'bg-black text-white border-black' : 'bg-white text-black border-gray-200 hover:border-black'"
                            class="border px-5 py-2.5 rounded-lg text-sm font-medium transition"
                        >
                            {{ size }}
                        </button>
                    </div>
                </div>

                <!-- Кнопки действий -->
                <div class="flex gap-3 mt-2">
                    <button @click="handleAddToCart" class="flex-1 bg-black text-white font-bold text-base rounded-lg py-4 hover:opacity-90 transition transform active:scale-[0.98]">
                        Добавить в корзину
                    </button>

                    <button @click="favoritesStore.toggleFavorite(product)" class="w-[58px] border border-gray-200 rounded-lg flex items-center justify-center hover:bg-gray-50 transition">
                        <svg v-if="isFav" class="w-6 h-6 fill-black stroke-black" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                        <svg v-else class="w-6 h-6 stroke-black fill-none stroke-[1.5]" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    </button>
                </div>

                <!-- Блок бренда (ВЕРНУЛИ) -->
                <div class="bg-[#f9f9f9] p-4 rounded-lg flex gap-4 items-center mt-2">
                    <div class="w-12 h-12 bg-black rounded-full text-white font-bold flex items-center justify-center text-lg flex-shrink-0">NF</div>
                    <div>
                        <div class="flex items-center gap-2">
                             <div class="font-bold text-sm uppercase">{{ product.brand }}</div>
                             <span class="text-[10px] bg-gray-200 text-gray-600 px-1.5 py-0.5 rounded font-bold">БРЕНД</span>
                        </div>
                        <div class="text-xs text-gray-500 mt-1 leading-snug">{{ product.desc }}</div>
                    </div>
                </div>

                <!-- Характеристики (ВЕРНУЛИ) -->
                <div class="border-t border-gray-100 pt-6 mt-2">
                    <h3 class="font-bold mb-4 text-base">Характеристики</h3>
                    <div class="flex flex-col gap-3">
                        <div v-for="(val, key) in product.specs" :key="key" class="flex justify-between text-sm border-b border-gray-50 pb-2 last:border-0">
                            <span class="text-gray-500">{{ key }}</span>
                            <span class="font-medium text-right">{{ val }}</span>
                        </div>
                    </div>

                    <div class="mt-4 text-xs text-gray-400">
                        Если у вас остались вопросы по товару - вы можете обратиться к продавцу
                    </div>
                    <button class="w-full border border-black text-black font-bold py-3 rounded-lg mt-3 text-sm hover:bg-gray-50 transition">
                        Написать продавцу
                    </button>
                </div>
            </div>
        </div>

        <!-- Описание (внизу) -->
        <div class="bg-white rounded-xl p-6 mt-4 flex justify-between items-center cursor-pointer hover:shadow-sm transition">
             <span class="font-bold">Описание</span>
             <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
        </div>
    </div>
</template>