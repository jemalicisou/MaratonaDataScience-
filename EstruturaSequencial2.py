# Continuação da lista de exercícios Estrutura Sequencial do Python

#11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#  A-  o produto do dobro do primeiro com metade do segundo .
#  B-  a soma do triplo do primeiro com o terceiro.
#  C-  o terceiro elevado ao cubo.


n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

print('')
print('O produto do dobro do primeiro com a metade do segundo é:')
print ('Soma:', ((2*n1) * (n2/2)))

print ('A soma do triplo do primeiro com o terceiro é:')
print ('Produto:', (3 * n1) + n3)

print('O terceiro elevado ao cubo é:')
print ('Cubo:', n3**3)

# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

print('')
peso1 = 72.7
def pesoideal (altura ,peso1):
    return ((peso1 *altura)-58)

print('')
print('Calculo do peso ideal:')

altura= float(input('Insira a sua altura para calcular o peso ideal:'))

print(' O peso ideal é %d:' %pesoideal(altura,peso1))

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('')
pesoh = 72.7
pesom = 62.1

print('Calculo do peso ideal')
sexo = int(input('Informe qual o sexo (1) para homem e (2) para mulher:'))

if sexo == 1:
    alturah = float(input('Digite sua altura:'))
    pesoih = ((72.7 * alturah) - 58)
    print("Seu peso ideal é:", pesoih)
elif sexo == 2:
    alturam = float(input("Digite sua altura:"))
    pesoim = ((62.1 * alturam) - 44.7)
    print("Seu peso ideal é:" ,pesoim)


#14 -João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
#e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print('')

pesopeixe = int(input('Digite quantos kilos de peixe foram pescados:'))
excesso = pesopeixe - 50
multa = excesso * 4

if pesopeixe > 50:
 print (' O excesso de peso foi de ', excesso, 'kg, portanto, a multa é de R$', multa)
else:
 print('A quantidade de peixes pescados está regular!')

