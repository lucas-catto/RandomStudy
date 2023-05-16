
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
    


FrontEnd()

