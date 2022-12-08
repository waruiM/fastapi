db_host='local postgres/Databases/postgres'
db_name='postgres'
db_user='postgres'
db_pass='mikeadmin'

import psycopg2

conn=psycopg2.connect(dbname=db_name,
user=db_user,
password=db_pass,
host=db_host)


conn.close()
