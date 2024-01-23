import psycopg2 as ps
from psycopg2 import Error
from timeit import default_timer as ti


con = ps.connect(dbname = 'test_database', user = 'postgres', password = 'postgres')
cur = con.cursor()


#Create a new table
def getCreateTable():
    try:
        cur.execute('DROP TABLE IF EXISTS Diary')
        cur.execute("CREATE TABLE Diary (diary_id serial PRIMARY KEY, p_fullname varchar, gender char, age int, city varchar DEFAULT 'Almaty');")
        con.commit()
        print("Table Dairy is created successfully")
    except (Exception, Error):
        print("Failed to create table", Error)
    finally:
        # cur.close()
        # con.close()
        print("Connection is close successfully")


#Inserting into table Diary
def getInsertTable():
    name, gender, age, city = input('Please enter your attribute by space: \n').split()
    try:
        cur.execute("INSERT INTO Diary (p_fullname, gender, age, city) VALUES (%s, %s, %s, %s)", (name, gender, age, city))
        con.commit()
        print(f'Data {name, gender, age, city} inserted successfully')
    except (Exception, Error):
        print("Failed to insert data", Error)
    finally:
        # cur.close()
        # con.close()
        print("Connection is close successfully")


#Update table Diary
def getUpdateTable():
    select, p_id = input("Please enter your choise p_fullname / age / gender / city and number of row_id: \n").split()
    if select == "p_fullname":
        try:
            name = input("Please enter your new name: \n")
            cur.execute("UPDATE Diary SET p_fullname = %s where diary_id = %s",(name, p_id))
            con.commit()
            print("Updating in Diary been successfully")
        except (Exception, Error):
            print("Failed to update Full Name", Error)
        finally:
            # cur.close()
            # con.close()
            print("Connection is close successfully")
    elif select == 'age':
        try:
            age = input("Please enter your new age: \n")
            cur.execute("UPDATE Diary SET age = %s where diary_id = %s",(age, p_id))
            con.commit()
            print("Updating in Diary been successfully")
        except (Exception, Error):
            print("Failed to update age", Error)
        finally:
            # cur.close()
            # con.close()
            print("Connection is close successfully")
    elif select == 'gender':
        try:
            gender = input("Please enter your new gender: \n")
            cur.execute("UPDATE Diary SET gender = %s WHERE diary_id = %s",(gender, p_id))
            con.commit()
            print("Updating in Diary been successfully")
        except (Exception, Error):
            print("Failed to update gender", Error)
        finally:
            # cur.close()
            # con.close()
            print("Connection is close successfully")
    elif select == 'city':
        try:
            city = input("Please enter your new city: \n")
            cur.execute("UPDATE Diary SET city = %s where diary_id = %s",(city, p_id))
            con.commit()
            print("Updating in Diary been successfully")
        except (Exception, Error):
            print("Failed to update city", Error)
        finally:
            # cur.close()
            # con.close()
            print("Connection is close successfully")
    else:
        print("You get a wrong column name")


#Delete a row in the table Diary
def getDeleteRow():
    diary_id = input("Please enter your id: \n")
    cur.execute("DELETE FROM Diary WHERE diary_id = %s",(diary_id))
    con.commit()
    print("Deleting in table Diary is completed successfully")


#Delete a all table Diary
def getDeleteTable():
    choose = input("Do you want to delete the table? y/n \n")
    if choose.lower() == "yes" or choose.lower() == "y":
        choose2 = input("Are you sure about it? y/n \n")
        if choose2.lower() == "yes" or choose2.lower() == "y":
            cur.execute("DELETE FROM Diary",())
            con.commit()
            print("Deleting in table Diary is completed successfully")
        elif choose2.lower() == "no" or choose2.lower() == "n":
            print("Deleting in table Diary was canclled")
        else:
            print("Unknown command")
    elif choose.lower() == "no" or choose.lower() == "n":
            print("Deleting in table Diary was canclled")
    else:
        print("Unknown command")


#Select all data from Diary
def getSelectedData():
    try:
        start = ti()
        cur.execute("SELECT * FROM Diary")
        fill = cur.fetchall()
        for i in fill:
            print(i)
        end = ti()
        print("Select completed successfully")
        print(f'Select took {end-start} for execution')
    except (Exception, Error):
        print("Failed to select from Diary", Error)
    finally:
        # cur.close()
        # con.close()
        print("Connection is close successfully")


print("""
    IF you want to CREATE a table choose a button 'C'
    IF you want to INSERT to table choose a button 'I'
    IF you want to UPDATE a table choose a button 'U'
    IF you want to DELETE a table choose a button 'D'
    IF you want to DELETE a row choose a button 'F'
    IF you want to SELECT a table choose a button 'S'
    IF you want to FINISH a table choose a button 'Q'
    """)


while True:
    choise = input("Enter your choise: \n")
    if choise.lower() == 'q':
        print("Thanks for using our application.")
        cur.close()
        con.close()
        print("Connection is closed successfully")
        break
    elif choise.lower() == 'c':
        getCreateTable()
    elif choise.lower() == 'i':
        getInsertTable()
    elif choise.lower() == 'u':
        getUpdateTable()
    elif choise.lower() == 'd':
        getDeleteTable()
    elif choise.lower() == 'f':
        getDeleteRow()
    elif choise.lower() == 's':
        getSelectedData()
