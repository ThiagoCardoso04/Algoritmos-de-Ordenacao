import random
import time

# Algoritmo: Counting Sort (Ordenação por Contagem)
# Não compara elementos. Conta a frequência de cada número na lista e usa essa 
# contagem para calcular a posição exata de cada elemento na lista final.

# VANTAGENS:
# 1. Extremamente rápido O(n + k), sendo linear.
# 2. Ideal para listas com números inteiros de intervalo pequeno.

# DESVANTAGENS:
# 1. Só funciona para números inteiros.
# 2. Consome muita memória se o maior valor da lista for muito grande.

def counting_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    contagem = [0] * (max_val + 1)
    
    for num in lista:
        contagem[num] += 1
        
    for i in range(1, len(contagem)):
        contagem[i] += contagem[i - 1]
        
    saida = [0] * len(lista)
    for i in range(len(lista) - 1, -1, -1):
        num = lista[i]
        saida[contagem[num] - 1] = num
        contagem[num] -= 1
        
    for i in range(len(lista)):
        lista[i] = saida[i]
    return lista

if __name__ == "__main__":
    lista = []
    for _ in range(100000):
        lista.append(random.randint(0, 100000))

    inicio = time.time()
    counting_sort(lista)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    print("\nPrimeiros 100 elementos:", lista[:100])
    print("Últimos 100 elementos:", lista[-100:])
    
    # print(lista)
