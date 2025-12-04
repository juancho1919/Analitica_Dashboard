import pandas as pd

#   CARGA DE INFORMACIÓN (CON TU RUTA)

df = pd.read_csv('Analitica_Dashboard/apuestas_online.csv')
print(df)

#   FUNCIONES DE INFO Y DESCRIBE

def mostrar_info():
    print("\n========== INFO DEL DATASET ==========")
    print("Columnas:", list(df.columns))
    print("\nTotal de registros:", len(df))
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nValores faltantes por columna:")
    print(df.isna().sum())


def mostrar_describe():
    print("\n========== DESCRIBE DEL DATASET ==========")
    print(df.describe())

    print("\n=== ESTADÍSTICAS EXTRA ===")
    print("Monto total apostado:", df["Monto_Apostado"].sum())
    print("Ganancia total neta:", df["Ganancia_Neta"].sum())
    print("Promedio apostado:", df["Monto_Apostado"].mean())

    print("\nFrecuencia por tipo de juego:")
    print(df["Tipo_Juego"].value_counts())

    print("\nFrecuencia por plataforma:")
    print(df["Plataforma_Online"].value_counts())

    print("\nFrecuencia por región:")
    print(df["Region_Usuario"].value_counts())

    print("\nResultados (Ganó / Perdió):")
    print(df["Resultado"].value_counts())

def llamar_promedio(apuestas):
    apuestas.promedio_monto_por_juego()

def llamar_plataforma(apuestas):
    apuestas.plataforma_mas_usada()

def llamar_region(apuestas):
    apuestas.region_mas_rentable()

def llamar_apuestas_ganadas(apuestas):
    apuestas.apuestas_ganadas_por_juego()

def llamar_top(apuestas):
    apuestas.top_apuestas_ganancia()


# ====== MENÚ PRINCIPAL ======
import pandas as pd
from funciones import ApuestasOnline
def menu():
    # Crear instancia de la clase
    apuestas = ApuestasOnline('Analitica_Dashboard/apuestas_online.csv')

    while True:
        print("\n========== MENÚ DE ANÁLISIS ==========")
        print("1 → INFO (estructura del dataset)")
        print("2 → DESCRIBE (estadísticas del dataset)")
        print("3 → Promedio de monto por juego")
        print("4 → Plataforma más usada")
        print("5 → Región más rentable")
        print("6 → Apuestas ganadas por juego")
        print("7 → Top 5 apuestas con mayor ganancia")
        print("8 → mostrar graficas")
        print("0 → Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_info()
        elif opcion == "2":
            mostrar_describe()
        elif opcion == "3":
            llamar_promedio(apuestas)
        elif opcion == "4":
            llamar_plataforma(apuestas)
        elif opcion == "5":
            llamar_region(apuestas)
        elif opcion == "6":
            llamar_apuestas_ganadas(apuestas)
        elif opcion == "7":
            llamar_top(apuestas)
        elif opcion == "8":
            from Graficas import Graficas
            g = Graficas(df)
            g.graficas_mostrar()    
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta, intenta de nuevo.")

menu()