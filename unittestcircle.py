import math
import unittest

# Импортируем функции, которые будем тестировать ,
from circle import area, perimeter  # Замените 'circle' на имя вашего файла

class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        # Тест для функции area
        self.assertAlmostEqual(area(1), math.pi)  # Площадь круга с радиусом 1
        self.assertAlmostEqual(area(0), 0)        # Площадь круга с радиусом 0
        self.assertAlmostEqual(area(2), math.pi * 4)  # Площадь круга с радиусом 2

    def test_perimeter(self):
        # Тест для функции perimeter
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)  # Периметр круга с радиусом 1
        self.assertAlmostEqual(perimeter(0), 0)            # Периметр круга с радиусом 0
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)  # Периметр круга с радиусом 2

if __name__ == '__main__':
    unittest.main()