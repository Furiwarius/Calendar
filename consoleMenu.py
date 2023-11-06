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
        
        # Текущий цвет фона для данного поля меню
        self.back_color = Back.RESET
        # Цвет поля при для смены цвета фона
        self.colorСhoice = Back.GREEN

        self.push_func = None
   
    
    def colorChange(self) -> None:
        '''Метод меняющий цвет поля меню

        Входящие данные: None'''
        self.colorChoice, self.back_color = self.back_color, self.colorChoice


    def backgroundColorSetting(self, new_color):
        '''Метод для настройки цвета фона

        Входящие данные: новый цвет фона'''
        
        self.colorСhoice = new_color

    
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


    def addField(self, name_field:str) -> MenuField:
        '''Метод создающий новое поле меню

        Входящие данные: имя поля (str)
        Возвращает: экземпляр класса MenuField с полученным именем'''
        
        new_field = MenuField(name_field)
        if len(self.field_list)==0:
            new_field.colorChange()
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
        #\x1b[A - up
        #\x1b[B - down
        keyboard.add_hotkey("\x1b[A", self.moveCursor())
        keyboard.add_hotkey("\x1b[B", self.moveCursor(mode=1))
        keyboard.add_hotkey("enter", self.moveEnter())
        keyboard.add_hotkey("esc", self.moveEsc())


    def settingEsc(self, func) -> None:
        '''Настройка функции Esc

        Клавише esc присваивается передаваемая функция.
        Она будет вызываться при нажатии клавиши Esc
        Входящиее данные: Функция (funcion), которая будет вызываться
        при нажатии клавиши Esc
        Возвращает: None'''
        self.log.debug(f"Клавище Esc присвоена функция {func}")
        self.esc_func = func


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
        print(self.menu_name)
        for field in self.field_list:
            print(field.name)
    

    def cleaning(self) -> None:
        '''Очистка консоли

        Входящиее данные: None
        Возвращает: None'''
        self.log.debug(f"Запущена очистка консоли")
        os.system(['clear','cls'][os.name == 'nt'])
        
        
    def moveCursor(self, mode = -1) -> None:
        '''Переместить курсор вверх

        Метод перемещает курсор >вверх<, то есть назад по списку,
        заменяя значение переменной в таргете (MenuField)
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
        '''Сменить цвет фона поля

        Данный метод вызывается при смене поля.
        Входящиее данные: None
        Возвращает: индекс поля, который сейчас находится в таргете'''
        if self.target_field!=None:
            self.log.debug(f"Запущена функция remobeCursor")
            self.target_field.colorChange()
            index = self.field_list.index(self.target_field)
            self.log.debug(f"Функция removeCursor возвращает индекс поля, находящегося в таргете: {index}")
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
        self.target_field.colorChange()


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

