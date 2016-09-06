import sqlite3


conn = sqlite3.connect('C:/Users/dsharp/PycharmProjects/kaggle_practice/data/world-food-facts/database.sqlite')

c = conn.cursor()

c.execute('SELECT * FROM sqlite_master')

print(c.fetchall())

c.execute('SELECT sugars_100g FROM FoodFacts where countries = \'United States\'')

print(c.fetchall())