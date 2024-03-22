from schemas import BaseSchem, Statistic, Users

def get_all(items:str):
    data = []
    for i in items:
        item = input(f'Введите {i} - ')
        data.append(item)
    return tuple(data)

def view_all(items:str, schema:BaseSchem):
    for item in items:
        schem = schema(*item)
        schem.get_info_low_users()

def view_full(item:str, schemas:BaseSchem, ) -> tuple | None:
    schema:BaseSchem = schemas(*item)
    schema.get_info_full()