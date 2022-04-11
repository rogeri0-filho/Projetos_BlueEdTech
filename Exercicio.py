from time import sleep

salario = float(input('Digite seu salário atual: R$')) #entrada de dados

print('--' * 30)
print('CALCULANDO SEU AUMENTO...')
print('--' * 30)

sleep(2)

print(f'Seu salário anterior era de R${salario}!')

#calculos dos aumentos
if salario <= 280.00:
    print(f'O percentual de aumento aplicado foi de 20%!')
    print(f'O valor aumentado foi de, R${salario * (20/100):.2f}!')
    print(f'Seu salário atual agora é de, R${salario + (salario * (20/100)):.2f}!')

elif salario > 280.00 and salario <= 700.00:
    print(f'O percentual de aumento aplicado foi de 15%!')
    print(f'O valor aumentado foi de, R${salario * (15/100):.2f}!')
    print(f'Seu salário atual agora é de, R${salario + (salario * (15/100)):.2f}!')

elif salario > 700.00 and salario <= 1500.00:
    print(f'O percentual de aumento aplicado foi de 10%!')
    print(f'O valor aumentado foi de, R${salario * (10/100):.2f}!')
    print(f'Seu salário atual agora é de, R${salario + (salario * (10/100)):.2f}!')

elif salario > 1500.00:
    print(f'O percentual de aumento aplicado foi de 5%!')
    print(f'O valor aumentado foi de, R${salario * (5/100):.2f}!')
    print(f'Seu salário atual agora é de, R${salario + (salario * (5/100)):.2f}!')
print('--' * 30)
