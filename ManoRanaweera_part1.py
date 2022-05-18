#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from getpass import getpass

pswd = getpass()

connection = pymysql.connect(host='bioed.bu.edu', port=4253, user='mranawee', database='mranawee', password = pswd, local_infile=1)

cursor = connection.cursor() #for mySQL commands

query = """drop table Pathways;"""
query2 = """create table Pathways(path_id integer not null, pathname char(100), primary key(path_id));"""

try:
    cursor.execute(query)
except pymysql.Error as e:
        print(e)
        
try:
    cursor.execute(query2)
except pymysql.Error as e:
    print(e)

command = ('''load data local infile 'pathways.tab' into table Pathways;''')

try:
    cursor.execute(command)
except pymysql.Error as e:
    print(e)

try:
    cursor.execute('show tables;')
except pymysql.Error as e:
    print(e)
    
connection.commit()
cursor.close()
connection.close()




