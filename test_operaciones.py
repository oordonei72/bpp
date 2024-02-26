import  unittest
import calc.utils.operaciones as operaciones

class PruebasUnitarias(unittest.TestCase):
    def test_areaCirculo(self):
        self.assertEqual(operaciones.areaCirculo(5),78.54)
    def test_areaCuadrado(self):
        self.assertEqual(operaciones.areaCuadrado(5),25)
    def test_volCubo(self):
        self.assertEqual(operaciones.volCubo(5),125)



if __name__=="__main__":

    unittest.main()
