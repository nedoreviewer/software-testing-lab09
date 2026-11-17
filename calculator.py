from math import isqrt


class Calculator:
    @staticmethod
    def add(left, right):
        return left + right

    @staticmethod
    def subtract(left, right):
        return left - right

    @staticmethod
    def multiply(left, right):
        return left * right

    @staticmethod
    def divide(left, right):
        if right == 0:
            raise ZeroDivisionError("Деление на ноль")
        return left / right

    @staticmethod
    def is_prime_number(number):
        if type(number) is not int:
            raise TypeError("Ожидается целое число")
        if number < 2:
            return False
        return all(number % divisor for divisor in range(2, isqrt(number) + 1))
