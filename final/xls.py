# import the modules
import mysql.connector as mc
import xlwt
import pandas.io.sql as sql
# connect the mysql with the python
con=mc.connect(user="root",password="",host="localhost",database="project")
# read the data
df=sql.read_sql('SELECT * FROM devotees_details',con)
# print the data
print(df)
# export the data into the excel sheet
df.to_excel('ds.xls')