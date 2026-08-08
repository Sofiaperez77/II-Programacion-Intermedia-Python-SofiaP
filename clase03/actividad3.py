import pandas as pd
df = pd.read_csv("./clase03/Estudiantes.csv", delimiter=";")
print(df.columns)
print(df["Edad"].max())
print(df["Edad"].min())
print(df["Estatura"].max())
print(df["Estatura"].min())