import random
import time

# Algoritmo: Insertion Sort (Ordenação por Inserção)
# Funciona como organizar cartas de baralho na mão. Pega um elemento por vez e o
# insere na posição correta em relação aos elementos que já estão ordenados.

# VANTAGENS:
# 1. Eficiente para listas pequenas ou que já estão quase ordenadas.
# 2. Baixo consumo de memória (ordenação "in-place").

# DESVANTAGENS:
# 1. Complexidade de tempo O(n²) em todos os casos.
# 2. Ineficiente para listas grandes devido ao alto número de deslocamentos.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    insertion_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
