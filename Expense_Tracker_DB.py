import sqlite3
import time
import datetime
import pandas as pd
import os
from sqlalchemy import create_engine

# Create db 
engine = create_engine('sqlite:////Users/dchrie504//Desktop//Tutorial//Python//Expense_Tracker_DB//Expense_Tracker.db', echo=False)

# Create db connection and cursor
conn = sqlite3.connect('Expense_Tracker.db')
c = conn.cursor()

# Get list of months to make tables into from excel sheet
def get_sheets_list():
	excel_tracker = pd.ExcelFile(str(os.getcwd()) + '//Expense_Tracker.xlsx')
	month_list = list(excel_tracker.sheet_names)
	return month_list


# Load the data to the db 1 sheet = 1 table. Overwrite Table if it exists
def load_data():
	for i in get_sheets_list():
		df = pd.read_excel('C://Users//dchrie504//Desktop//Tutorial//Python//Expense_Tracker_DB//Expense_Tracker.xlsx', sheetname=f'{i}')
		df.to_sql(f'{i}', con=engine, if_exists='replace')

def select_from_db(table):
	c.execute(f'SELECT * FROM {table}')
	data = c.fetchall()
	print(data)



get_sheets_list()
load_data()
select_from_db('Nov17')








