"""Простейшая регрессия: предсказание средним значением."""


def mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)


def predict(_x, train_y):
    """Для любого x возвращает среднее значение train_y."""
    return mean(train_y)


def mse(y_true, y_pred):
    """Среднеквадратичная ошибка."""
    if not y_true:
        return 0.0
    return sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)