import matplotlib.pyplot as plt
import pandas as pd


def generate_chart():
    # Leer los datos del CSV
    data = pd.read_csv('ventas_pan.csv')

    # Agrupar los datos por el tipo de pan más vendido
    grouped_data = data.groupby('Pan mas vendido').sum()

    # Crear las etiquetas y los valores para el gráfico
    labels = grouped_data.index
    values = grouped_data['Cantidad vendida']

    # Crear el gráfico de barras
    plt.bar(labels, values)

    # Añadir títulos y etiquetas
    plt.title('Panes más vendidos en 50 panaderías de Medellín')
    plt.xlabel('Tipo de pan')
    plt.ylabel('Cantidad vendida')

    plt.savefig('panes_mas_vendidos.png')
    plt.close()
