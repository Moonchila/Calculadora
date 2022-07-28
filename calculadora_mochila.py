resultado=0
r='S'
while r=='S':
    print('-'*4,'CALCULADORA DO MOCHILA','_'*4)
    num1=float(input('Digite um numero: '))
    operacao=str(input('Informe a operacao desejada [+,-,x,/]: ')).strip()
    num2=float(input('Digite um numero: '))
    if operacao == '+':
        resultado=num1+num2
    elif operacao == '-':
        resultado=num1-num2
    elif operacao == 'x':
        resultado=num1*num2
    elif operacao == '/':
        resultado=(num1/num2)
    else:
        print('Operacao Invalida')
    print(f'{resultado:,.10f}')
    r=str(input('Quer continuar [S/N]')).strip().upper()

