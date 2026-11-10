#Ismael Villatoro Elgaz
#Ejercicio 1: Escribe un programa que pida el precio de un producto sin IVA y muestre el importe del IVA (21 %) y el precio final que debe pagar el cliente.
#con float pregunto el precio sin iva y leo la variable
precio_Sin_IVA = float(input("Ingrese el precio sin IVA: "))

#hago los calculos del iva
resultado_IVA = precio_Sin_IVA * 0.21
print("IVA (21%):", resultado_IVA)

#sumo el iva con el precio original
precio_final = precio_Sin_IVA + resultado_IVA
print("El precio final es: ", precio_final)