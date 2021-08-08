from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def deltatempo():
    delta = timedelta(days = 86, hours= 8532, minutes= 7645)
    print(delta)

    hoje = datetime.now()

    print("Data futuro: ", hoje + delta)
    print("Data passado: ", hoje - delta)

deltatempo()