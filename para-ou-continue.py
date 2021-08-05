## O break interrompe a execução do loop
def loopBreak():
    for x in range(5, 10):
        if(x == 7):
            break
        print("o valor de x é : ", x)

loopBreak()

print()

## O Continue interrompe uma execução do loop e pula para o próximo item
def loopContinue():
    for x in range(5, 10):
        if(x == 7):
            continue
        print("O valor de x é: ", x)

loopContinue()