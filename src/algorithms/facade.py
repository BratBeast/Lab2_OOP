from src.algorithms.sorting import BubbleSort, QuickSort, BuiltInSortAdapter
from src.algorithms.factory import DataFactory
from src.algorithms.config import SettingsManager


class AlgorithmFacade:
    """
    Патерн Facade.
    Надає спрощений уніфікований інтерфейс для роботи з підсистемою алгоритмів.
    Сховує складність створення даних, вибору стратегії та виклику методів.
    """

    def __init__(self):
        self.settings = SettingsManager()

        # Ініціалізуємо доступні стратегії сортування
        self._algorithms = {
            "Bubble Sort": BubbleSort(),
            "Quick Sort": QuickSort(),
            "Python Built-in (Timsort)": BuiltInSortAdapter()
        }

    def get_available_algorithms(self) -> list:
        """Повертає список назв доступних алгоритмів для випадаючого списку в GUI."""
        return list(self._algorithms.keys())

    def get_available_data_types(self) -> list:
        """Повертає типи даних для генерації."""
        return ["random", "sorted", "reversed", "nearly_sorted"]

    def run_algorithm(self, algo_name: str, data_type: str = "random") -> dict:
        """
        Головний метод фасаду.
        Об'єднує роботу Factory Method, Singleton, Strategy та Decorator.
        """
        if algo_name not in self._algorithms:
            raise ValueError(f"Алгоритм {algo_name} не знайдено!")

        # 1. Отримуємо розмір масиву з Singleton-налаштувань
        size = self.settings.array_size

        # 2. Генеруємо вхідні дані через Factory
        original_data = DataFactory.create_data(data_type, size)

        # 3. Отримуємо потрібну стратегію
        strategy = self._algorithms[algo_name]

        # 4. Виконуємо сортування (всередині відпрацюють Template Method та Decorator)
        # Оскільки декоратор зараз виводить час у консоль, ми просто отримуємо відсортований масив
        sorted_data = strategy.execute(original_data)

        # Повертаємо зручний словник з результатами для GUI
        return {
            "algorithm": algo_name,
            "data_type": data_type,
            "size": size,
            "original_data": original_data,
            "sorted_data": sorted_data
        }