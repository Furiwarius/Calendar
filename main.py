from calendarDB import CalendarDatabase
from datetime import datetime

db = CalendarDatabase()
db.makeEntry(datetime.now(), 'Пробная запись')