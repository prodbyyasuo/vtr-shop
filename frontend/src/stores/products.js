import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('products', () => {
  // Строка поиска
  const searchQuery = ref('')

  // Список всех товаров (перенесли из CatalogView)
  const products = ref([
    { id: 1, title: 'zip-худи /mezu//', price: 5000, oldPrice: 5000, img: 'https://placehold.co/400x400/111/fff?text=Zip-Hoodie' },
    { id: 2, title: 'handcuff bracelet', price: 2300, img: 'https://placehold.co/400x400/d4af37/000?text=Handcuffs' },
    { id: 3, title: 'Часы custom watches', price: 2600, img: 'https://placehold.co/400x400/222/fff?text=Watch' },
    { id: 4, title: 'Green Skull Hoodie', price: 4500, img: 'https://placehold.co/400x400/2f4f4f/fff?text=Green' },
    { id: 5, title: 'Hakama Pants', price: 3200, img: 'https://placehold.co/400x400/000/fff?text=Pants' },
    { id: 6, title: 'Silver Spike Watch', price: 2900, img: 'https://placehold.co/400x400/eee/333?text=Silver' },
  ])

  // Умный список: если есть поиск, фильтруем, если нет — показываем всё
  const filteredProducts = computed(() => {
    if (!searchQuery.value) return products.value

    const query = searchQuery.value.toLowerCase()
    return products.value.filter(p => p.title.toLowerCase().includes(query))
  })

  // Очистка поиска
  function clearSearch() {
    searchQuery.value = ''
  }

  return { products, searchQuery, filteredProducts, clearSearch }
})