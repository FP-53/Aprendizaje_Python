"""DATES"""

from datetime import datetime

""" Importamos datetimes que es la biblioteca que nos permite acceder a fechas"""

#creamos una fecha 

now = datetime.now()

# aqui estamos sacando varias funciones de nuestra variable "now" o varios datos en especifico, estas funciones son parte del diccionario datatime
print('año',now.year)
print('mes',now.month)
print('dia',now.day)
print('hora',now.hour)
print('minuto',now.minute)
print('segundo',now.second)

#si se coloca solamente now se sacan los datos en en general, no uno en especial
print(now)

#es otro formato o forma de representar una fecha, es mas facil para enviar y transmitir fechas por este metodo 
timestamp = now.timestamp()

print('timestamp: ', timestamp)

#crear una fecha
year_2025 = datetime(year=2025, month=1, day=1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

print_date(year_2025)
#si se define un año lo minimo necesario es el año, mes y dia, otros datos que falten por defecto los considera 0 

from datetime import time 
# datetime usa hora en general contando año, mes, dia, hora, minuto, segundo y time se refiere a solamente hora, minuto y segundo 


current_time = time(5,36,23)
#time necesita tener los datos necesarios para poder devoler datos por consola, si no se colocan los datos se interpreta como 0
#los valores deben ser en su equivalente, es decir minutos no puede ser mayor a 59 y horas no puede ser mayor a 24

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print(current_time)

from datetime import date
#date es el opuesto a time, este solamente utiliza año, mes y dia 

current_date = date(2007,5,9)

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(current_date)

current_date = date.today()
print(current_date)

#se pueden realizar operaciones co las fechas mientras no superen los limites 
print(current_date.month - 1)

#para restar fecas u horas debes hacerlo dentro de una variable 

diff= year_2025.date() - current_date 
#necesitas especificar que la variable 'year_2025' restaras el date para evitar errores 
print(diff)

diff = year_2025 - now 
print(diff)

#diff = year_2025.time - current_time
# si o posee un time predefinido o los 3 valores son iguales a 0 no se pueden realizar operaciones 

from datetime import timedelta
#nos sire para traajar diferencias horarias 
init_timedelta = timedelta(200,100,100, weeks= 10)
end_timedelta = timedelta(300,100,100, weeks= 13)

print(init_timedelta - end_timedelta)

#timedelta se puede usar para restar dias, semanas, etc etc en casos como pueden ser controlar los  dias trabajados o similares 
#aqui al definir semanas, las semanas se convierten en dias
#se usan para restar periodos de tiempo, no se da una fecha como tal si no que se usa una cantidad de dias, semanas, horas, etc