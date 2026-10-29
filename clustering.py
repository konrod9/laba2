"""Простейшая кластеризация по порогу."""


def cluster(values, threshold=0.5):
    """Делит числа на две группы: меньше порога и больше/равно порогу."""
    low = [x for x in values if x < threshold]
    high = [x for x in values if x >= threshold]
    return low, high