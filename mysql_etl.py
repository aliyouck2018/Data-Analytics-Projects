import mysql.connector

cnx = mysql.connector.connect(user='root',password='fanell', database='classicmodels')
cursor = cnx.cursor()

add_customer = ("INSERT INTO customers "
               "(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) "
               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

data_customer = (500, 'Fanell Technologies','Liyouck','Alex','+237697397296','Cite Chirac','Yassa','Douala','Littoral','4889','Cameroon',cursor.lastrowid,200000)
cursor.execute(add_customer, data_customer)
cnx.commit()

cursor.close()
cnx.close()