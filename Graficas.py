import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Analitica_Dashboard/apuestas_online.csv')


class Graficas:
    def __init__(self,df):
        self.df = df
        
    def graficas_mostrar(self):
        total_ganancias_por_juego = self.df.groupby('Tipo_Juego')['Ganancia_Neta'].sum()
        total_ganancias_por_plataforma = self.df.groupby('Plataforma_Online')['Ganancia_Neta'].sum()
        total_monto_por_plataforma =self.df.groupby('Plataforma_Online')['Monto_Apostado'].sum()

        fig, axes = plt.subplots(3, 1, figsize=(14, 16))
        

        total_ganancias_por_plataforma.plot(kind='bar', ax=axes[0], title='Ganancias por plataforma')
        axes[0].set_xlabel('Plataforma_Online')
        axes[0].set_ylabel('Ganancia_Neta')

        total_monto_por_plataforma.plot(kind='bar', ax=axes[1], title='Monto por plataforma')
        axes[1].set_xlabel('Plataforma_Online')
        axes[1].set_ylabel('Monto_Apostado')
        
        total_ganancias_por_juego.plot(kind ='pie', ax=axes[2], autopct='%1.1f%%',  title='Ganancias por juego') 
        
        axes [2].set_ylabel('')

        datos = self.df["Ganancia_Neta"]

        # Calcular cuartiles
        q1 = datos.quantile(0.25)
        q2 = datos.quantile(0.50)  
        q3 = datos.quantile(0.75)

        # Crear histograma
        fig, ax = plt.subplots()
        datos.hist(bins=range(int(datos.min()), int(datos.max())+2), ax=ax, color='skyblue', edgecolor='black')

        # Marcar los cuartiles en el gráfico
        for q, color, label in zip([q1, q2, q3], ['red', 'green', 'orange'], ['Q1', 'Mediana', 'Q3']):
            ax.axvline(q, color=color, linestyle='--', linewidth=2, label=f'{label} = {q:.2f}')

        ax.set_xlabel("Ganancia_Neta")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Histograma con cuartiles")
        ax.legend()
        plt.show()




g = Graficas(df)
g.graficas_mostrar()







  














