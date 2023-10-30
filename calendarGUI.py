from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + 'зеленый текст')
print(Back.GREEN + 'на желтом фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')