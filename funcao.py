#funcao básica
def FuncaoSemParametro():
    print("Eu sou uma função")


# Funcao que recebe parametro
def FuncaoComParametro(nome, sobrenome):
    print(nome + " " + sobrenome)

FuncaoComParametro("Igor", "Macedo")


#Funcao que retorna valor
def FuncaoCubo(valor):
    return valor * valor *valor

print(FuncaoCubo(3))

f = FuncaoCubo(5)
print(f)