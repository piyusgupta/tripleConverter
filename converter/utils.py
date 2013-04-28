import new
from converter.models import *

def get_source_list():
    return tuple(Database.objects.filter(active = 1).order_by('name').values_list('id', 'name'))

def get_database_list(_id):
    source = Database.objects.get(id = _id)
    _module = new.module('db_connection')
    code = source.code_file.read()
    exec str(code) in _module.__dict__
    cursor = _module.get_connection(source.db_name, source.location, source.username, source.password)
    cursor.execute(_module.DB_LIST_QUERY)
    db_list = [e_value(x) for x in cursor.fetchall()]
    return tuple(zip(db_list, db_list))

def get_table_list(_id, db_name):
    source = Database.objects.get(id = _id)
    _module = new.module('db_connection')
    code = source.code_file.read()
    exec str(code) in _module.__dict__
    cursor = _module.get_connection(db_name, source.location, source.username, source.password)
    cursor.execute(_module.TABLE_LIST_QUERY %(db_name))
    table_list = [e_value(x) for x in cursor.fetchall()]
    return tuple(zip(table_list, table_list))

def get_data(_id, db_name, query):
    source = Database.objects.get(id = _id)
    _module = new.module('db_connection')
    code = source.code_file.read()
    exec str(code) in _module.__dict__
    cursor = _module.get_connection(db_name, source.location, source.username, source.password)
    cursor.execute(query)
    return cursor.fetchall()
   
e_value = lambda x : x.values()[0] if isinstance(x,(dict)) else x[0]