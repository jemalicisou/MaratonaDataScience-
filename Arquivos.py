#  Faça um programa que leia um arquivo texto contendo uma lista de endereços IP
#  O arquivo de entrada possui o seguinte formato:
#  200.135.80.9
#  192.168.1.1
#  8.35.67.74
#  257.32.4.5
#  85.345.1.2
#  1.2.3.4
#  9.8.234.5
#  192.168.0.256


print('')
print('Cria arquivo com lista de ips:')
arquivo = open('arquivos_ip.txt', 'w')

arquivo.write('200.135.80.9,192.168.1.1,8.35.67.74,257.32.4.5,85.345.1.21.2.3.4,9.8.234.5,192.168.0.256')

