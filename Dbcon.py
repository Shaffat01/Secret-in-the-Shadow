import pymysql

dbConfig = {
     'user': 'root', 
     'password': "1117",
     'host': '127.0.0.1',
     'database': 'adlogin', 
}

conn = pymysql.connect(**dbConfig)
print(conn)