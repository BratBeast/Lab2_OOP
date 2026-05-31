from src.algorithms.base import SortStrategy
from src.algorithms.metrics import timing_decorator

class BubbleSort(SortStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Bubble Sort"

    @timing_decorator
    def _sort(self, data: list):
        """Реалізація сортування бульбашкою."""
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]


class QuickSort(SortStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Quick Sort"

    @timing_decorator
    def _sort(self, data: list):
        """Реалізація швидкого сортування."""
        self._quick_sort_recursive(data, 0, len(data) - 1)

    def _quick_sort_recursive(self, data, low, high):
        if low < high:
            pi = self._partition(data, low, high)
            self._quick_sort_recursive(data, low, pi - 1)
            self._quick_sort_recursive(data, pi + 1, high)

    def _partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1


class BuiltInSortAdapter(SortStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Python Built-in Sort (Timsort)"

    @timing_decorator
    def _sort(self, data: list):
        """
        Патерн Adapter.
        Адаптує надзвичайно швидке вбудоване сортування Python
        під наш стандартизований інтерфейс SortStrategy.
        """
        data.sort()