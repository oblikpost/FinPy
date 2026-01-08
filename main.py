import json 




def criacao_ativos():
  carteira = []

  ticker_user    =   input("Qual o ticker: ")
  qntd_user      =   input("Qual a quantidade: ")
  prc_medio_user =   input("Preço médio: ")

  

  if(type(ticker_user) == 'int'): 
    print("ticker não pode ser um número")
    
  ativo_user = {
    "ticker": ticker_user,
    "quantidade": qntd_user,
    "preço médio": prc_medio_user
  }

  carteira.append(ativo_user)

  print(carteira)
  print(ativo_user)


criacao_ativos()





#print(type(1))


































#carteira = []

#ativo_0 = {
 # "ticker":"PETR4",
 # "quantidade":10,
  #"preco_medio":35.50
#}

#carteira.append(ativo_0)

#print(carteira)