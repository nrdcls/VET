import random

# Função para ler 10 números e armazená-los em um vetor VET
def ler_numeros():
    VET = []
    print("Digite 10 números:")
    for i in range(10):
        num = int(input())
        VET.append(num)
    return VET

# Função para verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram
def verificar_repetidos(VET):
    repetidos = {}
    for i in range(len(VET)):
        if VET[i] in repetidos:
            repetidos[VET[i]].append(i)
        else:
            repetidos[VET[i]] = [i]
    for num, posicoes in repetidos.items():
        if len(posicoes) > 1:
            print(f"O número {num} se repete nas posições: {posicoes}")

# Função para criar e imprimir uma matriz 10x10 com valores inteiros e randômicos
def criar_matriz():
    matriz = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
    return matriz

# Função para imprimir a soma de todos os valores da matriz
def imprimir_soma(matriz):
    soma = sum(sum(row) for row in matriz)
    print("A soma de todos os valores da matriz é:", soma)

# Função para criar uma nova matriz B, onde cada item seja o valor da matriz A * 3
def criar_matriz_b(matriz):
    matriz_b = [[elemento * 3 for elemento in row] for row in matriz]
    return matriz_b

# Função principal
def main():
    # Ler 10 números e armazenar em um vetor VET
    VET = ler_numeros()
    
    # Verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram
    verificar_repetidos(VET)
    
    # Criar e imprimir uma matriz 10x10 com valores inteiros e randômicos
    matriz_A = criar_matriz()
    print("Matriz A:")
    for row in matriz_A:
        print(row)
    
    # Imprimir a soma de todos os valores da matriz
    imprimir_soma(matriz_A)
    
    # Criar uma nova matriz B, onde cada item seja o valor da matriz A * 3
    matriz_B = criar_matriz_b(matriz_A)
    print("Matriz B (cada item é o valor da matriz A * 3):")
    for row in matriz_B:
        print(row)

if __name__ == "__main__":
    main()
