#  Projetos dentro de Estruturas de Decisão em Python

# 1- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
#    do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
#    Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de
#    horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
#    abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#            Salário Bruto: (5 * 220)        : R$ 1100,00
#            (-) IR (5%)                     : R$   55,00
#            (-) INSS ( 10%)                 : R$  110,00
#            FGTS (11%)                      : R$  121,00
#            Total de descontos              : R$  165,00
#            Salário Liquido                 : R$  935,00


print('')
print('Calculo do salário Bruto')

vhora = float(input('Informe o valor recebido por hora :'))
qhora = float(input('Informe a quantidade de horas trabalhadas'))
sbruto = vhora * qhora
fgts = (sbruto * 11) / 100
sind: float = (sbruto * 3) / 100
ir = 0

if sbruto<= 900:
        salario_liquido = (sbruto - sind)
elif sbruto <= 1500:
    ir = (sbruto / 100) * 5
    salario_liquido = sbruto - sind - ir

elif sbruto <= 2500:
    ir = (sbruto / 100) * 10
    salario_liquido = sbruto - sind - ir

else:
    ir = (sbruto / 100) * 20
    salario_liquido = sbruto - sind - ir


print(' O valor do seu salário bruto é %d:' %sbruto)
print(' O valor do seu salário liquido é:%d' %salario_liquido)
print('O imposto sindical foi de %d' %sind)
print("O valor de seu FGTS e de: %d" % fgts)



# ------------------------------------------------------------------------------------------------------------------
# 2 -Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#    se digitar outro valor deve aparecer valor inválido.


print('')
print('Indica o dia correspondente da semana')

dia = int(input('Digite um número de 1 a 7 para indicar os dias da semana, sendo: 1 - Domingo,2 - segunda, etc:'))

if dia == 1:
    print('Hoje é domingo!')
elif dia == 2 :
    print('Hojé é segunda-feira!')
elif dia == 3 :
    print('Hojé é terça-feira!')
elif dia == 4 :
    print('Hojé é quarta-feira!')
elif dia == 5 :
    print('Hojé é quinta-feira!')
elif dia == 6:
    print('Hojé é sexta-feira!')
elif dia == 7:
    print ('Hojé é sábado!')
else:
    print('Valor invalido, digite um número de 1 a 7. ')



# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
#    calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#      Média de Aproveitamento  Conceito

#      Entre 9.0 e 10.0        A
#      Entre 7.5 e 9.0         B
#      Entre 6.0 e 7.5         C
#      Entre 4.0 e 6.0         D
#      Entre 4.0 e zero        E


print('')
print('Cálculo da Média do aluno:')

nota1 = float(input('Insira a primeira nota:'))
nota2 = float(input('Insira a segunda nota:'))
media = ((nota1 + nota2)/2)

if 10 >= media > 9:
    print('Sua media teve um conceito A')
elif 9 >= media > 7.5:
    print('Sua media teve um conceito B')
elif 7.5 >= media > 6.0:
    print('Sua media teve um conceito C')
elif 6.0 >= media > 4.0:
    print('Sua media teve um conceito D')
elif 6 >= media > 0:
    print('Sua media teve um conceito E')




