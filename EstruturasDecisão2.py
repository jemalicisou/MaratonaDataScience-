# Segunda parte da Lista de Exercícios de Estrutura em Decisão de Python

# 6 -Faça um Programa que leia três números e mostre o maior deles.

print ('')
print ('Imprime maior de três números')
n1 = int (input ('Digite o primeiro número:') )
n2 = int (input ('Digite o segundo número:') )
n3 = int (input ('Digite o terceiro número:') )

if n1 > n2 and n1 > n3:
    print (n1)
elif n2 > n1 and n2 > n3:
    print (n2)
elif n3 > n1 and n3 > n2:
    print (n3)

# 7 -Faça um Programa que leia três números e mostre o maior e o menor deles.

print ('')
print (' Imprime maior  e o menor de três números')

nu1 = int (input ('Digite o primeiro número:'))
nu2 = int (input ('Digite o segundo número:'))
nu3 = int (input ('Digite o terceiro número:'))

maior = nu1
menor = nu1

if maior < nu2:
    maior = nu2

if maior < nu3:
    maior = nu3

if menor > nu2:
    menor = nu2

if menor > nu3:
    menor = nu3

print ('Maior:  %d ' % maior)
print ('Menor:  %d ' % menor)

#  8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#  sabendo que a decisão é sempre pelo mais barato.

print ('')
print (' Produto que você deve comprar!')

p1 = int (input ('Digite o preço do primeiro produto:'))
p2 = int (input ('Digite o preço do segundo produto:'))
p3 = int (input ('Digite o preço do terceiro produto:'))

if p1 < p2 and p1 < p3:
    print ('Você deve comprar o primeiro produto no valor de :%d' % p1)
if p2 < p1 and p2 < p3:
    print ('Você deve comprar o segundo produto no valor de :%d' % p2)
if p3 < p1 and p3 < p2:
    print ('Você deve comprar o terceiro produto no valor de :%d' % p3)

# 9 -Faça um Programa que leia três números e mostre-os em ordem decrescente.

print ('')
print (' Ordenando números!')

num1 = int (input ('Digite o primeiro numero:'))
num2 = int (input ('Digite o segundo numero:'))
num3 = int (input ('Digite o terceiro numero:'))

lista_num = [num1, num2, num3]
lista_num_sorted = sorted (lista_num)

print('O numeros digitados foram:', lista_num)
print ('A lista de numeros ordenadas é:',lista_num_sorted)

# 10-Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('')
print('Verifica o turno do estudante.')
turno = str(input( 'Digite (M) Matutino, (V) Verspertino, (N) Noturno ').upper())
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == "N":
    print('Boa Noite!')



