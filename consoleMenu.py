from colorama import init
from colorama import Fore, Back, Style
init()


class MenuField():
    '''Класс  реализующий поле в меню консоли
    
    Необходим для закрепления за полем имени и цвета фона поля'''

    def __init__(self, name:str) -> None:
        self.name = name
        # Текущий цвет фона для данного поля меню
        self.back_color = Back.RESET
        # Цвет поля при для смены цвета фона
        self.colorСhoice = Back.GREEN
    
    def colorChange(self) -> None:
        '''Метод меняющий цвет поля меню

        Входящие данные: None'''
        self.back_color, self.colorChoice = self.colorChoice, self.back_color  


class Menu():
    '''Класс  реализующий функции отображения меню в консоли
    
    Собирает поля меню (кнопки) из экземпляров класса MenuField'''

    def __init__(self) -> None:
        '''Метод инициализации'''
        pass


    def targetCursor(self):
        '''Установить курсор на поле меню'''
        pass
    

    def moveCursor(self):
        '''Переместить курсор с одного поля на другое'''
        pass

class ConsoleMenu():
    '''Класс  реализующий функции управления меню в консоли'''
    pass
