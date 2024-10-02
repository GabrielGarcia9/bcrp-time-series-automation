# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import plotly.offline as pyo 
import plotly.graph_objects as go

def visualizar_box_plot(data, titulo):
    data_sorted = data.sort_values(by='year')
    fig = px.box(data_sorted, y='value', color='year', title=titulo)
    fig.show()

def visualizar_line_plot(data, titulo):
    fig = px.line(data, y='value', labels={'value': '', 'fecha': 'Fecha'}, title=titulo)
    fig.show()

def visualizar_comparacion_anual(data):
    data_pivot = data.groupby(['value_month', 'year'])['value'].aggregate('mean').unstack()
    fig = px.line(data_pivot, x=data_pivot.index, y=data_pivot.columns,
                  title="Comparación de la media aritmética mensual para Cada Año",
                  labels={'value_month': 'Mes', 'year': 'Año', 'value': 'Valor'},
                  markers=True, line_dash_sequence=["solid", "dot", "dash"])
    fig.show()


# def visualizar_datos_combinados(data):
#     fig, axes = plt.subplots(2, 2, figsize=(15, 6))

#     # Histograma acumulativo
#     sns.histplot(data['value'], edgecolor="white", cumulative=True, color='#1F618D', bins=20, ax=axes[0, 0])
#     axes[0, 0].set_title('Histograma Acumulativo')

#     # Histograma regular
#     sns.histplot(data['value'], edgecolor="white", bins=20, ax=axes[0, 1])
#     axes[0, 1].set_title('Histograma Regular')

#     # Gráficos de series temporales en la segunda fila
#     axes[1, 0].plot(data['value'], alpha=0.5, linestyle='-', label='input')
#     axes[1, 0].plot(data['value'].resample('BA').mean(), linestyle=':', label='resample')
#     axes[1, 0].plot(data['value'].asfreq('BA'), linestyle='--', label='asfreq')
#     axes[1, 0].legend(loc='upper left')
#     axes[1, 0].set_title('Series Temporales')

#     fig.delaxes(axes[1, 1])

#     plt.tight_layout()
#     plt.show()