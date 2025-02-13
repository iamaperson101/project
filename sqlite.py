import sqlite3

# Connect to a database (or create it if it doesn't exist)
words = sqlite3.connect('words.db')
wordcursor = words.cursor()

# Perform a bulk update using the LENGTH() function in SQLite
wordcursor.execute('''
UPDATE words
SET length = LENGTH(word)
''')

# Commit the changes to the database
words.commit()

# Close the cursor and connection
wordcursor.close()
words.close()
