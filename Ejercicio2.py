#Ismael Villatoro Elgaz
#Ejercicio 2: Escribe un programa que pida una temperatura en grados Celsius y la muestre convertida a grados Fahrenheit y a Kelvin.

#pido los grados y leo la variable
grados_celsius = float(input("Introduce la temperatura en ºC: "))

#hago los calculos de farenheit y kelvin
farenheit = (grados_celsius * (9/5)) + 32
kelvin = (grados_celsius + 273.15)

#doy los resultados de farenheit y kelvin
print (grados_celsius, "ºC son", farenheit, "ºF")
print (grados_celsius, "ºC son", kelvin, "ºK")
