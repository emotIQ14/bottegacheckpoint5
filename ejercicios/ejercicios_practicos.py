"""Ejercicios prácticos del CheckPoint 5."""

from typing import Callable, Iterable


NOMBRE_BUSCADO = "Enrique"
LISTA_NOMBRE = ("Jessica", "Paul", "George", "Henry", "Adán")


def ejemplo_bucle_for(inicio: int = 1, fin: int = 5) -> None:
    """Muestra un ejemplo simple de bucle for."""
    print("1) Ejemplo de bucle for:")
    for numero in range(inicio, fin + 1):
        print(f"   Iteración {numero}")
    print()


def suma(a: int, b: int, c: int) -> int:
    """Devuelve la suma de tres argumentos."""
    return a + b + c


# Lambda con la misma funcionalidad que la función suma (requisito del ejercicio)
suma_lambda: Callable[[int, int, int], int] = lambda a, b, c: a + b + c


def contiene_nombre(nombre: str, lista_nombres: Iterable[str]) -> bool:
    """Verifica con el operador `in` si un nombre existe en la colección."""
    return nombre in lista_nombres


def contiene_nombre_con_for(nombre: str, lista_nombres: Iterable[str]) -> bool:
    """Verifica con un bucle `for in` si un nombre existe en la colección."""
    for nombre_lista in lista_nombres:
        if nombre_lista == nombre:
            return True
    return False


def mensaje_coincidencia(nombre: str, existe: bool) -> str:
    """Construye el mensaje final de coincidencia."""
    if existe:
        return f"El nombre '{nombre}' sí coincide con un valor de la lista."
    return f"El nombre '{nombre}' no coincide con ningún valor de la lista."


def main() -> None:
    """Ejecuta y muestra todos los ejercicios prácticos."""
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
    existe_con_in = contiene_nombre(NOMBRE_BUSCADO, LISTA_NOMBRE)
    existe_con_for = contiene_nombre_con_for(NOMBRE_BUSCADO, LISTA_NOMBRE)
    print(f"   Nombre buscado: {NOMBRE_BUSCADO}")
    print(f"   Lista: {LISTA_NOMBRE}")
    print(f"   Resultado con 'in': {mensaje_coincidencia(NOMBRE_BUSCADO, existe_con_in)}")
    print(f"   Resultado con 'for in': {mensaje_coincidencia(NOMBRE_BUSCADO, existe_con_for)}")


if __name__ == "__main__":
    main()
