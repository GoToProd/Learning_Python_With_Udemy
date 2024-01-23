import psycopg2
from psycopg2 import Error
# print(psycopg2.__version__)


con = psycopg2.connect(
    dbname='test_database', 
    user = 'postgres', 
    password = 'postgres'
    )

cur = con.cursor()

# cur.execute("SELECT * FROM categories")
# fill = cur.fetchall()
# for i in fill:
#     print(i)

# cur.execute('DROP TABLE IF EXISTS CARS')
# con.commit()

# cur.execute("CREATE TABLE CARS(car_id serial PRIMARY KEY, car_name varchar, volume int);")
# con.commit()

# cur.execute("INSERT INTO CARS(car_name, volume) VALUES (%s, %s)", ("BMW", 4))
# cur.execute(
#     """INSERT INTO CARS(car_name, volume)
#     VALUES (%(name)s, %(volume)s)""", 
#     {'name':"Tesla", 'volume':3}
#     )
# con.commit()

# cur.execute("SELECT * FROM CARS")
# fill = cur.fetchall()
# for i in fill:
#     print(i)

try:
    cur.execute("INSERT INTO CARS(car_name, volume) VALUES (%s, %s)", ("AUDI", 2))
    cur.execute("""INSERT INTO CARS(car_name, volume)
    VALUES (%(name)s, %(volume)s)""", 
    {'name':"Toyota", 'volume':2.6})
    con.commit()
except (Exception, Error) as e:
    print('Errror', e)
finally:
    if con:
        cur.close()
        con.close()
        print("Done. Data been inserted. ")