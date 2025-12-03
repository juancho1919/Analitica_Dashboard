import pandas as pd
df = pd.read_csv("apuestas_online.csv")
class Funciones:
    def __init__(self, df):
        # Recibe directamente un DataFrame ya cargado
        self.df = df

    # 1️ Promedio de monto apostado por juego
    def promedio_monto_por_juego(self):
        promedio = self.df.groupby("Tipo_Juego")["Monto_Apostado"].mean().round(2)
        print("PROMEDIO DE MONTO APOSTADO POR JUEGO:")
        for juego, valor in promedio.items():
            print(f"• {juego}: ${valor}")

    # 2️ Plataforma con mayor ganancia neta total
    def plataforma_mas_rentable(self):
        ganancias = self.df.groupby("Plataforma_Online")["Ganancia_Neta"].sum()
        mejor = ganancias.idxmax()
        print("PLATAFORMA CON MAYOR GANANCIA NETA:")
        print(f"{mejor} → ${round(ganancias[mejor], 2)}")

    # 3️ Región con más apuestas realizadas
    def region_mas_activa(self):
        conteo = self.df["Region_Usuario"].value_counts()
        region = conteo.idxmax()
        print("REGIÓN CON MÁS APUESTAS:")
        print(f"{region} → {conteo[region]} apuestas")

    # 4️ Porcentaje de apuestas ganadas vs perdidas
    def porcentaje_resultados(self):
        total = len(self.df)
        ganadas = (self.df["Resultado"] == "Ganada").sum()
        perdidas = (self.df["Resultado"] == "Perdida").sum()
        print("PORCENTAJE DE RESULTADOS:")
        print(f"• Ganadas: {round(ganadas / total * 100, 2)}%")
        print(f"• Perdidas: {round(perdidas / total * 100, 2)}%")

    # 5️ Apuesta con mayor ganancia neta
    def apuesta_mas_rentable(self):
        idx = self.df["Ganancia_Neta"].idxmax()
        fila = self.df.loc[idx]
        print("APUESTA MÁS RENTABLE:")
        print(f"ID {fila['ID_Apuesta']} → {fila['Tipo_Juego']} en {fila['Plataforma_Online']} → Ganancia: ${fila['Ganancia_Neta']}")

    # 6️⃣ Apuesta con mayor pérdida
    def apuesta_mas_perdida(self):
        idx = self.df["Ganancia_Neta"].idxmin()
        fila = self.df.loc[idx]
        print("APUESTA CON MAYOR PÉRDIDA:")
        print(f"ID {fila['ID_Apuesta']} → {fila['Tipo_Juego']} en {fila['Plataforma_Online']} → Pérdida: ${fila['Ganancia_Neta']}")



df = pd.read_csv("apuestas_online.csv", encoding="utf-8-sig")
funciones = Funciones(df)

funciones.promedio_monto_por_juego()
funciones.plataforma_mas_rentable()
funciones.region_mas_activa()
funciones.porcentaje_resultados()
funciones.apuesta_mas_rentable()
funciones.apuesta_mas_perdida()




