import pandas as pd
import mysql.connector
from datetime import datetime


print('Loading the excel file...')
transactions = pd.read_excel('ramasage_ordures_stats.xlsx')

DB_NAME = 'syrapp'
TABLES = {}
TABLES['transactions'] = (
    "CREATE TABLE `transactions` ("
    "  `Id` int,"
    "  `Date` date,"
    "  `Arrondissement` varchar(20),"
    "  `Quartier` varchar(20) ,"
    "  `Equipe` varchar(20) ,"
    "  `Tonnage` int ,"
     "  PRIMARY KEY (`Id`)"
    ") ENGINE=InnoDB")


print('Connecting to server...')
connection = mysql.connector.connect(user='username',password='password')
cursor = connection.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)


def create_table(cursor):
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


def insert_data(cursor):
	print('Inserting data ...')
	for index, transaction in transactions.iterrows():
	    add_transaction = ("INSERT INTO transactions "
	       "(Id,Date,Arrondissement,Quartier,Equipe,Tonnage) "
	       "VALUES (%s,%s,%s,%s,%s,%s)")

	    transaction_ = (
	        transaction['Id'],
            transaction['Date'],
	        transaction['Arrondissement'],
	        transaction['Quartier'],
	        transaction['Equipe'],
	        transaction['Tonnage'])

	    cursor.execute(add_transaction, transaction_)  

create_database(cursor)
create_table(cursor)
insert_data(cursor)

connection.commit()
cursor.close()
connection.close()