import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np
import os
os.system('cls')

stores = [
    ('./database/tienda_1.csv', 'Tienda 1'),
    ('./database/tienda_2.csv', 'Tienda 2'),
    ('./database/tienda_3.csv', 'Tienda 3'),
    ('./database/tienda_4.csv', 'Tienda 4')
]

result = []

for url, store in stores:
    df = pd.read_csv(url)
    average = df['Calificación'].mean()
    result.append((store, average))

# separa nombres y valores
store_name = [nombre for nombre, _ in result]
values = [valor for _, valor in result]

# genera colores personalizados por tienda
colors = cm.tab10(np.linspace(0, 1, len(values)))

# gráfico circular
plt.figure(figsize=(5, 5))
plt.pie(
    values,
    labels=store_name,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.4),
    pctdistance=.8,
)
plt.title('Promedio de Calificación por Tienda')
plt.axis('equal')  # para que el círculo no quede ovalado
plt.show()
