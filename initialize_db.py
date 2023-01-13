import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE orders
#              (text, trans text, symbol text, qty real, price real)''')


# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# EXISTING ORDERS
# Create table
c.execute('''CREATE TABLE orders
             (order_date, order_number, order_email, article, status)''')

# data to be added
purchases = [('2006-01-05',123456,'example@rasa.com', '102', 'shipped'),
             ('2021-01-05',123457,'me@rasa.com', '501', 'order pending'),
             ('2021-01-05',123458,'me@gmail.com', '601', 'delivered'),
            ]

# add data
c.executemany('INSERT INTO orders VALUES (?,?,?,?,?)', purchases)

# AVAILABLE INVENTORY
# Create table
c.execute('''CREATE TABLE inventory
             (article, type, brand)''')

# data to be added
inventory = [('101', 'shoes', 'A'),
             ('102', 'shoes', 'B'),
             ('103', 'shoes', 'C'),
             ('201', 'jacket', 'A'),
             ('202', 'jacket', 'C'),
             ('203', 'jacket', 'A'),
             ('301', 'shirt', 'B'),
             ('302', 'shirt', 'C'),
             ('401', 'hat', 'A'),
             ('402', 'hat', 'C'),
             ('501', 'scarf', 'B'),
             ('601', 'pants', 'A')
            ]

# add data
c.executemany('INSERT INTO inventory VALUES (?,?,?)', inventory)

# Create table
c.execute('''CREATE TABLE reviews
             (article, review)''')

# data to be added
reviews = [('101', 'good shoes at a good price'),
           ('101', 'terrible quality. be careful'),
           ('101', 'ok'),
           ('103', 'I bought a size 42, but it is more like 40'),
           ('201', 'jacket is cool'),
           ('201', '4/5 :)'),
           ('202', 'very warm, suitable for winter'),
           ('301', 'received an item with a defect'),
           ('301', '5/5'),
           ('301', 'thank you! happy new year'),
           ('301', 'i had problem with delivery, but product is ok'),
           ('302', 'normal'),
           ('402', 'i like this brand so much, very good'),
           ('402', 'bad quality'),
           ('601', 'pretty good')
           ]

# add data
c.executemany('INSERT INTO reviews VALUES (?,?)', reviews)


# Save (commit) the changes
conn.commit()

# end connection
conn.close()