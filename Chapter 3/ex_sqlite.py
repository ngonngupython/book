import sqlite3
connection = sqlite3.connect("storehouse.db")
#sqlite3.connect(":memory:")
print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("CREATE TABLE product (name TEXT, unit TEXT, quantity INTEGER)")

cursor.execute("INSERT INTO product VALUES ('bread', 'loaf', 50)")
cursor.execute("INSERT INTO product VALUES ('egg','dozen', 100)")
cursor.execute("INSERT INTO product VALUES ('milk','carton', 150)")

rows = cursor.execute("SELECT name, unit, quantity FROM product").fetchall()
print(rows)

target_product_name = "egg"
rows = cursor.execute("SELECT name, unit, quantity FROM product WHERE name = ?", (target_product_name,), ).fetchall()
print(rows)

new_quantity = 10
product_name = "bread"
cursor.execute("UPDATE product SET quantity = ? WHERE name = ?", (new_quantity, product_name))

rows = cursor.execute("SELECT name, unit, quantity FROM product").fetchall()
print(rows)

released_product_name = "milk"
cursor.execute("DELETE FROM product WHERE name = ?", (released_product_name,))

rows = cursor.execute("SELECT name, unit, quantity FROM product").fetchall()
print(rows)





