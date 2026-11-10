#Ismael Villatoro Elgaz
#Ejercicio 4: Escribe un programa que pida un número entero de tres cifras y muestre:
#Cada una de sus cifras (centenas, decenas y unidades).
#La suma de sus cifras.
#El número invertido, calculado como número (no como texto), de forma que pueda usarse en otras operaciones.

#
numero = float(input("Introduce un número de tres cifras: "))
centenas = numero // 100
decenas = numero // 10 % 10
unidades = numero % 10

print ("centenas:",round(centenas), "decenas:", round(decenas),"unidades", round(unidades))

sumadetodos = centenas + decenas + unidades
print("Suma de las cifras:", round(sumadetodos))

centenas2 = centenas + 0
decenas2 = decenas * 10
unidades2 = unidades * 100

numero2 = centenas2 + decenas2 + unidades2
print("numero invertido", round(numero2))