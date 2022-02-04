'''
Data Scientist Jr.: Eddy Giusepe Chirinos Isidro

A ideia neste Script é fazer a Leitura de dois valores, fazer a soma e logo mostrar o resultado

Link de estudo: https://www.youtube.com/watch?v=KS2ZCqPAuGY&list=PLZ3V9XyVA52_zzLpYQ6NLkCjLnQU79XOg&index=8
'''

valor1 = 0
valor2 = 0
soma = 0

def leitura():
    print("Digite o valor 1: ")
    global valor1
    valor1 = int(input())
    print("Digite o valor 2: ")
    global valor2
    valor2 = int(input())

def somatorio():
    global soma
    soma = valor1 + valor2

def resultado():
    print("Soma: ", soma)
'''    
Para que o código fique melhor implementado, fazemos:    
'''
if __name__ == "__main__":
    leitura()
    somatorio()
    resultado()
