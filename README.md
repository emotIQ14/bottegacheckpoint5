# CheckPoint 5 - Entrega Práctica (Python)

Este repositorio contiene la parte práctica de la asignación del CheckPoint 5.

## Contenido

- `ejercicios/ejercicios_practicos.py`: resolución de los ejercicios prácticos solicitados.
- `tests/test_ejercicios_practicos.py`: pruebas automáticas básicas con `unittest`.
- `docs/`: carpeta preparada para añadir la documentación teórica en PDF posteriormente.

## Ejercicios prácticos incluidos

1. Bucle `for` en Python.
2. Función `suma(a, b, c)` que recibe 3 argumentos y devuelve su suma.
3. Función `lambda` con la misma funcionalidad de suma.
4. Verificación de si un nombre existe en una lista de nombres.

## Cómo ejecutar

```bash
python3 ejercicios/ejercicios_practicos.py
```

## Cómo ejecutar las pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Criterios de calidad aplicados

- Código organizado en funciones reutilizables.
- Tipado básico (`type hints`) para mejorar legibilidad.
- Verificación del ejercicio de nombres con `in` y con `for in`.
- Pruebas automáticas para validar resultados.

## Nota sobre la documentación teórica

Las respuestas a las preguntas teóricas no están incluidas en este repositorio por ahora, ya que serán añadidas posteriormente en formato PDF dentro de la carpeta `docs/`.
