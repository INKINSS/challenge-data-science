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
    average = df['Costo de envío'].mean()
    result.append((store, average))

# separa nombres y valores

store_name = [nombre for nombre, _ in result]
values = [valor for _, valor in result]

# colores para la grafica
colors = cm.tab10(np.linspace(0, 1, len(values)))
fig, ax = plt.subplots()

labels = [f"${v/1e3:,.2f}K".replace('.', ',') for v in values]

# grafica de barras
bars = ax.bar(store_name, values, color=colors)

ax.bar_label(bars, labels=labels)

ax.set_title('Costo de envío promedio')
ax.set_ylabel('Costo de envío promedio')
plt.show()
