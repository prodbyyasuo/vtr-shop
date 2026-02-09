import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])
  const isOpen = ref(false)

  const total = computed(() => items.value.reduce((acc, item) => acc + item.price, 0))
  const count = computed(() => items.value.length)

  function addToCart(product) {
    items.value.push(product)
    isOpen.value = true // Открыть корзину при добавлении
  }

  function removeFromCart(index) {
    items.value.splice(index, 1)
  }

  function toggleCart() {
    isOpen.value = !isOpen.value
  }

  return { items, isOpen, total, count, addToCart, removeFromCart, toggleCart }
})