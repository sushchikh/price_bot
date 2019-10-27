import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='krot',
    passwd='1',
    database='new'
)

mycursor = mydb.cursor()
sql_formula = "INSERT INTO prices (id, name, price_strbt, price_instr) VALUE (%s, %s, %s, %s);"
my_list = [('00003', 'another name 3', '3000', '3300'),
('00004', 'another name 4', '3000', '3300'),
('00005', 'another name 5', '4000', '4400'),
('00006', 'another name 6', '5000', '5500')]
mycursor.executemany(sql_formula, my_list)
mydb.commit()

#mycursor.execute('SHOW TABlES')

#for tb in mycursor:
#    print(tb)

# print(mydb)


