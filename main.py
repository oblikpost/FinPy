import json 
from datetime import datetime, date, timedelta



def menu():
  user_name = input("Qual o seu nome?: ")


  if(len(user_name) < 3 or type(user_name) == "int"):
    print("Nome deve ter no mínimo 3 letras e não deve ser um número")

  print(f"O que quer fazer hoje, {user_name}?")
  print("1. Comprar ativos")
  print("2. Ver meus ativos")

  user_choice = input(": ")

  if(user_choice == "1"): 
    with open("ativos_comprar.json", "r") as f:
      ativos_data = json.load(f)
      print(ativos_data.items())


menu()

































#carteira = []

#ativo_0 = {
 # "ticker":"PETR4",
 # "quantidade":10,
  #"preco_medio":35.50
#}

#carteira.append(ativo_0)

#print(carteira)