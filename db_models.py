class StatisticDB:
    def __init__(self, cur):
        self.cur = cur

    def get_db_income(self):
        self.cur.execute("select * from income")
        income = self.cur.fetchall()
        return income
    
    def get_statistic(self, fullname):
        self.cur.execute('select u.fullname,sum(i.amount) as total_income, sum(e.amount) as total_expenses, s.net_saving, s.year, s.month from statistics as s join users as u on s.user_id = u.id join income as i on i.user_id = u.id join expences as e on e.user_id = u.id  where fullname = %s group by u.fullname, s.net_saving, s.year, s.month', (fullname,))
        user = self.cur.fetchone()
        return user
    
    def add_income(self, user_id, amount, source, event_date):
        try:
            self.cur.execute("insert into income(user_id, amount, source, event_date) values (%s, %s, %s, %s)", (user_id, amount, source, event_date))
            return True
        except Exception as e:
            print(e)
            return False

class UsersDB:
    def __init__(self, cur):
        self.cur = cur

    def get_db_users(self):
        self.cur.execute("select * from users")
        users = self.cur.fetchall()
        return users
    
    def add_users(self, fullname, username, email, password, balance):
        try:
            self.cur.execute("insert into users(fullname, username, email, password, balance) values (%s, %s, %s, %s, %s)", (fullname, username, email, password, balance))
            return True
        except Exception as e:
            print(e)
            return False