
#Importando modulos
from datetime import date
from datetime import time
from datetime import datetime


def ManipulaDataHora():
    hoje = date.today()
    print("Hoje é ",hoje)
    print("Hoje é: ", hoje.day, hoje.month, hoje.year)
    print("Número do dia da semana: ", hoje.weekday())
    dias = ["domingo","segunda", "terca", "quarta", "quinta", "sexta", "sábado"]
    print("Nome do dia da semana: ", dias[hoje.weekday()])

    
    print("Data e Hora: ", datetime.now())

    tempo = datetime.time(datetime.now())
    print("Hora Atual: ", tempo)
ManipulaDataHora()