from flask import Flask,redirect,url_for,render_template,request,session,flash,jsonify
from os import path
import pyodbc

server = 'LAPTOP-FF387IJ3\HOANGQUAN'
database = 'Account'
username = 'quan'
password = '123456'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

a='quan@gmail.com'
b='123'
#cursor.execute("SELECT * FROM NGANHANGCAUHOI WHERE mamon IN (?)",(mamonthi))
cursor.execute("UPDATE NGUOIDUNG SET pass=(?) WHERE username IN (?)",(b),(a))
conn.commit()
for row in cursor.execute("select * from NGUOIDUNG"):
    print(row)