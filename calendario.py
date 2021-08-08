import calendar

def Calendariotexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2021, 8)

    print(txtCalendario)

Calendariotexto()

def CalendarioHtml():
    calendarioHtml = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHtml.formatmonth(2021, 8)

    print(htmlCalendario)

CalendarioHtml()