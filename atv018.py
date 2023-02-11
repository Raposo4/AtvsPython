#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin,cos,tan,radians

ang = float(input(f"Digite o ângulo que você deseja: "))

print(f"O ângulo de {ang} tem o seno de {sin(radians(ang)):.2f}")
print(f"O ângulo de {ang} tem o cosseno de {cos(radians(ang)):.2f}")
print(f"O ângulo de {ang} tem a tangente de {tan(radians(ang)):.2f}")