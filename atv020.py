#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteadas

from random import shuffle

x = []
while len(x) != 4:
    x.append(input('Digite o nome do aluno: '))
shuffle(x)
print(f"A ordem sorteada foi {x}")
