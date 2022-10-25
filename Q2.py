import random
list=[]

for x in range(30):
    X = random.randint(1,15)
    list.append(x)

meu_numero = int(input("Digite um número de 1 à 15: "))
contador = 0
for x in list:
    if x == meu_numero:
        contador += 1
print(f"Eu escolhi o número: {meu_numero}. ")
print(f"Meu número repetiu, {contador} vezes. ")
print(f"Os números sorteados são: {list}")