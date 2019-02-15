# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.

print ('')
print ('Sorteia e separa números pares e ímpares')
import random

lista = []
par = []
impar = []

for i in range (20):
    n = random.randint (1, 100)
    lista.append (n)

    if n % 2 == 0:
        par.append (n)
    else:
        impar.append (n)

lista.sort ()
par.sort ()

impar.sort ()

print ("\nLISTA = ", lista)
print ("PAR   = ", par)
print ("IMPAR = ", impar, "\n")

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

print ('')
print ('Mosta médias maiores que 7,0')

notas = []
soma = 0
media = 0
notasM = 0
for cont in range (10):
    media = 0
    soma = 0
    for cont1 in range (4):
        nota = float (input ("Digite a nota: "))
        soma += nota
    media = soma / 4
    notas.append (media)
    print (notas)
for cont3 in notas:
    if (cont3 >= 7):
        notasM = notasM + str(cont3) + " "
print(notasM)

