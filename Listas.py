# Ecercícios sobre Listas

# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
print('')
print('Cria lista de cinco números')

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
n4 = int(input('Digite um numero:'))
n5 = int(input('Digite um numero:'))

list = [n1, n2, n3, n4, n5]
print(list)

# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

print('')
print('Mostra de lista de 10 elementos ao inverso')
nu1 = int(input('Digite um numero:'))
nu2 = int(input('Digite um numero:'))
nu3 = int(input('Digite um numero:'))
nu4 = int(input('Digite um numero:'))
nu5 = int(input('Digite um numero:'))
nu6 = int(input('Digite um numero:'))
nu7 = int(input('Digite um numero:'))
nu8 = int(input('Digite um numero:'))
nu9 = int(input('Digite um numero:'))
nu10 = int(input('Digite um numero:'))

list2 = [nu1, nu2, nu3, nu4, nu5, nu6, nu7, nu8, nu9, nu10]
list2.reverse()
print(list2)


# 3- Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


print('')
print('Mostra a media das notas:')
nota1 = int(input('Digite uma nota'))
nota2 = int(input('Digite outra nota:'))
nota3 = int(input('Digite outra nota:'))
nota4 = int(input('Digite outra nota:'))


lista_nota = [nota1, nota2, nota3, nota4]
soma_nota= (nota1 + nota2+ nota3+ nota4)
media_nota = (soma_nota/4)

print(lista_nota)
print(media_nota)


