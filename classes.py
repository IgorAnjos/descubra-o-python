
#Heranca
#class Signo(nome)

class MinhaClasse():                            #classe sem herança
    def __init__(self):                         #construtor
        self.atributo1 = "Primeiro atributo"    #criando atributo

    def meuMetodo(self):                        #Criando método
        print("Passou pelo meu Metodo")


    def Metodo(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)

def CriarObjeto():
    meuObj = MinhaClasse()
    var1 = meuObj.atributo1
    print(var1)

    meuObj.meuMetodo()

    meuObj.Metodo("Executando um metodo")

CriarObjeto()