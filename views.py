from schemas import Statistic, Users
from db_models import  StatisticDB, UsersDB
from functions import get_all, view_all, view_full

class StatisticsView:
    def __init__(self, cur):
        self.statistic_db = StatisticDB(cur)

    def view_all_income(self):
        data = self.statistic_db.get_db_income()
        view_all(data, Statistic)

    def view_add_income(self):
        data = get_all(['user_id', 'amount', 'source', 'date'])
        result = self.statistic_db.add_income(data[0], data[1])
        if result:
            print('Успешно')
        else:
            print('Ошибка')

    def view_search_user(self):
        fullname = get_all(["User's fullname"])[0]
        result = self.statistic_db.get_statistic(fullname)
        view_full(result,)

class UsersView:
    def __init__(self, cur):
        self.users_db = UsersDB(cur)

    def view_all_users(self):
        data = self.users_db.get_db_users()
        view_all(data, Users)

    def view_add_users(self):
        data = get_all(['fullname', 'username', 'email', 'password', 'balance'])
        result = self.users_db.add_users(data[0], data[1])
        if result:
            print('Успешно')
        else:
            print('Ошибка')