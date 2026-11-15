import random
import time

# Algoritmo: Radix Sort
# Ordena os números dígito por dígito, começando pelo menos significativo (unidade) 
# até o mais significativo. Usa o Counting Sort como sub-rotina em cada dígito.

# VANTAGENS:
# 1. Muito rápido para números inteiros e grandes volumes de dados.
# 2. Supera algoritmos de comparação como Quick e Merge Sort.

# DESVANTAGENS:
# 1. Só funciona para números inteiros.
# 2. Requer memória extra O(n).

def counting_sort_radix(lista, exp):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10

    for i in range(n):
        indice = lista[i] // exp
        contagem[indice % 10] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        indice = lista[i] // exp
        saida[contagem[indice % 10] - 1] = lista[i]
        contagem[indice % 10] -= 1
        i -= 1

    for i in range(n):
        lista[i] = saida[i]

def radix_sort(lista):
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(lista, exp)
        exp *= 10
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    radix_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
