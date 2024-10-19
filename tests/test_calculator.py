# Проводим тестирование функции calculator из файла my_tests
# python -m unittest tests.test_calculator

# unittest
from unittest import TestCase, main

# my_code
from testing.my_unittest.calculator import calculator


# класс создан для тестирования указаной функции внутри себя
class CalculatorTest(TestCase):

    # функции-тестирования нужно називать с началом test_
    def test_plus(self):
        self.assertEqual(calculator("2+2"), 4)

    def test_minus(self):
        self.assertEqual(calculator("5-2"), 3)

    def test_multi(self):
        self.assertEqual(calculator("4*4"), 16)

    def test_devide(self):
        self.assertEqual(calculator("10/2"), 5.0)

    # проверка, если пользователь не передал ни один арифметическйи знак
    def test_no_signs(self):
        # assertRaises провека на вызвалось ил указаное исключение
        with self.assertRaises(ValueError) as my_raise:
            calculator("ashd")

        # my_raise.exception.args[0] хранит текст вызваного исключения
        self.assertEqual(
            "Expression must have at least one allowed math operator +-/*",
            my_raise.exception.args[0],
        )

    # проверка, если пользователь передал два арифметических знака
    def test_two_signs(self):
        with self.assertRaises(ValueError) as my_raise:
            calculator("1+2+3")

        self.assertEqual(
            "Expression must have two integer numbers and one math operator +-/*",
            my_raise.exception.args[0],
        )


if __name__ == "__main__":
    main()
