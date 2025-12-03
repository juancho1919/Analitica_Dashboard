import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Analitica_Dashboard/apuestas_online.csv')


class Graficas:
    def __init__(self,df):
        self.df = df
        self.dt = pd.read_csv('Analitica_Dashboard/apuestas_online.csv')
    
    
    import pandas as pd
    def leer(self):
        print(self.dt)


    
        

    def mostrar(self):
        print(self.df)
        print(self.df.head(2))






g = Graficas(df)
g.mostrar()
g.leer()





    


  














