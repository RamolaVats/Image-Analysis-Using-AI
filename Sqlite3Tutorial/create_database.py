import sqlite3

#connection creating function
def create_connection(db_file):

	#connection object; connection opened
	conn = sqlite3.connect(db_file)
	#connection closed
	conn.close()

#creating database Database.db 
create_connection("Database.db")