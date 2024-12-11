import unittest

# Импортируем функции, которые будем тестировать
from square import area, perimeter  # Замените 'square' на имя вашего файла

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        # Тест для функции area
        self.assertEqual(area(1), 1)  # Площадь квадрата со стороной 1
        self.assertEqual(area(0), 0)  # Площадь квадрата со стороной 0
        self.assertEqual(area(5), 25)  # Площадь квадрата со стороной 5

    def test_perimeter(self):
        # Тест для функции perimeter
        self.assertEqual(perimeter(1), 4)  # Периметр квадрата со стороной 1
        self.assertEqual(perimeter(0), 0)  # Периметр квадрата со стороной 0
        self.assertEqual(perimeter(5), 20)  # Периметр квадрата со стороной 5

if __name__ == '__main__':
    unittest.main()