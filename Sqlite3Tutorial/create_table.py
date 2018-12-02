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

#main function
def main():

	#required constants and queries
	database = "Database.db"
	create_table_sql = """ CREATE TABLE IF NOT EXISTS students(
								id integer PRIMARY KEY,
								name text NOT NULL,
								marks integer
							); """

	#creating database Database.db 
	conn = create_connection(database)

	#creating a table in Database.db
	create_table(conn, create_table_sql)

main()