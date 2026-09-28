total_excelente = 0
total_ruim = 0

for i in range(1, 51):
    print(f" Entrevistado {i}")
    nome = input("Nome: ")
    idade = input("Idade: ")
    opiniao = int(input("Nota (1-Excelente, 2-Bom, 3-Ruim): "))

    if opiniao == 1:
        total_excelente = total_excelente + 1
    elif opiniao == 3:
        total_ruim = total_ruim + 1

print("\n--- Resultado da pesquisa ---")
print(f"Quantidade de notas Excelentes: {total_excelente}")
print(f"Quantidade de notas Ruins: {total_ruim}")
