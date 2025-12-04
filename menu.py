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

#   MENÚ PRINCIPAL

def menu():
    while True:
        print("\n========== MENÚ DE ANÁLISIS ==========")
        print("1 → INFO (estructura del dataset)")
        print("2 → DESCRIBE (estadísticas del dataset)")
        print("3 → Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_info()
        elif opcion == "2":
            mostrar_describe()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta, intenta de nuevo.")

menu()