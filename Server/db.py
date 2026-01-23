import sqlite3

# 1. Connect to the database (creates the file if it doesn't exist)

class dbHandler:
	def __init__(self) -> None:
		self.conn = sqlite3.connect('sqlite.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS requests (message TEXT, device TEXT, timestamp TEXT)")
		self.conn.close()

	def new_request(self, message, device, timestamp):
		self.conn = sqlite3.connect('sqlite.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute("INSERT INTO requests VALUES (?, ?, ?)", (message, device, timestamp))
