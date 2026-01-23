import sqlite3, json

# 1. Connect to the database (creates the file if it doesn't exist)

class dbHandler:
	def __init__(self) -> None:
		self.conn = sqlite3.connect('db.sqlite3')
		self.cursor = self.conn.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS requests (message TEXT, device TEXT, timestamp TEXT, raw TEXT)")
		self.conn.close()

	def new_request(self, message, device, timestamp, raw=''):
		self.conn = sqlite3.connect('db.sqlite3')
		self.cursor = self.conn.cursor()
		raw = json.dumps(raw)
		self.cursor.execute("INSERT INTO requests VALUES (?, ?, ?, ?)", (message, device, timestamp, raw))
		self.conn.commit()
		self.conn.close()


	def get_requests(self) -> list:
		self.conn = sqlite3.connect('db.sqlite3')
		self.cursor = self.conn.cursor()
		requests = self.cursor.execute("SELECT raw FROM requests").fetchall()
		self.conn.commit()
		self.conn.close()

		return requests

