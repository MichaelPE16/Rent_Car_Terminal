import sqlite3
from db.bd import DATABASE, USER
from datetime import datetime, timedelta


# classe1 = DATABASE('db/rentcar.db')
# table = input('Which table you want to read ->')
# datos = classe1.read(table)

# for i in datos: 
#     print(f'Nombre {i[1]}{i[2]} Wallet {i[3]}')


hoy = datetime.now()
mes = hoy + timedelta(days=29)
print(f"Siguiente mes {mes.strftime("%y-%m-%d")}")