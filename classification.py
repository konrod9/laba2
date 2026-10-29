"""Простейшая классификация по порогу."""


def predict(x, threshold=0.5):
    """Возвращает 1, если x >= threshold, иначе 0."""
    return 1 if x >= threshold else 0


def accuracy(y_true, y_pred):
    """Доля правильных ответов."""
    if not y_true:
        return 0.0
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)