import pandas as pd
from statistics import mode

class ApuestasOnline:

    def __init__(self, ruta_csv):
        self.ruta = ruta_csv
        self.df = self.cargar_csv()

    def cargar_csv(self):
        try:
            df = pd.read_csv(self.ruta)
            print(f"CSV cargado correctamente → {len(df)} registros.")
            return df
        except Exception as e:
            print("Error al leer CSV:", e)
            return pd.DataFrame()

    # 1 Promedio de monto apostado por tipo de juego
    def promedio_monto_por_juego(self):
        print("PROMEDIO DE MONTO APOSTADO POR TIPO DE JUEGO:")
        promedio = self.df.groupby("Tipo_Juego")["Monto_Apostado"].mean()
        for juego, valor in promedio.items():
            print(f"• {juego}: ${round(valor, 2)}")

    # 2 Plataforma más usada
    def plataforma_mas_usada(self):
        plataformas = self.df["Plataforma_Online"].dropna().tolist()
        try:
            print("PLATAFORMA MÁS USADA:", mode(plataformas))
        except:
            print("No hay moda (todas diferentes o empate).")

    # 3 Región con mayor ganancia neta total
    def region_mas_rentable(self):
        ganancias = self.df.groupby("Region_Usuario")["Ganancia_Neta"].sum()
        region_max = ganancias.idxmax()
        print("REGIÓN MÁS RENTABLE:")
        print(f"{region_max} → ${round(ganancias[region_max], 2)}")

    # 4 Total de apuestas ganadas por tipo de juego
    def apuestas_ganadas_por_juego(self):
        ganadas = self.df[self.df["Resultado"] == "Ganada"]
        conteo = ganadas["Tipo_Juego"].value_counts()
        print("APUESTAS GANADAS POR TIPO DE JUEGO:")
        for juego, total in conteo.items():
            print(f"- {juego}: {total} ganadas")

    # 5 Primeras 5 apuestas con mayor ganancia
    def top_apuestas_ganancia(self):
        top = self.df.sort_values(by="Ganancia_Neta", ascending=False).head(5)
        print("TOP 5 APUESTAS CON MAYOR GANANCIA:")
        for _, fila in top.iterrows():
            print(f"ID {fila['ID_Apuesta']} → {fila['Tipo_Juego']} en {fila['Plataforma_Online']} → ${fila['Ganancia_Neta']}")

# Crear instancia leyendo el archivo
apuestas = ApuestasOnline('Analitica_Dashboard/apuestas_online.csv')

# Ejecutar los análisis
apuestas.promedio_monto_por_juego()
apuestas.plataforma_mas_usada()
apuestas.region_mas_rentable()
apuestas.apuestas_ganadas_por_juego()
apuestas.top_apuestas_ganancia()
