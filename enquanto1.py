# contador = 1
#
# while contador <= 5:
#     print("mensagem", contador)
#     contador += 1

# Aqui vamos a calcular a média de 5 números:
# Link de estudo: https://www.youtube.com/watch?v=FIgBqW0S2eE&list=PLZ3V9XyVA52_zzLpYQ6NLkCjLnQU79XOg&index=9
contador = 1
nota = 0
soma = 0
media = 0
while contador <= 5:
    print("Digite a sua nota: ", contador)
    nota = float(input())
    soma = soma + nota
    contador += 1
print("Soma: ", soma)
media = soma / 5
print("Média: ", media)
