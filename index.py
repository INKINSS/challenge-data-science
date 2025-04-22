import pandas as pd
import os
os.system('cls')

stores = [
    './database/tienda_1.csv',
    './database/tienda_2.csv',
    './database/tienda_3.csv',
    './database/tienda_4.csv'
]

column = 'Precio'

def total_price(url, column):
    df = pd.read_csv(url)
    total = df[column].sum()
    print(f'{url} → Total {column}: {total}')

# Llama a la función para cada archivo
for store in stores:
    total_price(store, column)
