import mysql.connector
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'us',
	)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print('All done!')
