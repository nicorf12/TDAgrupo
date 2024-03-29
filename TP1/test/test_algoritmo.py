from unittest import TestCase

from TP1 import algoritmo


class Test(TestCase):
    def test_minimizar_suma_10(self):
        resultado = 309600
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/10.txt"))[0])

    def test_minimizar_suma_50(self):
        resultado = 5218700
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/50.txt"))[0])

    def test_minimizar_suma_100(self):
        resultado = 780025365
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/100.txt"))[0])

    def test_minimizar_suma_1000(self):
        resultado = 74329021942
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/1000.txt"))[0])

    def test_minimizar_suma_5000(self):
        resultado = 1830026958236
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/5000.txt"))[0])

    def test_minimizar_suma_10000(self):
        resultado = 7245315862869
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/10000.txt"))[0])

    def test_minimizar_suma_100000(self):
        resultado = 728684685661017
        self.assertEqual(resultado, algoritmo.minimizar_suma(algoritmo.leer_archivo("../archivos/100000.txt"))[0])