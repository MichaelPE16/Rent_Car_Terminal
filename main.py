import sqlite3
from db.bd import DATABASE, USER


classe1 = DATABASE('db/rentcar.db')
table = input('Which table you want to read ->')
datos = classe1.read(table)

for i in datos: 
    print(f'Nombre {i[1]}{i[2]} Wallet {i[3]}')

