import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Analitica_Dashboard/apuestas_online.csv')


class Graficas:
    def __init__(self,df):
        self.df = df
        
    def mostrar(self):
        print(self.df)
        print(self.df.head(2))
    
    def grafica_circulo(self):
        total_ganancias_por_juego = self.df.groupby('Tipo_Juego')['Ganancia_Neta'].sum()
        total_ganancias_por_plataforma = self.df.groupby('Plataforma_Online')['Ganancia_Neta'].sum()

        fig, axes = plt.subplots(2, 1, figsize=(8, 8))

        total_ganancias_por_plataforma.plot(kind='bar', ax=axes[0], title='Ganancias por plataforma')
        axes[0].set_xlabel('Plataforma_Online')
        axes[0].set_ylabel('Ganancia_Neta')

        total_ganancias_por_juego.plot(kind ='pie', ax=axes[1], autopct='%1.1f%%',  title='Ganancias por juego') 
        
        axes [1].set_ylabel('')

        plt.tight_layout()
        plt.show()






g = Graficas(df)
g.grafica_circulo()






    


  














