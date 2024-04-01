from schemas import BaseSchema

def view_all_income(items:list, schema:BaseSchema):
    for item in items:
        schema(*item[:11]).get_info_income()

def view_all_users(items:list, schema:BaseSchema):
    for item in items:
        schema(*item).get_info_users()

def view_full(item:list, schema:BaseSchema):
    schema(*item).get_info_full()