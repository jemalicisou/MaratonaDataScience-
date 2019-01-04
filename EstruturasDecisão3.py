# Terceira parte da lista de exercícios de Estrutura de Decisão

#2-Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
#(resto da divisão).

print('')
print('Determina se o número é par ou impar')

numero = int(input('Insira aqui um número inteiro:'))

if(numero % 2 == 0):
    print("O número é par!")
else:
    print("Número é ímpar!")



#3-Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
#arredondamento.

print('')
print('Determina se um número é inteiro ou decimal')

n1 = float(input('Digite um número :'))

if(n1 % 100 == 0):
    print("O número é inteiro.")
else:
    print("O número é decimal")







