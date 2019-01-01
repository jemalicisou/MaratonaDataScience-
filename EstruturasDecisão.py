# Lista de exercícios Estrutura de Decisões em Python

# 1- Faça um Programa que peça dois números e imprima o maior deles.

print ('')

print ('\nMaior de dois de números:')

n1 = int (input ('Digite um número:'))
n2 = int (input ('Digite outro numero número:'))

if n1 > n2:
    print (n1)

elif n1 < n2:
    print (n2)

# 2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print ('')
print ('Valor positivo ou negativo?')

nu1 = int (input ('Digite um numero:'))

if nu1 > 0:
    print ('Este número é positivo')
elif nu1 < 0:
    print ('Este número é negativo')

# 3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

print ('')
print ('Masculino ou feminino?')

sexo = str (input ('Digite (F)-Feminino, (M)-Masculino: ').upper ())
if sexo == 'M':
    print ('Sexo Masculino.')
elif sexo == 'F':
    print ('Sexo Feminino.')
else:
    print ('Sexo Inválido.')

# 4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print ('')
print (' Verificar se uma letra é vogal ou consoante')
# -*- coding: latin-1 -*
l = str (input ('Digite uma letra: ').lower ())

if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    print ('A letra é uma vogal!')
else:
    print ('A letra é uma consoante!')

# 5- Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:

#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.

print ('')
print ('Calulo da média escolar:')


def media(nota1, nota2):
    return ((nota1 + nota2) / 2)


nota1 = int (input ('Digite a primeira nota:'))
nota2 = int (input ('Digite a segunda nota:'))


if media(nota1,nota2)> 6:
    print('Aprovado!')
elif media(nota1,nota2) == 10:
    print ('Aprovado com distinção!')
else:
    print ('Reprovado')
