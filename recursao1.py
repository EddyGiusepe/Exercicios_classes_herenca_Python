'''
Data Scientist Jr.: Eddy Giusepe Chirinos Isidro

Neste exemplo de recursão aplicaremos o DEBUGGER para entender o passo a passo do tudo o processo.
Link de estudo: https://www.youtube.com/watch?v=CiULVWWscU4
'''
# Exemplo de recursão
def recursao(i):
  print("Recursão")
  i += 1
  if i == 5:
    return
  else:
    recursao(i)

recursao(0)