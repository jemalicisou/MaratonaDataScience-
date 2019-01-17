# Exercícios Estruturas de Repetição - Parte II




# 1- Faça um programa que imprima na tela os números de 1 a 16, um abaixo do outro.


for i in range (17):
	print (i)

# 2- Depois modifique o programa para que ele mostre os números um ao lado do outro.

print('')
print(list(range(1, 21)))

# 3- Faça um programa que leia 5 números e informe o maior número.

print('')
print('Maior de cinco números')

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))
n4 = int(input('Digite o quarto numero:'))
n5 = int(input('Digite o quinto numero:'))

lista = [n1, n2, n3, n4, n5]
print(max(lista))


# 4- Faça um programa que leia 5 números e informe a soma e a média dos números.

print('')
print('Soma de 5 números e sua média')

nu1 = int(input('Digite o primeiro numero:'))
nu2 = int(input('Digite o segundo numero:'))
nu3 = int(input('Digite o terceiro numero:'))
nu4 = int(input('Digite o quarto numero:'))
nu5 = int(input('Digite o quinto numero:'))

soma = (nu1 + nu2 + nu3 + nu4 + nu5)
print(soma)
media = (soma/5)
print(media)


# 5- Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print('')
print('Números ímpares de 1 a 50')
n = 0

for n in range(1, 51):
    if n % 2 != 0:
        print(n)
print('FIM')


