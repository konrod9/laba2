"""Простые вычислительные функции."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def average(values):
    if not values:
        return 0.0
    return sum(values) / len(values)