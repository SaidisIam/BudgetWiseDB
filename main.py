import psycopg2
import conf 

from views import StatisticsView, UsersView

def main():
    conn = psycopg2.connect(f"dbname={conf.DBNAME} user={conf.USER} password={conf.PASSWORD}")
    cur = conn.cursor()

    while True:
        print('1 - Statistic \n2 - Users \n3 - Exit')
        command = input('Введите комманду - ')
        if command == '1':
            while True:
                print('1 - посмотреть все статистики \n2 поиск статистик \n3 добавить статистику \n4 выйти')
                command = input('Введите комманду - ')
                book = StatisticsView(cur)
                if command == '1':
                    book.view_all_income()
                # elif command == '2':
                #     book.view_search_book()
                elif command == '3':
                    book.view_add_income()
                    conn.commit()
                elif command == '4':
                    print('Вернулись в Меню')
                    break
        elif command == '2':
            while True:
                print('1 - посмотреть всех user \n2 поиск user \n3 добавить user \n4 выйти')
                command = input('Введите комманду - ')
                author = UsersView(cur)
                if command == '1':
                    author.view_all_users()
                elif command == '2':
                    author.view_search_user()
                elif command == '3':
                    author.view_add_users()
                    conn.commit()
                elif command == '4':
                    print('Вернулись в Меню')
                    break
                    
        elif command == '3':
            print('Вы вышли из программы')
            break
                
        
        

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()