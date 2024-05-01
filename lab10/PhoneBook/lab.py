import psycopg2
import csv
import openpyxl 
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)

cur = conn.cursor()

def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS postgres.public.phone_book (
            "PersonName" VARCHAR(255) NOT NULL,
            "PhoneNumber" VARCHAR(20) NOT NULL
        );
    ''')

# Call the function to create the table
create_table()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute(' INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES( %s, %s); ' , (name, number))

def importFromCSV():
    with open(r'C:\Users\hhhg4\Desktop\pp2\lab10\PhoneBook\abc.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute(' INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES( %s, %s); ', (personName, phoneNumber))

def importFromXL():
    book=openpyxl.load_workbook(r'C:\Users\hhhg4\Desktop\pp2\lab10\PhoneBook\abc.xlsx')
    sheet=book.active
    for row in sheet.iter_rows(values_only=True):
        if len(row) == 2:
            cur.execute('INSERT INTO postgres.public.phone_book("PersonName", "PhoneNumber") VALUES (%s, %s);', row)
def update_contact(personName, phoneNumber):
    cur.execute(' UPDATE postgres.public.phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s ', (phoneNumber, personName))

def queryData():
    cur.execute(' SELECT * FROM postgres.public.phone_book ')
    data = cur.fetchall()
    path = r"C:\Users\hhhg4\Desktop\pp2\lab10\PhoneBook2\a.txt"
    for row in data:
        print(row)
    f = open(path, "w")
    for row in data:
        f.write("Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")
    f.close()


def deleteData():
    print("Which name do ypu want to delete?\n")
    personName = input()
    cur.execute(f''' DELETE FROM postgres.public.phone_book WHERE "PersonName"='{personName}' ''')

def deleteAllData():
    cur.execute(' DELETE FROM postgres.public.phone_book ')

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload form csv file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Delete data from table by person name\n\
          6. Delete all data from table\n\
          7. Upload form xlsx file\n\
          8. Exit")
    x = int(input("Enter number 1-5\n"))
    if(x == 1):
        inputData()
    elif(x == 2):
        importFromCSV()
    elif(x == 3):
        print("Which number do you want to update? Enter name and new number: ")
        name = input()
        newNumber = input()
        update_contact(name, newNumber)
    elif(x == 4):
        queryData()
    elif(x == 5):
        deleteData()
    elif(x == 6):
        deleteAllData()
    elif(x == 7):
        importFromXL()
    elif(x == 8):
        done = True
    conn.commit()
    
cur.close()
conn.close()