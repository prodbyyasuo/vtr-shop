import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useFiltersStore = defineStore('filters', () => {
  const isOpen = ref(false)

  function toggleFilters() {
    isOpen.value = !isOpen.value
  }

  return { isOpen, toggleFilters }
})