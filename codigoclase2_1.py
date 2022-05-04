from ipaddress import summarize_address_range
from prueba import *
import unittest

class TestSumaPosNeg(unittest.TestCase):
    def test_1(self):
        resultado = suma_valorespos_yneg([-80,20,-20,30])
        self.assertEqual(resultado,(50,-100))

class TestPotencia(unittest.TestCase):
    def test_1(self):
        resultado = potencia(3,4)
        self.assertEqual(resultado,81)

class TestPares(unittest.TestCase):
    def test_1(self):
        resultado = pares([3,4,5,6])
        self.assertEqual(resultado,[4,6])

class TestNumerosNegativos(unittest.TestCase):
    def test_1(self):
        resultado = numerosnegativos([3,-4,-5,6,-8,9,90,1,2,-67])
        self.assertEqual(resultado,[-4,-5,-8,-67])



if __name__ == '__main__':
    unittest.main()