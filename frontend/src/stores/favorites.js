import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useFavoritesStore = defineStore('favorites', () => {
  const items = ref([])

  // Проверить, лайкнут ли товар
  function isFavorite(productId) {
    return items.value.some(item => item.id === productId)
  }

  // Добавить или удалить (Toggle)
  function toggleFavorite(product) {
    const index = items.value.findIndex(item => item.id === product.id)
    if (index === -1) {
      items.value.push(product)
    } else {
      items.value.splice(index, 1)
    }
  }

  const count = computed(() => items.value.length)

  return { items, isFavorite, toggleFavorite, count }
})