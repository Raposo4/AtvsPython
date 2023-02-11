#Faça um exercício que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

sal = float(input('Qual o salário do funcionário?R$: '))

print(f"Um funcionário que ganhava {sal}, com 15% de aumento receberá {sal+(sal*15/100):.2f}")