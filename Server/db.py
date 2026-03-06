import sqlite3, json

# 1. Connect to the database (creates the file if it doesn't exist)

class dbHandler:
	def __init__(self, name='db.sqlite3') -> None:
		self.dbName = name
		self.conn = sqlite3.connect(self.dbName)
		self.cursor = self.conn.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS requests (message TEXT, device TEXT, timestamp TEXT, raw TEXT)")
		self.conn.close()

	def new_request(self, message, device, timestamp, raw=''):
		self.conn = sqlite3.connect(self.dbName)
		self.cursor = self.conn.cursor()
		raw = json.dumps(raw)
		
		self.cursor.execute("INSERT INTO requests VALUES (?, ?, ?, ?)", (message, device, timestamp, raw))
		self.conn.commit()
		self.conn.close()


	def get_requests(self, backwards=False) -> list:
		self.conn = sqlite3.connect(self.dbName)
		self.cursor = self.conn.cursor()
		requests = self.cursor.execute("SELECT raw FROM requests").fetchall()
		self.conn.commit()
		self.conn.close()

		output = []

		for i in requests:
			output.append(json.loads(i[0]))

		if backwards: output.reverse()

		return output
	
	def reset_DB(self):
		self.conn = sqlite3.connect(self.dbName)
		self.cursor = self.conn.cursor()
		self.conn.execute("DELETE FROM requests")
		self.conn.commit()
		self.conn.close()

