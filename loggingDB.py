import logging

class LoggingDatabase():
    '''Класс логирования базы данных календаря

    Отслеживает данные поступающие в функции для изменения бд.'''
    
    def __init__(self) -> None :
        '''Инициализация экземпляра класса

        Входящие данные: None
        Возвращает: None'''
        
        self.logger = logging.getLogger("calendarDB")
        self.logger.propagate = False
        
        # установка уровня логгирования
        self.logger.setLevel(logging.DEBUG)

        # настройка обработчика
        self.handler = logging.FileHandler(f"log\calendarDB_logging.log", mode='w')
        # настройка форматировщика
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        
        # добавление форматировщика к обработчику
        self.handler.setFormatter(self.formatter)
        # добавление обработчика к логгеру
        self.logger.addHandler(self.handler)

        self.logger.info(f"Начало работы модуля логгирования {__name__}...")
        
