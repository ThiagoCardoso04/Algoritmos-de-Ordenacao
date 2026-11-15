import random
import time

# Algoritmo: Selection Sort (Ordenação por Seleção)
# O Selection Sort divide a lista em duas partes: a parte ordenada (início) e a
# parte não ordenada (resto). A cada iteração, ele busca o menor elemento da
# parte não ordenada e o troca com o primeiro elemento da parte não ordenada.
# Esse processo se repete até que toda a lista esteja ordenada.

# VANTAGENS:
# 1. Fácil de entender e implementar.
# 2. Funciona bem para listas pequenas.
# 3. Baixo consumo de memória (ordenação "in-place", altera a lista no mesmo lugar).
# 4. Realiza o número mínimo de trocas (swaps): no máximo O(n).

# DESVANTAGENS:
# 1. Complexidade de tempo O(n²) em todos os casos (melhor, médio e pior).
# 2. Torna-se ineficiente para listas grandes.
# 3. Não é um algoritmo "estável".

def selection_sort(lista):
    n = len(lista)
    
    # Percorre a lista até o penúltimo elemento
    for j in range(n - 1):
        # Assume que o menor elemento é o atual (primeiro da parte não ordenada)
        min_index = j
        
        # Busca o menor elemento no restante da lista (parte não ordenada)
        for i in range(j + 1, n):
            if lista[i] < lista[min_index]:
                min_index = i
                
        # Se encontrou um elemento menor que o atual, realiza a troca (swap)
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
            
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    selection_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
   
    # print(lista)
