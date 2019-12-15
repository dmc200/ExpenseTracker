import sqlite3
import time
import datetime
import pandas as pd
import os
import random



# excel_tracker = pd.ExcelFile('C://Users//dchrie504//Desktop//Tutorial//Python//Expense_Tracker_DB//Expense_Tracker.xlsx')
# print(excel_tracker.sheet_names)
# months_List = list(excel_tracker.sheet_names)

#Create Connection
conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(1234556654, '2019-01-01', 'python', 5)")
	conn.commit()
	c.close()
	conn.close()


def dynamic_data_entry():
	unix = time.time()
	datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'Python'
	value = random.randrange(0,10)

	c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (? , ? , ? , ?)" , (unix, datestamp, keyword, value))
	conn.commit()
 

def read_from_db():
	c.execute('SELECT * FROM stuffToPlot')
	data = c.fetchall()

# create_table()
# for i in range(10):
# 	dynamic_data_entry()
# 	time.sleep(1)


c.close()
conn.close()