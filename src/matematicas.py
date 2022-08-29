def mediana(lista):
    #import statistics
    #return statistics.median(lista)
    lista.sort()
    elementos = len(lista)
    if not elementos % 2 == 0:
        x = elementos // 2
        return lista[x]
    elif elementos % 2 == 0:
        x = elementos // 2
        conta = (lista[x-1] + lista [x]) / 2
        return conta

def media(lista):
    #import statistics
    #return statistics.mean(lista)
    x = len(lista)
    y = sum(lista)
    return y / x

def moda(lista):
    #import statistics
    #return statistics.multimode(lista)
    from collections import Counter
    from itertools import groupby
    from operator import itemgetter
    counts = Counter(iter(lista)).most_common()
    maxcount, mode_items = next(groupby(counts, key=itemgetter(1)), (0, []))
    return list(map(itemgetter(0), mode_items))

def amplitude(lista):
    return max(lista) - min(lista)

def quartil(lista):
    #import statistics
    #return statistics.quantiles(lista, n=4)
    lista.sort()
    if len(lista) % 2 == 0:
        tamanho = len(lista)
        metade = tamanho // 2
        comeco = lista[:metade]
        fim = lista[metade:]

        print(comeco, fim)
        resposta = []
        resposta.append(mediana(comeco))
        resposta.append(mediana(fim))
        return resposta
    elif len(lista) % 2 != 0:
        tamanho = len(lista)
        metade = tamanho // 2
        comeco = lista[:metade]
        fim = lista[1 + metade:]
        meio = mediana(lista)

        print(comeco, meio, fim)
        resposta = []
        resposta.append(mediana(comeco))
        resposta.append(meio)
        resposta.append(mediana(fim))
        return resposta

def varianciapop(lista):
    #import statistics
    #return statistics.pvariance(lista) # [Populacional]
    listatemp = []
    medialista = media(lista)
    for i in range(len(lista)):
        x = (lista[i] - medialista) ** 2
        listatemp.append(x)

    populacional = sum(listatemp) / (len(lista))
    return populacional # [Populacional]

def varianciaamostral(lista):
    #import statistics
    #return statistics.variance(lista) # [Amostral]
    listatemp = []
    medialista = media(lista)
    for i in range(len(lista)):
        x = (lista[i] - medialista) ** 2
        listatemp.append(x)

    amostral = sum(listatemp) / (len(lista) - 1)
    return amostral # [AmostraL]

def desvio_padraopop(lista):
    #import statistics
    #return statistics.pstdev(lista) # [Populacional]
    return varianciapop(lista) ** 0.5

def desvio_padraoamostral(lista):
    #import statistics
    #return statistics.stdev(lista) # [Amostral]
    return varianciaamostral(lista) ** 0.5

def coeficientevariacaopop(lista):
    #from scipy.stats import variation 
    #return variation(lista) * 100
    return (desvio_padraopop(lista) / media(lista)) * 100

def coeficientevariacaoamostral(lista):
    return (desvio_padraoamostral(lista) / media(lista)) * 100

def histograma(lista):
    from matplotlib import pyplot as plt
    import numpy as np
    marks = np.array(lista)
    fig, axis = plt.subplots(figsize =(10, 5))
    axis.hist(marks, bins = [0, 2, 4, 6, 8, 10]) # alterar de acordo com os dados
    return plt.show()

def boxplot(lista):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.boxplot(lista)
    return plt.show()