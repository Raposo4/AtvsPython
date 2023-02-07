#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que 
#cada litro de tinta pinta uma área de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

print(f"Sua parede tem dimensão de {larg}x{alt} e sua área é de {larg*alt}m².")
print(f"Para pintar essa parede, você precisará de {larg*alt/2}L de tinta.")
