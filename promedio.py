lista_notas=[5.0, 6.2, 3.8, 5.2]
cantidad_de_notas=len(lista_notas)
suma=0
#EN CASO DE SUMAR DATOS USAR UNA VARIABLE EN 0.
for nota in lista_notas:
    suma=suma+nota
#esto se ejecuta la veces necesarias, segun la cantidad de datos.
print(f" LA SUMA DE LAS NOTAS ES: {suma}")

promedio= suma/cantidad_de_notas
print(F"EL PROMEDIO ES: {promedio}")