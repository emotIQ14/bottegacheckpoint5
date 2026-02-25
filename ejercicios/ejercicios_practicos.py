"""Ejercicios prácticos del CheckPoint 5."""


def ejemplo_bucle_for():
    """Muestra un ejemplo simple de bucle for."""
    print("1) Ejemplo de bucle for:")
    for numero in range(1, 6):
        print(f"   Iteración {numero}")
    print()


def suma(a, b, c):
    """Devuelve la suma de tres argumentos."""
    return a + b + c


# Lambda con la misma funcionalidad que la función suma
suma_lambda = lambda a, b, c: a + b + c


def verificar_nombre_en_lista(nombre, lista_nombres):
    """Verifica si un nombre existe en la lista y devuelve un mensaje."""
    if nombre in lista_nombres:
        return f"El nombre '{nombre}' sí coincide con un valor de la lista."
    return f"El nombre '{nombre}' no coincide con ningún valor de la lista."


def main():
    ejemplo_bucle_for()

    print("2) Función suma con 3 argumentos:")
    resultado_suma = suma(10, 20, 30)
    print(f"   suma(10, 20, 30) = {resultado_suma}")
    print()

    print("3) Función lambda con la misma funcionalidad:")
    resultado_lambda = suma_lambda(10, 20, 30)
    print(f"   suma_lambda(10, 20, 30) = {resultado_lambda}")
    print()

    print("4) Verificación de nombre en lista:")
    nombre = "Enrique"
    lista_nombre = ("Jessica", "Paul", "George", "Henry", "Adán")
    print(f"   Nombre buscado: {nombre}")
    print(f"   Lista: {lista_nombre}")
    print(f"   Resultado: {verificar_nombre_en_lista(nombre, lista_nombre)}")


if __name__ == "__main__":
    main()

