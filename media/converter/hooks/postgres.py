DB_LIST_QUERY = "select datname from pg_database"
TABLE_LIST_QUERY = "select table_name from information_schema.tables where table_schema = 'public' and table_type = 'BASE TABLE';"
COLUMN_LIST_QUERY = "SELECT column_name, udt_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name='%s' ORDER BY ordinal_position;"

def get_connection(db, host, username, password):
    import psycopg2
    import psycopg2.extras
    _conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (host, db, username, password)
    conn = psycopg2.connect(_conn_string)
    cur = conn.cursor()#cursor_factory=psycopg2.extras.RealDictCursor)
    return cur
