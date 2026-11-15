import random
import time

# Algoritmo: Bucket Sort (Ordenação por Baldes)
# Divide a lista em um número de "baldes" (sub-listas). Distribui os elementos 
# para os baldes, ordena cada balde individualmente e depois concatena tudo.

# VANTAGENS:
# 1. Muito rápido para dados uniformemente distribuídos.
# 2. Complexidade média O(n + k).

# DESVANTAGENS:
# 1. Desempenho depende da distribuição dos dados (se mal distribuídos, fica lento).
# 2. Precisa de memória extra para criar os baldes.

def bucket_sort(lista):
    if not lista:
        return lista
    
    num_baldes = 10
    max_val = max(lista)
    baldes = [[] for _ in range(num_baldes)]

    for num in lista:
        indice = int(num * num_baldes / (max_val + 1))
        baldes[indice].append(num)

    for i in range(num_baldes):
        baldes[i].sort()

    lista.clear()
    for balde in baldes:
        lista.extend(balde)
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    bucket_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
