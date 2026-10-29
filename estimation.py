"""Простые статистические оценки."""


def mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)


def median(values):
    if not values:
        return 0.0

    data = sorted(values)
    n = len(data)
    middle = n // 2

    if n % 2 == 1:
        return data[middle]

    return (data[middle - 1] + data[middle]) / 2