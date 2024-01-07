import sqlite3
import csv

# Ryan Dennis

with sqlite3.connect("chinook.db") as conn:
    # SQL command to insert values
    command = """
            INSERT INTO customers (Company, FirstName, LastName, Address, City, PostalCode, Country, Email) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
              """

    # Open CSV file and execute SQL command to write to database
    with open("customers.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            conn.execute(command, row)
