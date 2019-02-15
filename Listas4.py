# Faça um programa que simule um lançamento de dados. Lance o dado 20 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função
# para gerar numeros aleatórios, simulando os lançamentos dos dados.

print('')
print('Simula o lançamento de dados: ')

import random

vetor =[]
for d in range(20):
    d1 = random.randint(1, 6)
    vetor.append(d1)

print(vetor)

print("O numero de vezes que o numero 1 foi sorteado foi:", vetor.count(1))
print("O numero de vezes que o numero 2 foi sorteado foi:", vetor.count(2))
print("O numero de vezes que o numero 3 foi sorteado foi:", vetor.count(3))
print("O numero de vezes que o numero 4 foi sorteado foi:", vetor.count(4))
print("O numero de vezes que o numero 5 foi sorteado foi:", vetor.count(5))
print("O numero de vezes que o numero 6 foi sorteado foi:", vetor.count(6))


