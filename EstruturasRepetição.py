# Exercícios de Estrutura de Repetição
# #1-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.
#
print('')
print('Valida a nota do aluno:')
while True:
 nota = float(input("Digite uma nota entre 0 e 10: "))
 if nota >= 0 and nota <= 10:
     print('A nota é válida!')
     break
 else:
     print ("A nota digitada é inválida!")

# #2 -Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

print('')
print('Valida senha')




while True:
    user = str (input ('Insira um nome de usuário:'))
    senha = str (input ('Insira uma senha:'))
    if user != senha:
        print('A Senha escolhida foi registrada com sucesso!')
        break
    else:
        print ('A senha não pode ser igual ao nome de usuário, favor digitar outra senha!')





