def main():
    import os
    from src.init import inicio as init
    lista = init()
    x = 0
    while x != 11:
        x = int(input("\nQual operação desejas fazer:\n1= Mediana\n2= Media\n3= Moda\n4= Amplitude\n5= Quartil\n6= Variância\n7= Desvio Padrão\n8= Coeficiente de Variação\n9= Histograma\n10= Box Plot\n11= Sair do programa\n"))
        if x == 1:
            os.system("cls || clear")
            from src.matematicas import mediana
            print(mediana(lista))

        elif x == 2:
            os.system("cls || clear")
            from src.matematicas import media
            print(media(lista))

        elif x == 3:
            os.system("cls || clear")
            from src.matematicas import moda
            print(moda(lista))

        elif x == 4:
            os.system("cls || clear")
            from src.matematicas import amplitude
            print(amplitude(lista))

        elif x == 5:
            from src.matematicas import quartil
            x = quartil(lista)
            os.system("cls || clear")
            if len(x) == 3:
                print("\nMediana da lista da esquerda (Q1)",x[0])
                print("Mediana geral (Q2)",x[1])
                print("Mediana da lista da direita (Q3)",x[2],"\n")
            else:
                print("\nMediana da lista da esquerda (Q1)",x[0])
                print("Mediana da lista da direita (Q3)",x[1],"\n")
        elif x == 6:
            from src.matematicas import varianciaamostral, varianciapop
            os.system("cls || clear")
            amostral = varianciaamostral(lista)
            pop = varianciapop(lista)
            print("Variância Populacional =",pop,"\nVariância Amostral =",amostral)

        elif x == 7:
            from src.matematicas import desvio_padraopop, desvio_padraoamostral
            os.system("cls || clear")
            amostral = desvio_padraoamostral(lista)
            pop = desvio_padraopop(lista)
            print("Desvio Padrão Populacional =",pop,"\nDesvio Padrão Amostral =",amostral)

        elif x == 8:
            from src.matematicas import coeficientevariacaoamostral, coeficientevariacaopop
            os.system("cls || clear")
            pop = coeficientevariacaopop(lista)
            amostral = coeficientevariacaoamostral(lista)
            print("Coeficiente de Variação Populacional =",pop,"\nCoeficiente de Variação Amostral =",amostral)
        
        elif x == 9:
            os.system("cls || clear")
            from src.matematicas import histograma
            histograma(lista)
        elif x == 10:
            os.system("cls || clear")
            from src.matematicas import boxplot
            boxplot(lista)
        else:
            os.system("cls || clear")
            print("A operação inserida não é válida. Por favor, tente novamente.")
    os.system("cls || clear")
main()