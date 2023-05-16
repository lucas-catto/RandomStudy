'''
    Algoritmo que escolhe o que você deve estudar dentro das opções que você oferece, quando se esta indeciso
'''

# Aqui é só o back-end, vou fazer um front-end legal depois, mas o 'importante' é essa parte:
def RandomStudy():
    from random import randint

    vetor = []

    print("=" * 60)
    
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

print(RandomStudy())
