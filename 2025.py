import pandas as pd

dados = pd.read_excel("2025.xlsx", sheet_name="aaa")
dados = dados.rename(columns={"Empenhado": "Projetado"})
dados = dados.rename(columns={"Credor": "Quem Recebeu"})
