import calendar
from datetime import datetime


class calendarConsole():

    def __init__(self) -> None:
        '''Инициализация экземпляра класса

        При создании класса создается дата создания экземпляра,
        из которой будет изпользоваться год и месяц, которые
        можно будет получать или менять. Они будут использованы 
        при выводе на консоль. Так же задаются ширина и высота 
        колонок для вывода на консоль календаря. Изначально 
        они равны: width = 3, heigth = 2. Их также можно 
        настроить и получить.
        Входящие данные: None
        Возвращает: None'''

        now_date = datetime.now()

        self.year = now_date.year
        self.month = now_date.month

        self.column_width = 3
        self.column_height = 2

        self.calr = calendar.TextCalendar(firstweekday=0)


    def __str__(self) -> str:
        '''Строковое представление экземпляра

        Входящие данные: None
        Возвращает: Календарь (str), вызванный методом formatmonth()'''

        calr_output = self.calr.formatmonth(self.year, self.month,
                                       self.column_width, self.column_height)
        return calr_output


    def getYear(self) -> int:
        '''Получить год

        Входящие данные: None
        Возвращает: Год (int)'''

        return self.year


    def setYear(self, new_year:int) -> None:
        '''Установить нужный год

        Входящие данные: Год (new_year) в формате int
        Возвращает: None'''

        self.year = new_year


    def getMonth(self) -> int:
        '''Получить месяц

        Входящие данные: None
        Возвращает: Месяц (int)'''

        return self.month
    

    def setMonth(self, new_month:int) -> None:
        '''Установить месяц

        Входящие данные: Менсяц (new_month) в формате int
        Возвращает: None'''

        self.month = new_month


    def setWidth(self, new_width:int) -> None:
        '''Установить ширину колонок

        Входящие данные: Новая ширина в формате int
        Возвращает: None'''

        self.column_width = new_width


    def setHeight(self, new_heigth:int) -> None:
        '''Установить высоту колонок

        Входящие данные: новая высота колонок в формате int
        Возвращает: None'''

        self.column_height = new_heigth


    def outputConsole(self) -> None:
        '''Вывести на экран текущий месяц календаря

        Печатает в консоль месяц календаря с текущими 
        настройками экземпляра (год, месяц, ширина колонок, высота колонок)
        Входящие данные: None
        Возвращает: None'''

        calr_output = self.calr.formatmonth(self.year, self.month,
                                       self.column_width, self.column_height)
        print(calr_output)



