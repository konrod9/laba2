# machine_learning_lib

Учебная библиотека с простыми функциями машинного обучения.

## Файлы

- `classification.py` — классификация по порогу.
- `regression.py` — простая регрессия через среднее значение.

## Запуск

Пример:

```python
from classification import predict, accuracy
from regression import predict as reg_predict, mse

print(predict(0.7))          # 1
print(accuracy([1, 0], [1, 0]))  # 1.0