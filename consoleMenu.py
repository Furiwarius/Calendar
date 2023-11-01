from colorama import init
from colorama import Fore, Back, Style
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
        
        # Текущий цвет фона для данного поля меню
        self.back_color = Back.RESET
        # Цвет поля при для смены цвета фона
        self.colorСhoice = Back.GREEN

        self.push_func = None
   
    
    def colorChange(self) -> None:
        '''Метод меняющий цвет поля меню

        Входящие данные: None'''
        self.back_color, self.colorChoice = self.colorChoice, self.back_color


    def backgroundColorSetting(self, new_color):
        '''Метод для настройки цвета фона

        Входящие данные: новый цвет фона'''
        
        self.colorСhoice = new_color

    
    def settingFuncion(self, func:function) -> None:
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


    def addField(self, name_field:str) -> MenuField:
        '''Метод создающий новое поле меню

        Входящие данные: имя поля (str)
        Возвращает: экземпляр класса MenuField с полученным именем'''
        
        new_field = MenuField(new_field)
        if len(self.field_list)==0:
            new_field.colorChange()
            self.target_field = new_field
        self.field_list.append(new_field)
        return new_field


    def keyProcessing(self):
        '''Обработка нажатия клавиш

        Метод реагирует на нажатие клавишь. При нажатии одной из нужных,
        вызывает функцию перемещения или обработку нажатия клавиши.
        Входящиее данные: None
        Возвращает: None'''
        #\x1b[A - up
        #\x1b[B - down
        keyboard.add_hotkey("\x1b[A", self.moveCursorUP())
        keyboard.add_hotkey("\x1b[B", self.moveCursorDown())
        keyboard.add_hotkey("enter", self.moveEnter())
        keyboard.add_hotkey("esc", self.moveEsc())


    def settingEsc(self, func) -> None:
        '''Настройка функции Esc

        Клавише esc присваивается передаваемая функция.
        Она будет вызываться при нажатии клавиши Esc
        Входящиее данные: Функция (funcion), которая будет вызываться
        при нажатии клавиши Esc
        Возвращает: None'''
        self.esc_func = func


    def moveEsc(self) -> None:
        '''Вызов функции присвоенной клавище Esc

        Входящиее данные: None
        Возвращает: None'''
        self.esc_func()


    def moveEnter(self) -> None:
        '''Выполнение функции присвоенной к полю,
        которое находится в таргете

        Входящиее данные: None
        Возвращает: None'''
        self.target_field.performFunction()


    def outputOnDisplay(self) -> None:
        '''Вывод полей меню на консоль

        Входящиее данные: None
        Возвращает: None'''
        
        print(self.name)
        for field in self.field_list:
            print(field.name)
    

    def cleaning(self) -> None:
        '''Очистка консоли

        Входящиее данные: None
        Возвращает: None'''
        
        os.system(['clear','cls'][os.name == 'nt'])
        
        
    def moveCursorUP(self) -> None:
        '''Переместить курсор вверх

        Метод перемещает курсор >вверх<, то есть назад по списку,
        заменяя значение переменной в таргете (MenuField)
        Входящиее данные: None
        Возвращает: None'''

        number = self.removeCursor()
        if number-1 < len(self.field_list)*(-1):
            self.changeCursor(0)
        else:
            self.changeCursor(number-1)


    def moveCursorDown(self)  -> None:
        '''Переместить курсор вниз

        Метод перемещает курсор >вниз<, то есть дальше по списку,
        заменяя значение переменной в таргете (MenuField)
        Входящиее данные: None
        Возвращает: None'''
        #ПРОПИСАТЬ ВЫХОД ИЗ ПРОЦЕССА!!!
        number = self.removeCursor()
        if number+1 > len(self.field_list):
            self.changeCursor(0)
        else:
            self.changeCursor(number-1)


    def removeCursor(self) -> int:
        '''Сменить цвет фона поля

        Данный метод вызывается при смене поля.
        Входящиее данные: None
        Возвращает: индекс поля, который сейчас находится в таргете'''
        
        self.target_field.colorChange()
        index = self.field_list.index(self.target_field)
        return index


    def changeCursor(self, index:int) -> None:
        '''Сменить таргет

        Данный метод меняет значение в переменной target_field текущего экземпляра класса на
        экземпляр класса MenuField из списка field_list с заданным индексом.
        Входящиее данные: индекс нового таргета (int)
        Возвращает: None'''
        
        self.target_field = self.field_list[index]
        self.target_field.colorChange()


    def processStarting(self):
        '''Метод запускающий процесс изображения полей и реагирования
        на нажатие клавиш

        Входящиее данные: None
        Возвращает: None'''
        
        self.click_processing = True
        while self.click_processing:
            self.cleaning()
            self.outputOnDisplay()
            self.keyProcessing()
