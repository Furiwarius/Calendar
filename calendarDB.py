import sqlalchemy as sqla
from datetime import datetime
from loggingModule import Logging


class CalendarDatabase():
    '''Класс  управления базы данных календаря

    Взаимидействует с базой данных, сохраняя, изменяя,
    проводя поиск, удаляя записи на определенные
    даты. Отвечает только за обращение к бд, без
    валидации значений'''

    
    def __init__(self) -> None:

        self.log = Logging(__file__).getLogger()

        self.engine = sqla.create_engine('sqlite:///data/calendarDB.db')
        self.conn = self.engine.connect()
        self.metadata = sqla.MetaData()
        self.__creatingTables()
    

    def __creatingTables(self) -> None:
        #создание таблиц в бд
        '''Создание таблиц в базе данных

        В базе данных создаются 3 таблицы:
        date - хранит дату на которую существуют записи,
        record - хранит запись,
        scheduledDays - сводная таблица соотносящая даты и записи по id
        '''

        self.log.info(f"Начало создания таблиц БД")
        
        self.records = sqla.Table('records', self.metadata, 
            sqla.Column('id', sqla.Integer(), primary_key=True),
            sqla.Column('date', sqla.DateTime(), nullable=False),
            sqla.Column('content', sqla.String(200), nullable=False))

        self.metadata.create_all(self.engine)

        self.log.info(f"Завершение создания таблиц БД")


    def makeEntry(self, date:datetime, new_record:str) -> int:
        # внесение записи
        '''Внесение записи в бд

        Функция разделена на три части, которые выполняют записи в разные таблицы бд.
        Входящие данные: дата и время (Datetime), запись на эту дату (Str)'''

        self.log.info(f"Внесение новой записи в бд")
        request = sqla.insert(self.records).values(
                date = date,
                content = new_record)
        execution_request = self.conn.execute(request)
        self.log.info(f"Запись успешно внесена. id записи: {execution_request}")
        return execution_request

    
    def findByDate(self, find_date:datetime) -> tuple:
        # найти id по дате
        '''Нахождение записи по дате

        Ищет входящую дату в таблице records и возвращает кортеж
        с id, где присутствует данная дата.
        Входящие данные: дата и время (datetime)
        Возвращает: None в случает отсутствия,
        кортеж id (tuple) в случае наличия дат в бд
        '''
        self.log.debug(f"Запущен метод findbyDate.n\Входящие данные: find_date = {find_date}")
        request = self.records.select([self.records.c.id]).where(
            self.records.c.date == find_date)
        result = self.conn.execute(request)
        self.log.debug(f"Результаты метода findByDate: {result}")
        return result


    def findByRecord(self, find_record:str) -> tuple:
        # найти id по записи
        '''Нахождение записи по тексту

        Ищет входящий текст в таблице records и возвращает кортеж
        с id, где присутствует данная запись.
        Входящие данные: запись (str)
        Возвращает: None в случает отсутствия,
        кортеж id (tuple) в случае наличия записи в бд
        '''
        self.log.debug(f"Запущен метод findbRecord.n\Входящие данные: find_record = {find_record}")
        request = self.records.select([self.records.c.id]).where(
            self.records.c.content == find_record)
        result = self.conn.execute(request)
        self.log.debug(f"Результаты метода findByRecord: {result}")
        return result


    def findByRecord(self, find_record:str) -> tuple:
         # найти id записей по слову
         pass
    

    def getRecords(self, records_id:tuple) -> list:
        # Получить запись (текст)
        '''Получить запись по id в таблице records

        Входящие данные: кортеж (tuple) id нужных записей
        Возвращает: кортеж (tuple) c найденными записями'''
        self.log.debug(f"Запущен метод getRecords.n\Входящие данные: records_id = {records_id}")
        result = []
        for id_r in records_id:
            request = self.record.select([self.records.c.content]).where(
                self.records.c.id == id_r)
            execution_request = self.conn.execute(request)
            result.append(execution_request)
        self.log.debug(f"Результаты метода getRecords: {result}")
        return tuple(result)


    def getDate(self, records_id:tuple) -> list:
        # Получить дату
        '''Получить даты по id в таблице records

        Входящие данные: кортеж (tuple) id нужных дат
        Возвращает: кортеж (tuple) c найденными датами'''
        self.log.debug(f"Запущен метод getDate.n\Входящие данные: records_id = {records_id}")
        result = []
        for id_r in records_id:
            request = self.record.select([self.records.c.date]).where(
                self.records.c.id == id_r)
            execution_request = self.conn.execute(request)
            result.append(execution_request)
        self.log.debug(f"Результаты метода getRecords: {result}")
        return tuple(result)


    def changeEntry(self, record_id: int, new_content:str):
        # Изменить запись
        '''Изменить запись по id в таблице records

        Входящие данные: id нужной записи (int), новые данные (str)
        Возвращает: None'''

        self.log.info(f"Запущен метод changeEntry.n\Входящие данные: record_id = {record_id}; new_content = {new_content} ")
        request = sqla.update(self.records).where(
            self.records.c.id == record_id
            ).values( content = new_content)
        execution_request = self.conn.execute(request)
        self.log.info(f"Изменения успешно внесены")
            

    def deleteRecord(self, record_id: int) -> None:
        # Удалить запись
        '''Удалить запись по id в таблице records

        Входящие данные: id нужной записи (int)
        Возвращает: None'''

        self.log.info(f"Запущен метод deleteRecord.n\Входящие данные: record_id = {record_id}")
        request = sqla.delete(self.records).where(
            self.records.c.id == record_id)
        execution_request = self.conn.execute(request)
        self.log.info(f"Изменения успешно внесены")

    


