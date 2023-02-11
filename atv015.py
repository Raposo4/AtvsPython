#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar
#sabendo que o carro custa R$60,00 por dfia e R$0,15 por Km rodado.

km = float(input('Quantidade de km rodados: '))
dias = int(input('Quantidade de dias rodados: '))

print(f"O total é pagar é de {(dias*60)+(km*0.15):.2f}")
