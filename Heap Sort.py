import random
import time

# Algoritmo: Heap Sort
# Transforma a lista em uma árvore binária (Heap). Remove o maior elemento (raiz) 
# repetidamente, colocando-o no final da lista, e reorganiza o Heap.

# VANTAGENS:
# 1. Complexidade garantida de O(n log n) em todos os casos.
# 2. É "in-place" (usa pouca memória extra).

# DESVANTAGENS:
# 1. É um algoritmo mais difícil de entender e implementar.
# 2. Não é um algoritmo "estável".

def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    heap_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
