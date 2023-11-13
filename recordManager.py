import datetime
from calendarDB import CalendarDatabase

class RecordManager():
    '''Класс Менеджер запросов

    По сути является валидатором запросов к бд,
    который проверяет правильность отправляемых данных.
    Все взаимодействия с бд происходят с помощью
    '''

    def __init__(self, data_base: CalendarDatabase) -> None:
        '''Метод инициализации экземпляра класса 

        Входящие данные: База данных, с которой будет
        взаимодействовать менеджер запросов
        '''
        self.__data_base__ = data_base
        

    def __inputDate(self) -> datetime.datetime:
        '''Метод ввода даты 

        Метод запускает циклы для ввода чисел,
        для создания даты. Все вводимые значения
        проверяются на корректный ввод.
        Входящие данные: None
        Возвращаемое значение: дата в формате datetime
        '''
        day_input = self.__dateAcquisitionCycle("Введите день: ", 1)
        month_input = self.__dateAcquisitionCycle("Введите месяц числом: ", 2)
        year_input = self.__dateAcquisitionCycle("Введите год четырехзначным числом: ", 3)
        result_date = datetime.datetime(year_input, month_input, day_input)
        return result_date


    def __dateAcquisitionCycle(self, input_massage:str, date_mode:int) ->int:
        '''Метод собирающий вводимые данные 

        Метод запрашивает данные у пользователя, и проверяет
        их: чтобы ввод был не пустым и чтобы ввод был числом,
        а так же чтобы ввод не был отрицательным числом.
        В метод также поступает информация о том, чем именно должны
        быть вводимые пользователем данные (mode). Ввод поступает в метод
        checkingCorrectness, который проверяет, подходит ли цифра под
        данный формат времени (день, месяц или год)
        Входящие данные: Сообщение пользователю (str), дающее
        подсказку о том, что нужно вводить
        Возвращаемое значение: введенные данные в формате int
        '''
        response_collection_process = True
        while response_collection_process:
            new_input = input(input_massage)
            if self.__checkInputDate(new_input) and self.__checkingCorrectness(new_inpur, date_mode):
                response_collection_process = False
        return int(new_input)
        

    def __checkInputDate(self, number: str) -> bool:
        '''Метод проверки чисел 

        Выполняет проверку строки на пустоту, также на то,
        чтобы строка состояла из чисел, и на то, чтобы
        число не было отрицательным.
        Входящие данные: Число в виде строки (str)
        Возвращаемое значение: (str)
        '''
        if new_input!=None and new_input.isdigit() and int(new_input)>0:
            return True
        print("Получены некорректные данные. (Пустое, не число, меньше нуля)")
        return False


    def __checkingCorrectness(self, date:str, mode:int) -> bool:
        '''Метод проверки даты 

        Выполняет проверку строки в зависимости от
        поступаемого значения, а точнее модификации
        проверки этого значения. mode=1 - для дней,
        mode=2 - для месяцев, mode=3 - для лет.
        Входящие данные: Проверяемая строка (str), модификатор проверки (int)
        Возвращаемое значение: True если соответствует
        требованиям, False, если нет
        '''
        if mode==1 and int(date)<32: return True
        elif mode==2 and int(date)<12: return True
        elif mode==3 and len(date)==4: return True
        print("Получены некорректные данные. Не соотвутствуют формату.")
        return False


    def __inputrecord(self) -> str:
        '''Метод ввода записи 

        Метод запускает цикл для ввода записи.
        Запись проверяется на пустоту и на
        содержание из неотображаемых символов.
        После чего возвращается с удаленными
        пробелами с начала и конца строки.
        Входящие данные: None
        Возвращаемое значение: запись (str)
        '''
        flag = True
        while flag:
            new_input = input("Введите запись: ")
            if new_input!=None and new_input.isspace()==False:
                flag=False
        return new_input.lstrip().rstrip()


    def searchDate(self, date:datetime) -> None:
        pass


    def saveRecord(self) -> None:
        pass


    def createRecord(self) -> None:
        pass


    def changeRecord(self) -> None:
        pass
