#usei série de pagamentos


def depositos():
    idade = int(input("digite a sua idade: "))
    idade_futura = int(input("digite a idade de resgate: "))
    vf = float(input("digite o valor que deseja resgatar: "))
    #tx. juros
    i = float(input("qual a taxa de juros: "))

    while True:

        mensal_anual = int(input("1 - para juros mensais\n2 - para jutos anuais\nDigite o número da opção: "))

        if mensal_anual == 1:

            #tempo de aplicação mensal
            t = (idade_futura - idade)*12
            break

        if mensal_anual == 2:

            t = (idade_futura - idade)
            break

    #fórmula da série de pagamentos
    depositos = (vf*( i/ ( ((1+i)**t) - 1) ))
    print("Precisa fazer depósitos periódicos de: R$ {}".format(round(depositos)))
    return depositos


depositos()