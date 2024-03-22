from datetime import date

class BaseSchem():
    def __init__(self, id:int):
        self.id = id

    def get_info_low(self):
        print(self.id)
    def get_info_full(self):
        print(self.id)

class Statistic(BaseSchem):
    def __init__(self, id:int, amount:int, source:str, category:str, event_date:date, fullname:str, total_income:int, total_expences:int, net_saving:int, year:date, month:date):
        super().__init__(id)
        self.id = id
        self.amount = amount
        self.source = source
        self.category = category
        self.event_date = event_date
        self.fullname = fullname
        self.total_income = total_income
        self.total_expences = total_expences
        self.net_saving = net_saving
        self.date = event_date
        self.month = month

    def get_info_income(self):
        print(f'Total amount {self.amount}, Source - {self.source}, Date - {self.event_date}')

    def get_info_expences(self):
        print(f'Total amount {self.amount}, Source - {self.category}, Date - {self.event_date}')

    def get_info_full(self):
        print(f'Fullname - {self.fullname}, Total income {self.total_income}, Total expences - {self.net_saving}, Net saving - {self.net_saving}, Date - {self.date}, Month - {self.month}')


class Users(BaseSchem):
    def __init__(self, id:int, fullname:str, username:str, email:str,     password:int, balance:int):
        super().__init__(id)
        self.id = id
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.balance = balance

    def get_info_users(self):
        print(f'Fullname {self.fullname}, Username - {self.username}, Email - {self.email}, Password - {self.password}, Balance - {self.balance}')

    def get_info_low_users(self):
        print(f'Fullname {self.fullname}, Balance - {self.balance}')