import psycopg2
import conf 
from views import StatisticsView, UsersView

def main():
    conn = psycopg2.connect(f"dbname={conf.DBNAME} user={conf.USER} password={conf.PASSWORD}")
    cur = conn.cursor()

    while True:
        print('1 - Statistic \n2 - Users \n3 - Exit')
        command = input('Enter command - ')
        if command == '1':
            stat_view = StatisticsView(cur)
            while True:
                print('1 - View all statistics\n2 - Search statistics\n3 - Add statistic\n4 - Back')
                sub_command = input('Enter sub command - ')
                if sub_command == '1':
                    stat_view.view_all_income()
                elif sub_command == '2':
                    stat_view.view_search_users_income()
                elif sub_command == '3':
                    stat_view.view_add_income()
                    conn.commit()
                elif sub_command == '4':
                    print('Back to main menu')
                    break
                else:
                    print('Invalid command')
        elif command == '2':
            user_view = UsersView(cur)
            while True:
                print('1 - View all users\n2 - Search user\n3 - Add user\n4 - Back')
                sub_command = input('Enter sub command - ')
                if sub_command == '1':
                    user_view.view_all_users()
                elif sub_command == '2':
                    user_view.view_search_users()
                elif sub_command == '3':
                    user_view.view_add_users()
                    conn.commit()
                elif sub_command == '4':
                    print('Back to main menu')
                    break
                else:
                    print('Invalid command')
        elif command == '3':
            print('Exiting program')
            break
        else:
            print('Invalid command')

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()