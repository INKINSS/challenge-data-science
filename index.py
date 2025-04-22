import pandas as pd
import os
os.system('cls')

stores = [
    './database/tienda_1.csv',
    './database/tienda_2.csv',
    './database/tienda_3.csv',
    './database/tienda_4.csv'
]


def total_price(url):
    df = pd.read_csv(url)
    total = df['Precio'].sum()
    print(f'{url} → Total de Precio: {total}')


for store in stores:
    total_price(store)

#########################################################################


def count_product_by_category(url):
    df = pd.read_csv(url)
    count = df['Categoría del Producto'].value_counts()
    print(f'{url} → Cantidad de productos por categoría: {count}')
    return count


for store in stores:
    count_product_by_category(store)

#########################################################################


def average_qualification(url):
    df = pd.read_csv(url)
    average = df['Calificación'].mean()
    print(f'{url} → Promedio de Calificación: {average}')
    return average


for store in stores:
    average_qualification(store)

#########################################################################


def better_selling_product(url):
    df = pd.read_csv(url)
    count = df['Categoría del Producto'].value_counts()
    print(f'{url} → Productos más vendidos: {count}')
    return count

for store in stores:
    better_selling_product(store)

#########################################################################

def average_shipping_cost(url):
    df = pd.read_csv(url)
    average = df['Costo de envío'].mean()
    print(f'{url} → Promedio de Costo de envío: {average}')
    return average

for store in stores:
    average_shipping_cost(store)

#########################################################################