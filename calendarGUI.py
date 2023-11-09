<<<<<<< HEAD
from consoleMenu import ConsoleMenu
=======
import calendar
from datetime import datetime
>>>>>>> 6a4f91569bd65f6074a187b5cf7be8469284df5d


class calendarConsole():

    def __init__(self) -> None:
        
        now_date = datetime.now()

        self.year = now_date.year
        self.month = now_date.month

        self.column_width = 3
        self.column_height = 2

        self.calr = calendar.TextCalendar(firstweekday=0)


    def setYear(self, new_year:int) -> None:
        self.year = new_year


    def setMonth(self, new_month:int) -> None:
        self.month = new_month


    def setWidth(self, new_width:int) -> None:
        self.column_width = new_width


    def setHeight(self, new_heigth:int) -> None:
        self.column_height = new_height


    def outputConsole(self) -> None:
        
        calr_output = self.calr.formatmonth(self.year, self.month,
                                       self.column_width, self.column_height)
        print(calr_output)



