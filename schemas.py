from datetime import date

class BaseSchema:
    def __init__(self, id:int):
        self.id = id

    def get_info_low(self):
        print(self.id)
        
    def get_info_full(self):
        print(self.id)

class Statistic(BaseSchema):
    def __init__(self, id:int, amount:int, source:str, category:str, event_date:date, fullname:str, total_income:int, total_expenses:int, net_saving:int, year:int, month:int):
        super().__init__(id)
        self.amount = amount
        self.source = source
        self.category = category
        self.event_date = event_date
        self.fullname = fullname
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.net_saving = net_saving
        self.year = year 
        self.month = month 

    def get_info_income(self):
        print(f'Total amount {self.amount}, Source - {self.source}, Date - {self.event_date}')

    def get_info_expenses(self):
        print(f'Total amount {self.amount}, Source - {self.category}, Date - {self.event_date}')

    def get_info_full(self):
        print(f'Fullname - {self.fullname}, Total income {self.total_income}, Total expenses - {self.total_expenses}, Net saving - {self.net_saving}, Year - {self.year}, Month - {self.month}')


class Users(BaseSchema):
    def __init__(self, id:int, fullname:str, username:str, email:str, password:int, balance:int):
        super().__init__(id)
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.balance = balance

    def get_info_users(self):
        print(f'Fullname {self.fullname}, Username - {self.username}, Email - {self.email}, Password - {self.password}, Balance - {self.balance}')

    def get_info_low_users(self):
        print(f'Fullname {self.fullname}, Balance - {self.balance}')