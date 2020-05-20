import pymysql, time
from configs import DB_NAME, MYSQL_HOST, DB_USERNAME, DB_PASSWORD
class MyDatabase():
    def __init__(self, name, endpoint, username, password, connect_timeout=86400):
        self.dbname = name
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.connect_timeout = connect_timeout
        self.createConnection()

    def createConnection(self):
        try:
            self.connection = pymysql.connect(self.endpoint, self.username, self.password, self.dbname,
                                              connect_timeout=self.connect_timeout,
                                              cursorclass=pymysql.cursors.DictCursor)
            # self.createCursor()
        except pymysql.err.OperationalError:
            print("DB downed, hang 60s")
            time.sleep(10)

    def createCursor(self):
        try:
            self.cursor = self.connection.cursor()
        except pymysql.err.OperationalError:
            print("DB downed, hang 60s")
            time.sleep(10)

    def reset(self):
        try:
            self.cursor.close()
            self.connection.close()
            self.createConnection()
        except pymysql.err.OperationalError:
            print("DB downed, hang 60s")
            time.sleep(10)
        except pymysql.err.Error:
            print("connection closed")

    def new_execute(self, query, params=None):
        new_cursor = self.connection.cursor()
        while True:
            try:
                if params:
                    new_cursor.execute(query, params)
                else:
                    new_cursor.execute(query)
                low_query = query[:5].lower()
                if "select" != low_query or "update" in low_query or 'insert' in low_query:
                    self.connection.commit()
                return new_cursor
            except pymysql.OperationalError as e:
                # if str(e) != 'database is locked':
                print("RETRY SQL", query, params, "CAUSED BY", e)
                time.sleep(1)

db = MyDatabase(DB_NAME, MYSQL_HOST, DB_USERNAME, DB_PASSWORD)