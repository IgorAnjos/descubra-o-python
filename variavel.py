
#Para declarar uma variável global dentro de function
global variavel

#Variável global
f= 0
print(f)

f = "abc"
print(f)

#Forma de Concatenar
print("Isto é uma string " + str(123))


#Criar Função equivale ao método no c#
#Variável local
def PrimeiraFuncao():
    global f
    f= "def"
    print(f)

PrimeiraFuncao()
print(f)

