def bubble_sort(vetor):

    #uso essa variável pra descobrir o tamanho do vetor
    fim = len(Vetor)

    #isso pq a variavel fim vai diminuir em função dos elementos ordenados dentro do vetor
    #
    while fim > 0:

        i = 0
        #anadando no vetor de 0 até o fim
        #
        while i < fim-1:
            #se o meu elemento "i" for maior que o próximo(i+1) eu troco os elementos de de posição

            if vetor[i] > vetor[i+1]
                #variável auxiliar pra armazenar o vetor
                #realizar a troca de posição
                temp = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = temp
                print(vetor)
            i += 1
        #decrementa o fim pois sabemos que sempre o último elemento está ordenado
        fim -= 1

def merge_sort(v, p, r):
    #caso a pessoa não saiba o tamonho o do vetor podmeos cacular
    if p < r :
        q = (p+r) // 2 #posição do elemento do meio , # usa o // pra pegar o valor inteiro
        #usamos recursão
        #quebra o vetor em dois metade direita (1) e metade esquerda (2)
        merge_sort(v,p,q)
        merge_sort(v, q+1, r)
        merge(v,p,q,r)

def merge(v,p,q,r):
    auxiliar = v.copy()
    #contador vetor esquerda (1) e direita(2)
    i = p # (1)
    j = q+1 # (2)
    k = p #contador vetor original

    while k<= r:
        if i > q: #quando acabar os elementos do vetor esquedo (1)

            v[k] =temp[j]
            j += 1

        elif j > r : #quando acaba os elementos do vetor direito (2)

            v[k] = temp[i]
            i += 1

        elif temp[i <= temp[j]:
            #retira o elemento do vetor da esquerda (1)
            v[k] = temp[i]
            i += 1

        else:
            #tira o elemento do vetor direito (2)
            v[k] = temp[j]
            j += 1

        k += 1