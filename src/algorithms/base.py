from abc import ABC, abstractmethod


class SortStrategy(ABC):
    """
    Базовий клас для алгоритмів сортування.
    Використовує патерн Strategy (як єдиний інтерфейс для різних алгоритмів)
    та патерн Template Method (метод execute задає загальний каркас роботи).
    """

    def __init__(self):
        self.name = "Unknown Strategy"

    def execute(self, data: list) -> list:
        """
        Шаблонний метод (Template Method).
        Задає строгу послідовність дій: копіювання -> сортування -> повернення результату.
        """
        # Працюємо з копією, щоб не мутувати оригінальні вхідні дані
        data_copy = data.copy()
        self._sort(data_copy)
        return data_copy

    @abstractmethod
    def _sort(self, data: list):
        """
        Конкретна реалізація сортування.
        Цей крок має бути реалізований у кожному конкретному підкласі.
        """
        pass