print("1) Bucle for en Python:")
for numero in range(1, 6):
    print(f"   Iteración {numero}")

print()


def suma(a, b, c):
    return a + b + c


print("2) Función suma con 3 argumentos:")
print(f"   suma(10, 20, 30) = {suma(10, 20, 30)}")

print()

suma_lambda = lambda a, b, c: a + b + c

print("3) Función lambda con la misma funcionalidad:")
print(f"   suma_lambda(10, 20, 30) = {suma_lambda(10, 20, 30)}")

print()

nombre = "Enrique"
lista_nombre = ("Jessica", "Paul", "George", "Henry", "Adán")

print("4) Verificación de nombre en lista:")
print(f"   Nombre buscado: {nombre}")
print(f"   Lista: {lista_nombre}")

if nombre in lista_nombre:
    print(f"   Resultado: El nombre '{nombre}' sí coincide con un valor de la lista.")
else:
    print(f"   Resultado: El nombre '{nombre}' no coincide con ningún valor de la lista.")
