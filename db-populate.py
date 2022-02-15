import sqlite3

db_locale = 'students.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
INSERT INTO contact_details (firstname, surname, street_address, suburb) VALUES
('David', 'Bowie', '11 Stardust Way', 'Wynnum'),
('Johnny', 'Cash', '1 Dark Way', 'Blackkall'),
('Kanye', 'West', '420 Space Way', 'Canadia')
""")

connie.commit()
connie.close()