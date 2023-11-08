from colorama import init
from colorama import Fore, Back, Style
from loggingModule import Logging
import keyboard
import os

init()

class MenuField():
    '''Класс  реализующий поле в меню консоли
    
    Необходим для закрепления за полем имени и цвета фона поля'''

    def __init__(self, name:str) -> None:
        '''Метод инициализации

        При создании экземпляра класса передается имя экземпляра,
        которое будет выводится на экран при визуализации меню'''
        
        self.name = name

        self.push_func = None
   

    def __str__(self) -> str:
        return self.name
    

    def getName(self) -> str:
        return self.name

    
    def settingFuncion(self, func) -> None:
        '''Привязка функции к полю меню

        Входящие данные: функция, которая будет исполняться при нажатии на поле меню'''
        self.push_func = func


    def performFunction(self) -> None:
        '''Выполнение присвоенной этой функции

        Входящие данные: None'''
        self.push_func()
    

class ConsoleMenu():
    '''Класс  реализующий функции управления меню в консоли
    
    Собирает поля меню (кнопки) из экземпляров класса MenuField'''

    def __init__(self, name="Menu") -> None:
        '''Метод инициализации'''

        self.log = Logging(__file__).getLogger()

        self.menu_name = name
        # Список полей (кнопок)
        self.field_list = []
        # Выделенное поле
        self.target_field = None
        # Функция, срадатывающая при нажатии клавиши Esc
        self.esc_func = None

        # Переменная определяющая непрерывный процесс
        # обработки и изображения полей меню
        self.click_processing = True

        self.log.info(f"Создание эземпляра класса ConsoleMenu")


    def __str__(self) -> str:
        return self.menu_name


    def addField(self, name_field:str) -> MenuField:
        '''Метод создающий новое поле меню

        Входящие данные: имя поля (str)
        Возвращает: экземпляр класса MenuField с полученным именем'''
        
        new_field = MenuField(name_field)
        if len(self.field_list)==0:
            self.target_field = new_field
        self.field_list.append(new_field)
        
        self.log.info(f"Создан экземпляр класса MenuField с именем {name_field}")

        return new_field


    def keyProcessing(self):
        '''Обработка нажатия клавиш

        Метод реагирует на нажатие клавишь. При нажатии одной из нужных,
        вызывает функцию перемещения или обработку нажатия клавиши.
        Входящиее данные: None
        Возвращает: None'''
        
        key_input = keyboard.record("enter")
        if len(key_input)>1:
            last_input = key_input[-2].name
            if last_input=='up':self.moveCursor(mode=-1)
            elif last_input=='down':self.moveCursor()
            elif last_input=='esc':self.moveEsc()
        else:
            self.moveEnter()


    def settingEsc(self, func=None) -> None:
        '''Настройка функции Esc

        Клавише esc присваивается передаваемая функция.
        Если функия не передавалась, то будет использована функция 
        по умолчанию - escFuncion().
        Она будет вызываться при нажатии клавиши Esc
        Входящиее данные: Функция (funcion), которая будет вызываться
        при нажатии клавиши Esc
        Возвращает: None'''
        if func==None:
            self.esc_func=self.escFuncion
        else:
            self.esc_func = func
            self.log.debug(f"Клавище Esc присвоена функция {func}")
    

    def escFuncion(self):
        '''Функция выхода

        Функция выхода из цикла в processStarting.
        При нажатии клавиши esc будет срабатывать эта функция.
        Входящиее данные: None
        Возвращает: None'''
        self.log.debug(f"Вызвана стандартная функция выхода из меню")
        self.click_processing = False


    def moveEsc(self) -> None:
        '''Вызов функции присвоенной клавище Esc

        Входящиее данные: None
        Возвращает: None'''
        self.log.debug(f"Вызвана функция присвоенная клавище Esc")
        self.esc_func()


    def moveEnter(self) -> None:
        '''Выполнение функции присвоенной к полю,
        которое находится в таргете

        Входящиее данные: None
        Возвращает: None'''

        self.log.debug(f"Запущена функция на поле {self.target_field.name}")
        self.target_field.performFunction()


    def outputOnDisplay(self) -> None:
        '''Вывод полей меню на консоль

        Входящиее данные: None
        Возвращает: None'''

        self.log.debug(f"Запущен вывод меню в консоль")
        print(self)
        for field in self.field_list:
            self.outputFieldOnDisplay(field)
    

    def outputFieldOnDisplay(self, field:MenuField) -> None:
        '''Вывод поля на консоль

        Входящиее данные: поле (MenuField), которое нужно вывести в консоль
        Возвращает: None'''
        if self.target_field==field:
            print(Back.GREEN + str(field))
        else:
            print(Back.BLACK + str(field))


    def cleaning(self) -> None:
        '''Очистка консоли

        Входящиее данные: None
        Возвращает: None'''
        self.log.debug(f"Запущена очистка консоли")
        os.system(['clear','cls'][os.name == 'nt'])
        
        
    def moveCursor(self, mode = 1) -> None:
        '''Переместить курсор

        Метод перемещает курсор "вверх" или "вниз", то есть назад или вперед по списку
        в зависимости от знака mode (-1 - спускаемся, 1 - поднимаемся), заменяя значение 
        переменной в таргете (MenuField)
        Входящиее данные: None
        Возвращает: None'''
        self.log.debug(f"Запущена функция moveCursorUP")
        number = self.removeCursor()
        if number!=None:
            if number+mode < len(self.field_list)*(mode):
                self.changeCursor(0)
            else:
                self.changeCursor(number+mode)


    def removeCursor(self) -> int:
        '''Получение индекса поля в таргете

        Данный метод вызывается для получения поля, которое находится в таргете.
        Входящиее данные: None
        Возвращает: индекс поля, который сейчас находится в таргете'''
        if self.target_field!=None:
            self.log.debug(f"Запущена функция remobeCursor")
            index = self.field_list.index(self.target_field)
            self.log.debug(f"Функция removeCursor возвращает индекс поля, находящегося в таргете: {index}")
            self.log.debug(f"Сейчас в таргете находится поле {self.target_field.getName()}")
            return index
        return None


    def changeCursor(self, index:int) -> None:
        '''Сменить таргет

        Данный метод меняет значение в переменной target_field текущего экземпляра класса на
        экземпляр класса MenuField из списка field_list с заданным индексом.
        Входящиее данные: индекс нового таргета (int)
        Возвращает: None'''
        self.log.debug(f"Запущена функция changeCursor (смена таргета) c новым индеком {index}")
        self.log.debug(f"Таргет перешел от поля {self.target_field.name} на поле {self.field_list[index].name}")
        self.target_field = self.field_list[index]
        self.log.debug(f"В тарегете теперь находится поле {self.target_field.getName()}")


    def processStarting(self):
        '''Метод запускающий процесс изображения полей и реагирования
        на нажатие клавиш

        Входящиее данные: None
        Возвращает: None'''
        self.log.info(f"Запущена функция processStarting запускающая процесс отображения полей меню и считывания нажатых клавиш")
        self.click_processing = True
        while self.click_processing:
            self.cleaning()
            self.outputOnDisplay()
            self.keyProcessing()
        self.log.info(f"Функция processStarting прекратила работу")

