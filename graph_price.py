import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
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
    total = df['Precio'].sum()
    result.append((store, total))

store_name = [nombre for nombre, _ in result]
values = [valor for _, valor in result]

colors = cm.tab10(np.linspace(0, 1, len(values)))

fig, ax = plt.subplots()

bars = ax.bar(store_name, values, color=colors)

# Formatea valores a millones con separador coma y símbolo $
labels = [f"${v/1e6:,.2f}M".replace('.', ',') for v in values]

ax.bar_label(bars, labels=labels)

ax.set_title('Ventas Totales')
ax.set_ylabel('Total de ventas')
plt.show()
