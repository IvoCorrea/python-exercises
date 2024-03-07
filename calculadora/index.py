numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))
operacao = input('Escolha uma operação(Soma, divisão, multiplicação): ')
if operacao == 'soma':
    print(f'O resultado da soma foi {numero1 + numero2}')

elif operacao == 'divisao':
    print(f'O resultado da divisão foi {numero1 / numero2}')

elif operacao == 'multiplicaçao':
    print(f'O resultado da multiplicação foi {numero1 * numero2}')  