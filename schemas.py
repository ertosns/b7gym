import os
import io
import shutil
import sqlite3
import random
import string
import datetime
import requests
import calendar
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from tkinter import messagebox, simpledialog, ttk
from consts import ADMIN_MANAGER

# Connect to SQLite database
try:
    conn=sqlite3.connect('SQLite db/registered_users.db')
    cursor=conn.cursor()
    # Create a table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    contact_no TEXT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')

    cursor.execute('''INSERT INTO accounts (full_name, contact_no, username, password) values (?,?,?,?)
    ''', (ADMIN_MANAGER, ADMIN_NO, 'Admin', 'Admin@gym'))
    conn.commit()
except Exception as e:
    print("Error:", e)
    messagebox.showerror("Registration Error", "An error occurred during registration.")
finally:
    conn.close()

with sqlite3.connect('SQLite db/registration_form.db') as conn:
    cursor=conn.cursor()

    # Create a table to store registration information
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    age INTEGER,
    sex TEXT,
    birth_date DATE,
    contact_no TEXT,
    email TEXT,
    subscription_id TEXT,
    subscription_period TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT DEFAULT 'Ongoing',
    photo_data BLOB,
    week_mode REAL,
    cardio_mode REAL,
    full_name REFERENCES accounts(full_name)
    )
    ''')
# Create attendance record sqlite database if it doesn't exist
conn=sqlite3.connect('SQLite db/attendance_records.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS attendance_records (
id INTEGER PRIMARY KEY,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
contact_no TEXT,
subscription_id TEXT,
time_in TEXT,
time_out TEXT
)
''')

# Create a connection to the database (or create it if it doesn't exist)
conn=sqlite3.connect('SQLite db/register_equipment.db')

try:
    # Create a cursor object to interact with the database
    cursor=conn.cursor()

    # Create a table to store registration information
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_name TEXT NOT NULL,
    equipment_brand TEXT NOT NULL,
    equipment_model TEXT NOT NULL,
    equipment_serial_number TEXT NOT NULL,
    equipment_quantity TEXT NOT NULL,
    equipment_condition TEXT NOT NULL,
    equipment_type TEXT NOT NULL,
    equipment_status TEXT NOT NULL,
    equipment_location TEXT NOT NULL,
    equipment_training_required TEXT NOT NULL
    )
    ''')

    # Commit the changes
    conn.commit()

except sqlite3.Error as e:
    print(f"Error creating table: {e}")

finally:
    # Close the database connection
    conn.close()


# Create a connection to the database (or create it if it doesn't exist)
conn=sqlite3.connect('SQLite db/register_trainer.db')

# Create a cursor object to interact with the database
cursor=conn.cursor()

# Create the trainer table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS trainer (
id INTEGER PRIMARY KEY,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
age INTEGER,
sex TEXT,
birth_date DATE,
contact_no TEXT,
status TEXT DEFAULT 'Active',
photo_data BLOB
)
''')

# Create attendance record sqlite database if it doesn't exist
conn=sqlite3.connect('SQLite db/trainer_attendance_records.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS trainer_attendance (
id INTEGER PRIMARY KEY,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
contact_no TEXT,
time_in TEXT,
time_out TEXT
)
''')
conn.commit()
conn.close()

# Create a connection to the database (or create it if it doesn't exist)
try:
    with sqlite3.connect('SQLite db/visitors_log.db') as conn:
        # Create a cursor object to interact with the database
        cursor=conn.cursor()

        # Create a table to store registration information
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        contact_no TEXT,
        time_start TEXT
        )
        ''')

        # Commit the changes
        conn.commit()

except sqlite3.Error as e:
    print(f"SQLite error: {e}")

# Create a connection to the database (or create it if it doesn't exist)
conn=sqlite3.connect('SQLite db/register_employee.db')

# Create a cursor object to interact with the database
cursor=conn.cursor()

# Create a table to store registration information
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
age INTEGER,
sex TEXT,
birth_date DATE,
contact_no TEXT,
status TEXT DEFAULT 'Active',
photo_data BLOB
)
''')
# # to Add a new column to the table/ alter the name of the column, uncomment this.
# cursor.execute("ALTER TABLE employees ADD COLUMN photo_data BLOB")

# Commit the changes and close the database connection
conn.commit()
conn.close()

# Create attendance record sqlite database if it doesn't exist
conn=sqlite3.connect('SQLite db/employee_attendance_records.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee_attendance (
id INTEGER PRIMARY KEY,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
contact_no TEXT,
time_in TEXT,
time_out TEXT
)
''')
conn.commit()
conn.close()
