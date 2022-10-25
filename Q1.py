clubs = []

for time in range(3):
    clubs.append(input("Digite os clubes: "))

print("Digite o nome do seu clube para conferir se está na lista! ")
print("*"*26)

x = input("Verifique aqui: ")
if x in clubs:
    print(f"ACHEI! O time {x} foi selecionado. ")
else: 
    print("NÃO ACHEI! O {x}, não foi selecionado. ")