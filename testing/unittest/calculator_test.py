# Проводим тестирование функции calculator из файла my_tests

# unittest
from unittest import TestCase, main

# my_code
from testing.unittest.calculator_test import calculator


# класс создан для тестирования указаной функции внутри себя
class CalculatorTest(TestCase):

    # функции-тестирования нужно називать с началом test_
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)


if __name__ == "__main__":
    main()
