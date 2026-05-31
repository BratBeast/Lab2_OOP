from abc import ABC, abstractmethod

class Command(ABC):
    """
    Патерн Command.
    Інкапсулює дію (запит) як окремий об'єкт.
    """
    @abstractmethod
    def execute(self):
        pass

class RunAlgorithmCommand(Command):
    """
    Команда для запуску алгоритму через наш існуючий Facade.
    """
    def __init__(self, facade, algo_name: str, data_type: str, ui_callback):
        self.facade = facade
        self.algo_name = algo_name
        self.data_type = data_type
        # Функція вікна Tkinter, яка оновиться після отримання результату
        self.ui_callback = ui_callback

    def execute(self):
        # Викликаємо логіку через фасад
        result = self.facade.run_algorithm(self.algo_name, self.data_type)
        # Передаємо результат назад в інтерфейс для відмальовування
        self.ui_callback(result)