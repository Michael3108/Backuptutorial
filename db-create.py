import sqlite3

db_locale = 'students.db'

#since thhere is no file which is called student.db. Python creates one
connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
CREATE TABLE contact_details 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
firstname TEXT,
surname TEXT,
street_address TEXT,
suburb TEXT
)
""")

connie.commit()
connie.close()
