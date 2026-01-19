import unittest

from ClaseContacto import clase_contacto
from ClaseGestor import clase_gestor


class TestClaseGestor(unittest.TestCase):
    def test_registrar_contacto(self):
        m = clase_gestor()
        c = clase_contacto("Ana", "123", "ana@mail.com", "Calle 1")
        self.assertTrue(m.agregar_contacto(c))

    def test_buscar_por_telefono(self):
        m = clase_gestor()
        m.agregar_contacto(clase_contacto("Ana", "123", "ana@mail.com", "Calle 1"))

        encontrado = m.buscar_telefono("123")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.get_nombre(), "Ana")


if __name__ == "__main__":
    unittest.main()
