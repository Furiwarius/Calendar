import logging
import os

class Logging():
    '''Класс логирования модулей календаря

    Отслеживает и записывает данные поступающие в функции для изменения бд,
    вывода на экран, расчета различных значений'''

    
    def __init__(self, path:str) -> None :
        '''Инициализация экземпляра класса

        При создании метод извлекает имя файла и ставит его в название логгера
        Входящие данные: путь к файлу (str), который нужно обрабатывать.
        Возвращает: None'''
        name = self.nameExtraction(path)
        
        self.logger = logging.getLogger(name)
        self.logger.propagate = False
        
        # установка уровня логгирования
        self.logger.setLevel(logging.DEBUG)

        # настройка обработчика
        self.handler = logging.FileHandler(f"log\{name}_logging.log", mode='w')
        # настройка форматировщика
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        
        # добавление форматировщика к обработчику
        self.handler.setFormatter(self.formatter)
        # добавление обработчика к логгеру
        self.logger.addHandler(self.handler)

        self.logger.info(f"Начало работы модуля логгирования {__name__}...")
    
    def getLogger(self):
        '''Получить логгер

        Входящие данные: None
        Возвращает: Логгер(Logger) для записи в журнал'''
        return self.logger


    def nameExtraction(self, path:str) -> str:
        '''Извлечение имени файла из пути

        Входящие данные: путь к файлу (str), из которого нужно извлечь имя файла.
        Возвращает: имя файла (str) без пути и без указания расширений'''
        
        name = os.path.basename(path)
        return name.replace(".py", "")
        
