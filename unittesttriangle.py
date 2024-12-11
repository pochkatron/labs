import unittest

# Импортируем функции, которые будем тестировать
from triangle import area, perimeter  # Замените 'triangle' на имя вашего файла

class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        # Тест для функции area
        self.assertEqual(area(10, 5), 25)  # Площадь треугольника с основанием 10 и высотой 5
        self.assertEqual(area(0, 5), 0)    # Площадь треугольника с основанием 0 и высотой 5
        self.assertEqual(area(10, 0), 0)   # Площадь треугольника с основанием 10 и высотой 0

    def test_perimeter(self):
        # Тест для функции perimeter
        self.assertEqual(perimeter(3, 4, 5), 12)  # Периметр треугольника со сторонами 3, 4, 5
        self.assertEqual(perimeter(0, 4, 5), 9)   # Периметр треугольника со стороной 0
        self.assertEqual(perimeter(3, 0, 5), 8)   # Периметр треугольника со стороной 0
        self.assertEqual(perimeter(3, 4, 0), 7)   # Периметр треугольника со стороной 0

if __name__ == '__main__':
    unittest.main()