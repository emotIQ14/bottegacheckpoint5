"""Pruebas básicas para los ejercicios prácticos."""

import unittest

from ejercicios.ejercicios_practicos import (
    LISTA_NOMBRE,
    contiene_nombre,
    contiene_nombre_con_for,
    mensaje_coincidencia,
    suma,
    suma_lambda,
)


class TestEjerciciosPracticos(unittest.TestCase):
    def test_suma(self) -> None:
        self.assertEqual(suma(1, 2, 3), 6)
        self.assertEqual(suma(-1, 0, 5), 4)

    def test_suma_lambda(self) -> None:
        self.assertEqual(suma_lambda(1, 2, 3), 6)
        self.assertEqual(suma_lambda(10, 20, 30), 60)

    def test_contiene_nombre_con_in(self) -> None:
        self.assertFalse(contiene_nombre("Enrique", LISTA_NOMBRE))
        self.assertTrue(contiene_nombre("Henry", LISTA_NOMBRE))

    def test_contiene_nombre_con_for(self) -> None:
        self.assertFalse(contiene_nombre_con_for("Enrique", LISTA_NOMBRE))
        self.assertTrue(contiene_nombre_con_for("Henry", LISTA_NOMBRE))

    def test_mensaje_coincidencia(self) -> None:
        self.assertIn("sí coincide", mensaje_coincidencia("Henry", True))
        self.assertIn("no coincide", mensaje_coincidencia("Enrique", False))


if __name__ == "__main__":
    unittest.main()
