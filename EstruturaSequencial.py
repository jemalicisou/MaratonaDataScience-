# Lista de exercícios Estrutura Sequencial de Python

# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

saudacao = "Alo mundo"
print(saudacao)

# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input("Escreva um número aqui:")
print("O numero escolhido foi:", numero)


# 3- Faça um Programa que peça dois números e imprima a soma.
def sum(num1, num2):
    return num1 + num2


# Atribui valores nas variáveis
print("\tSoma de dois números\n")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

# Imprime resultado na tela
print("")
print("O resultado da soma é %d" % sum(num1, num2))


# 4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media(nota1, nota2, nota3, nota4):
    return ((nota1 + nota2 + nota3 + nota4) / 4)


print("\tMédia das notas Bimestrais\n")
nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota:'))
nota3 = int(input('Digite a terceira nota:'))
nota4 = int(input('Digite a quarta nota:'))

print('')
print("O resultado da média é %d" % media(nota1, nota2, nota3, nota4))


# 5 - Faça um Programa que converta metros para centímetros.
print('')
def convert(nmetro1):
    return ((nmetro1) * 100)


print("\tConversão de metros em centimetros\n")

nmetro1 = float(input('Digite  a quantidade de metros:'))
print('')
print("O resultado em centímetros é: %d" % convert(nmetro1))

# 6-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

Npi= 3.14
def area(Nraio, Npi):
    return ((Npi) * (Nraio ** 2))

print('\tCalculo da area do circulo\n')

Nraio = float(input('Digite o valor do raio:'))
print('')

print("O valor da area é: %d" % area(Nraio, Npi))

# 7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print('')

def qarea (qbase, qaltura):
    return ((qbase * qaltura) * 2)

print('Calculo da area do quadrado:')

qbase = int(input('Digite o valor da base do quadrado ou de um dos lados caso sejam diferentes:'))
qaltura = int(input('Digite o valor da altura do quadrado ou de um dos lados caso sejam diferentes:'))

print('')

print("O valor do dobro area do quadrado é %d:" % qarea(qbase, qaltura))


#8-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.


def salario (qhoras , valorh):
    return (qhoras * valorh)

print('')

print('Definir calculo do salário:')

qhoras = float(input('Insira a quantidade de horas trabalhadas no mês:'))
valorh = float(input('Insira o valor ganho por hora:'))

print('')
print( 'O valor do salário mensal é %d:' %salario(qhoras,valorh))

#9- Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#  C = (5 * (F-32) / 9).

def temperatura (tempf):
    return (5 * (tempf-32)/9)

print('')
print('Definir temperatura em graus Celcius :')

tempf = float(input('Insira a temperatura em Farenheit:'))

print('')
print('O valor da temperatura em graus Celcius é %d:'% temperatura(tempf))


#10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
#  °C × 9/5) + 32 = 32 °F

print('')

def temperaturaf (tempc):
    return ((( tempc * 9 )/5) +32)

print('')
print('Definir temeperatura em graus Farenheit')

tempc = float(input('Insira a temperatura em Celcius:'))

print('')
print('O valor da temperatura em Farenheit é %d:' % temperaturaf(tempc))

