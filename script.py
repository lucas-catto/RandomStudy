'''
    Algoritmo que escolhe o que você deve estudar dentro das opções que você oferece, quando se esta indeciso
'''
def FrontEnd():
    # ----------------------------------------------------
    from time import sleep
    # ----------------------------------------------------
    for c in range(0, 60):
        print(":", end="")
        sleep(0.03)
    print()
    # ----------------------------------------------------
    words1 = 'Você está indeciso(a) sobre o que estudar?'

    for c in range(0, len(words1)):
        print(words1[c], end='')
        sleep(0.04)
    print()
    # ----------------------------------------------------
    words2 = 'Eu posso te ajudar!'
    for c in range(0, len(words2)):
        print(words2[c], end="")
        sleep(0.04)
    print()
    # ----------------------------------------------------
    for c in range(0, 60):
        print('=', end="")
        sleep(0.03)
    print()
    # ----------------------------------------------------

# ====================================================================================================

# Aqui é só o back-end, vou fazer um front-end legal depois, mas o 'importante' é essa parte:
def RandomStudy():
    from random import randint

    FrontEnd()

    vetor = []
    
    try:
        amount = int(input("Informe a quantidade de matérias que deseja escolher: "))
    except ValueError or TypeError:
        print("Informe uma quantidade válida!")
    
    cont = 0
    while True:

        cont += 1
        study = str(input(f"Informe o nome da {cont}ª máteria (000 p/ break): "))

        if(study == "000"):
            break
        else:
            vetor.append(study)


    choose = []
    # Se o número de escolhas informado for maior que o número de matérias.
    if(amount >= len(vetor)):
        for c in vetor:
            choose.append(c)
    # Se não for, sorteia normal.
    else:
        for c in range(0, amount):
            choose.append(vetor[randint(0, len(vetor))]) #


    return choose

# ====================================================================================================
print(RandomStudy())
# ====================================================================================================
