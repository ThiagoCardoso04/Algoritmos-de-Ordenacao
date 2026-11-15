import random
import time

# Algoritmo: Merge Sort (Ordenação por Intercalação)
# Usa a estratégia "Dividir para Conquistar". Divide a lista recursivamente ao meio 
# até ter sublistas de 1 elemento, depois mescla essas sublistas de forma ordenada.

# VANTAGENS:
# 1. Desempenho excelente e garantido O(n log n) mesmo no pior caso.
# 2. É um algoritmo "estável" (não muda a ordem de elementos iguais).

# DESVANTAGENS:
# 1. Requer memória extra (O(n)) para criar as sublistas durante a execução.
# 2. A recursão pode ser mais complexa de entender e implementar.

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    merge_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
