import pymysql
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

db_info = {"host" : "localhost", "user" : "root", "password" : "s01010101!", "db" : 'ad', "charset" : 'utf8'}

class db_connection:
    def __init__(self, host, user, password, db, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    def connect(self):
        return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset)

class db_excute:
    def __init__(self, connection):
        self.connection = connection

    def execute_query(self, sql):
        try:
            with self.connection.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                data = cursor.fetchall()
                conn.commit()
                if data == () or data == []:
                    return {"success" : True}
                return data
        except Exception as e:
            print('예외가 발생했습니다.', e)
            return {"success" : False}
