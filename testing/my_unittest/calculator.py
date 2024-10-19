# Библиотека Unittest для Тестрирования Кода
# Успешные Тесты - ето гарантия и доказательство, что написаный код правильный и рабочий


# функция калькулятор, которая принимает агрумент строку, где есть и числа и математическая операция которую нужно выполнить с ними
def calculator(expression: str):
    # содержит допустимые операции + - / * с числами внутри текущей функции
    allowed = "+-/*"
    # если нету ни одного разрешеного знака в переданом аргументе, тогда выбрасываем ошибку
    # sign ето математическая разрешеная операция "+-/*"
    if not any(sign in expression for sign in allowed):
        raise ValueError(
            f"Expression must have at least one allowed math operator {allowed}"
        )

    for sign in allowed:
        if sign in expression:
            try:
                # делим весь переданый аргумент по математическому знаку "+-/*" на два числа
                left, right = expression.split(sign)
                left, right = int(left), int(right)

                if sign == "+":
                    return left + right
                elif sign == "-":
                    return left - right
                elif sign == "*":
                    return left * right
                elif sign == "/":
                    return left / right
            except (ValueError, TypeError):
                raise ValueError(
                    f"Expression must have two integer numbers and one math operator {allowed}"
                )


if __name__ == "__main__":
    print(calculator("10-3"))
