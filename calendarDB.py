import sqlalchemy as sqla
from datetime import datetime


class CalendarDatabase():
    '''Класс  управления базы данных календаря

    Взаимидействует с базой данных, сохраняя, изменяя, проводя поиск,
    удаляя записи на определенные даны'''
    
    def __init__(self) -> None:

        self.engine = sqla.create_engine('sqlite:///calendarDB.db')
        self.conn = self.engine.connect()
        self.metadata = sqla.MetaData()
        self.creatingTables()
    

    def creatingTables(self) -> None:
        #создание таблиц в бд
        '''Создание таблиц в базе данных

        В базе данных создаются 3 таблицы:
        date - хранит дату на которую существуют записи,
        record - хранит запись,
        scheduledDays - сводная таблица соотносящая даты и записи по id
        '''
        
        self.date = sqla.Table('date', self.metadata, 
            sqla.Column('id', sqla.Integer(), primary_key=True),
            sqla.Column('date', sqla.DateTime(), nullable=False),
            sqla.Column('day_week', sqla.Integer(), nullable=False))

        self.record = sqla.Table('record', self.metadata, 
            sqla.Column('id', sqla.Integer(), primary_key=True),
            sqla.Column('content', sqla.String(200),  nullable=False))

        self.scheduledDays = sqla.Table('scheduledDays', self.metadata, 
            sqla.Column('day_id', sqla.Integer(), sqla.ForeignKey("date.id"), nullable=False),
            sqla.Column('record_id', sqla.Integer(), sqla.ForeignKey("record.id"), nullable=False))
        self.metadata.create_all(self.engine)


    def makeEntry(self, date:datetime, new_record:str) -> None:
        # внесение записи
        '''Внесение записи в бд

        Функция разделена на три части, которые выполняют записи в разные таблицы бд.
        Входящие данные: дата и время (Datetime), запись на эту дату (Str)'''

        date_id = self.makeDate(date)
        record_id = self.makeRecord(new_record)
        #self.makeScheduledDays(date_id, record_id)
    

    def makeDate(self, new_date:datetime) -> int:
        # добавить дату
        '''Добавление даты в таблицу date
        
        Входящие данные: дата и время (Datetime)
        Возвращает id внесенных данных'''

        if self.dateSearch(new_date)==None:
            request = sqla.insert(self.date).values(
                date = new_date,
                day_week = new_date.weekday())
            execution_request = self.conn.execute(request)
            return execution_request.inserted_primary_key
        else:
            return self.dateSearch(new_date)
                    

    def makeRecord(self, new_record:str) -> int:
        # добавить запись
        '''Добавление записи в таблицу record
        
        Входящие данные: текст, который нужно сохранить (str)
        Возвращает id внесенных данных'''

        request = sqla.insert(self.record).values(content = new_record) 
        execution_request = self.conn.execute(request)
        return execution_request.inserted_primary_key
        

    def makeScheduledDays(self, date_id:int, new_record_id:int) -> None:
        # добавить id в сводную таблицу
        '''Вносит в сводную таблицу scheduledDays id даты и id записи

        Входящие данные: id даты из таблицы date и id записи на эту дату из таблицы record
        Возвращает id внесенных данных'''

        request = sqla.insert(self.record).values(
            day_id = date_id,
            record_id = new_record_id) 
        execution_request = self.conn.execute(request)
        return execution_request

    
    def findEntry(self, find_date:datetime) -> tuple:
        # найти записи
        '''Нахождение записи по дате

        Проверяет наличие полученной даты в таблице date. 
        В случае если такая дата есть, возвращает все имеющиеся к ней записи.
        Входящие данные: дата и время (datetime)
        Возвращает: None в случает отсутствия, кортеж (tuple) в случае наличия даты в бд'''

        answer = self.dateSearch(find_date)
        if answer!=None:
            records_id = self.searchIdRecords(answer)
            return self.searchRecords(records_id)
        else: 
            return None
            
            
    def dateSearch(self, find_date:datetime) -> int:
        # найти дату
        '''Проверка наличия даты в бд

        Проверяет наличие полученной даты в таблице date.
        Входящие данные: дата и время (datetime)
        Возвращает: None в случает отсутствия, id поля в котором хранится дата в случае если такая дата есть'''

        request = self.date.select().where(
            self.date.c.date == find_date)
        execution_request = self.conn.execute(request)
        return execution_request.scalar()


    def searchIdRecords(self, date_id:int) -> tuple:
        # найти id записей
        '''Нахождение id записей в таблице scheduledDays по id даты

        Ищет в таблице scheduledDays id записей связанные с id полученной даты
        Входящие данные: id даты (int)
        Возвращает: кортеж с id имеющихся записей'''

        request = self.scheduledDays.select([self.record.c.id]).where(
            self.scheduledDays.c.date == date_id)
        execution_request = self.conn.execute(request)
        return execution_request


    def searchRecords(self, records_id:sqla.ResultProxy) -> list:
        # найти записи
        '''Найти записи по id в таблице records

        Входящие данные: список (list) id нужных записей
        Возвращает: список (list) c найденными записями'''

        result = []
        for id_r in records_id:
            request = self.record.select([self.record.c.content]).where(
                self.record.c.id == id_r)
            execution_request = self.conn.execute(request)
            result.append(execution_request)
        return result
    

db = CalendarDatabase()

db.makeEntry(datetime.now(), 'Пробная запись')
