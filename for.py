def loopFor():
    for x in range(5, 10):
        print(x)

loopFor()

print()

def loopArray():
    dias = ["domingo","segunda", "terca", "quarta", "quinta", "sexta", "sábado"]
    for d in dias:
        print(d)

loopArray()

print()

#Funcao Enumerada com valores e indices
def loopEnum():
    dias = ["domingo","segunda", "terca", "quarta", "quinta", "sexta", "sábado"]
    for i, d in enumerate(dias):
        print(i, d)

loopEnum()