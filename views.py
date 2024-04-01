from schemas import Statistic, Users
from db_models import  StatisticDB, UsersDB
from functions import view_all_income, view_all_users, view_full

class StatisticsView:
    def __init__(self, cur):
        self.statistic_db = StatisticDB(cur)

    # def view_all_income(self):
    #     data = self.statistic_db.get_db_income()
    #     view_all_income(data, Statistic)
    
    def view_all_income(self):
        data = self.statistic_db.get_db_income()
        for item in data:
            print(f"User: {item[0]}, Total Income: {item[2]}, Source: {item[3]}, Event date: {item[4]}")
            # print(f"User: {item[0]}, Total Income: {item[1]}, Total Expenses: {item[2]}, Net Saving: {item[3]}, Year: {item[4]}, Month:")

    def view_add_income(self):
        user_id = int(input('Enter user_id: '))
        amount = float(input('Enter amount: '))
        source = input('Enter source: ')
        event_date = input("Enter event's date: ")
        result = self.statistic_db.add_income(user_id, amount, source, event_date)
        if result:
            print('Successfully added')
        else:
            print('Error')

    def view_search_users_income(self):
        fullname = input("Enter user's fullname: ")
        result = self.statistic_db.get_statistic(fullname)
        if result:
            view_full(result, Statistic)
        else:
            print("User not found.")

class UsersView:
    def __init__(self, cur):
        self.users_db = UsersDB(cur)

    def view_all_users(self):
        data = self.users_db.get_db_users()
        view_all_users(data, Users)

    def view_add_users(self):
        # data = input('Enter fullname, username, email, password, balance: ').split()
        # result = self.users_db.add_users(*data)

        fullname = input('Enter fullname: ')
        username = input('Enter username: ')
        email = input('Enter email: ')
        password = input('Enter password: ')
        balance = input('Enter balance: ')
        result = self.users_db.add_users(fullname, username, email, password, balance)
        if result:
            print('Successfully added')
        else:
            print('Error')

    def view_search_users(self):
        fullname = input("Enter user's fullname: ")
        result = self.users_db.get_db_users(fullname)
        if result:
            view_all_users(result, Users)
        else:
            print("User not found.")