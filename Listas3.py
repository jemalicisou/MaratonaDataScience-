# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

print ('')
print ('Mostra soma e a multiplicação')

vetor = []
soma = 0
multiplicacao = 0

for v in range(5):
    v1 = int(input('Digite uma valor inteiro: '))
    vetor.append(v1)

print(vetor)
soma = sum(vetor)
print('A soma dos valores é =', soma)
multiplicacao = (vetor * 2)
print(multiplicacao)



# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

print('')
print('Cria lista com idade e altura')

idade = []
altura =[]

for i in range(5):
    i1 = int(input('Digite a idade: '))
    idade.append(i1)
print('A lista de idade é:', idade)

for a in range(5):
    a1 = float(input('Digite a altura:'))
    altura.append(a1)
print('A lista de altura é:',altura)


idade.reverse()
altura.reverse()
print(idade)
print(altura)

