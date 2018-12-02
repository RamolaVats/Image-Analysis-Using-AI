import sqlite3

#connection creating function
def create_connection(db_file):

	#connection object; connection opened
	conn = sqlite3.connect(db_file)
	#returning the connection object
	return conn

#table creating function
def create_table(conn, create_table_sql):

	#creating a cursor object
	cursor = conn.cursor()
	#executing the creation of the table
	cursor.execute(create_table_sql)

#inserting into the table students
def insert_values(conn, values):

	#insert query to be fired
	insert_query = """ INSERT INTO students(id, name, marks) VALUES (?,?,?) """

	cursor = conn.cursor()
	#executing insert query
	cursor.execute(insert_query, values)

#selecting all values from students
def select_values(conn, select_query):

	cursor = conn.cursor()
	cursor.execute(select_query)

	rows = cursor.fetchall()
	
	for row in rows:
		print(row[0], ' ', row[1], ' ', row[2])

#main function
def main():

	#required constants and queries
	database = "Database.db"
	create_table_sql = """ CREATE TABLE IF NOT EXISTS students(
								id integer PRIMARY KEY,
								name text NOT NULL,
								marks integer
							); """
	values1 = (1, 'Amish', 50,)
	values2 = (2, 'Rajat', 45,)
	values3 = (3, 'Ramola', 42,)
	select_query = """ SELECT * FROM students """

	#creating database Database.db 
	conn = create_connection(database)

	#creating a table in Database.db
	create_table(conn, create_table_sql)

	#inserting a row into table students
	insert_values(conn, values1)
	insert_values(conn, values2)
	insert_values(conn, values3)

	#selecting all values from students
	select_values(conn, select_query)

main()