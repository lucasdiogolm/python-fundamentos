'''
texto = input("Informe um texto: ")
# texto = ''
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
    else:
        print() #quebra de linha
        print('Executa no final do laço')
'''

'''
lista = list(range(5, 190, 10))
print(lista)
'''

# Usando While
opcao = -1
while opcao != 0:
    opcao = int(input('[1] Sacar \n [2] Extrato \n [0] Sair \n: '))

    if opcao == 1:
        print('Sacando')
    elif opcao == 2:
        print('Exibindo extrato')
else:
    print('Obrigado por utilizar nossos serviços. Até logo!')