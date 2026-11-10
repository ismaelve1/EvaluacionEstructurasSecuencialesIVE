#Ismael Villatoro Elgaz
#Ejercicio 3: Un servidor guarda el tiempo que lleva encendido como una cantidad total de segundos. Escribe un programa que pida esa cantidad (número entero) y muestre a cuántos días, horas, minutos y segundos corresponde.

#
tiempo_segundos = float(input("Introduce el tiempo en segundos: "))

dias = tiempo_segundos / 86400
horas = tiempo_segundos // 3600
minutos = tiempo_segundos // 60
segundos = tiempo_segundos % 60

print(round(dias), "dias")
print(round(horas), "horas")
print(round(minutos), "minutos")
print(round(segundos), "segundos")