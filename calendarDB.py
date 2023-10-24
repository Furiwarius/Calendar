import sqlalchemy as sqla


class calendarDatabase():

    def __init__(self) -> None:
        # при создании экземпляра класса связывается с бд календаря
        # если не находит, то создает пустую бд с таблицами

        self.engine = sqla.create_engine('sqlite:///calendarDB.db')
        self.conn = self.engine.connect()
        self.metadata = sqla.MetaData()
        self.createDataBase()
    

    def createDataBase(self):
        #создание таблиц в бд
        self.date = sqla.Table('date', self.metadata, 
            sqla.Column('id', sqla.Integer(), primary_key=True),
            sqla.Column('number', sqla.Integer(), nullable=False),
            sqla.Column('day_week', sqla.Integer(), nullable=False),
            sqla.Column('month', sqla.Integer(), nullable=False),
            sqla.Column('year', sqla.BigInteger(), nullable=False))

        self.record = sqla.Table('record', self.metadata, 
            sqla.Column('id', sqla.Integer(), primary_key=True),
            sqla.Column('content', sqla.String(200),  nullable=False))

        self.scheduledDays = sqla.Table('scheduledDays', self.metadata, 
            sqla.Column('day_id', sqla.Integer(), sqla.ForeignKey("date.id"), nullable=False),
            sqla.Column('record_id', sqla.Integer(), sqla.ForeignKey("record.id"), nullable=False))
        self.metadata.create_all(self.engine)


    def makeEntry(self, new_number:int, new_week:int, new_month:int, new_year:int, new_record:str):
        # внесение записи
        ins_date = self.makeDate(new_number, new_week, new_month, new_year)
        ins_recorrd = self.makeRecord(new_record)
        self.conn = self.engine.connect()
        self.conn.execute(ins_date)
        self.conn.execute(ins_recorrd)
    

    def makeDate(self, new_number:int, new_week:int, new_month:int, new_year:int):
        ins = self.date.insert().values(
        number = new_number,
        day_week = new_week,
        month = new_month,
        year = new_year)
        return ins


    def makeRecord(self, new_record:str):
        ins = self.record.insert().values(content = new_record) 
        return ins
    
    def findEntry(self):
        # найти запись
        pass


a = calendarDatabase()
record = "Сегодня я начал работать над дз"
a.makeEntry(24, 2, 10, 2023, record)


