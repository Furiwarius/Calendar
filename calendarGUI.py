import time
from consoleMenu import ConsoleMenu, MenuField
import keyboard
from colorama import Fore, Back, Style

menu = ConsoleMenu('Календарь')

menu.addField("Поле 1")
menu.addField("Поле 2")
menu.addField("Поле 3")

menu.outputOnDisplay()

