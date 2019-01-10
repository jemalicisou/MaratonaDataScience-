# Exercícios sobre Strings

# 1- Tamanho de strings. Faça um programa que leia 2 strings e informe o seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento ou diferentes.
#    Compara duas strings
#    String 1: Brasil Hexa 2006
#    String 2: Brasil! Hexa 2006!
#    Tamanho de "Brasil Hexa 2006": 16 caracteres
#    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#    As duas strings são de tamanhos diferentes.
#    As duas strings possuem conteúdo diferente.

print('')
print('Compara duas Strings:')

p1 = len(str(input('Digite uma palavra: ')))
p2 = len(str(input('Digite outra palavra: ')))

if p1 == p2:
    print('As duas Strings possuem o mesmo Tamanho')
elif p1 != p2:
    print('As duas Strings possuem tamanhos diferentes')

# 2 - Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida
# mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao
# informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.


print('')
print('Mostra nome ao contrário:')

nome = str(input('Digite seu nome: ')).upper()
print(nome[::-1])


# 3- Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

#    F
#    U
#    L
#    A
#    N
#    O

print ('')
print ('Mostra nome na vertical:')

nome = str(input('Digite seu nome: ')).upper()

for letter in nome:
    print(letter)

#04 -Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#
#    quantos espaços em branco exintem na frase.
#    quantas vezes aparecem as vogain a, e, i, o, u.'''

print('')
print('Conta a quantidade de vogais e espaços em uma frase:')

cont = 0

dig = input ("informe uma frase: ")
print("Ha '%i' espaços na frase.  " % (dig.count(" ")))

s = dig.count("a") + dig.count("e") + dig.count("i") + dig.count("o") + dig.count("u")
print("Ha '%i' vogais na frase.  " % (s))

#05 - Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
#ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
#A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
#uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

print('')
print('Verifica se a frase é palindromo')

frase = str(input('Digite aqui uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto)-1,-1,-1):
    inverso += junto[c]
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')



