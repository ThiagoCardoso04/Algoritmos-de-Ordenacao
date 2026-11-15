import random
import time

# Algoritmo: Quick Sort (Ordenação Rápida)
# Escolhe um "pivô" e reorganiza a lista colocando menores à esquerda e maiores à direita.
# Aplica a mesma lógica recursivamente nas sublistas geradas.

# VANTAGENS:
# 1. Na prática, geralmente é o algoritmo de ordenação mais rápido O(n log n).
# 2. Ordena "in-place", não precisa de grandes arrays extras.

# DESVANTAGENS:
# 1. No pior caso (escolha ruim de pivô), a complexidade cai para O(n²).
# 2. Não é um algoritmo "estável".

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        pivo = lista[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        posicao_pivo = i + 1
        
        quick_sort(lista, inicio, posicao_pivo - 1)
        quick_sort(lista, posicao_pivo + 1, fim)

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio_tempo = time.time()
    quick_sort(lista, 0, len(lista) - 1)
    fim_tempo = time.time()

    print(f"Tempo de execução: {fim_tempo - inicio_tempo:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
