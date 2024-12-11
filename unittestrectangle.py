# unittestrectangle.py
import unittest
from rectangle import area, perimeter  # Импортируем функции из rectangle.py

class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(10, 5), 50)  # Площадь прямоугольника 10x5
        self.assertEqual(area(0, 5), 0)    # Площадь прямоугольника 0x5
        self.assertEqual(area(10, 0), 0)   # Площадь прямоугольника 10x0

    def test_perimeter(self):
        self.assertEqual(perimeter(10, 5), 30)  # Периметр прямоугольника 10x5
        self.assertEqual(perimeter(0, 5), 10)   # Периметр прямоугольника 0x5
        self.assertEqual(perimeter(10, 0), 20)  # Периметр прямоугольника 10x0

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area("a", 5)  # Передача строки вместо числа
        with self.assertRaises(TypeError):
            perimeter(10, "b")  # Передача строки вместо числа

if __name__ == '__main__':
    unittest.main()