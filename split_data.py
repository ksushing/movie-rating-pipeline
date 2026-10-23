import pandas as pd
import os
import numpy as np

np.random.seed(42)

# Загрузка
df = pd.read_csv('/movies.csv')

# Перемешиваем
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Размеры
n = len(df)
n_initial = int(n * 0.6)
n_batches = 5
n_batch = (n - n_initial) // n_batches

# Создаём папки
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/incoming', exist_ok=True)

# Исходная часть
initial = df.iloc[:n_initial]
initial.to_csv('data/raw/movies_initial.csv', index=False)

# Порции
for i in range(n_batches):
    start = n_initial + i * n_batch
    end = start + n_batch if i < n_batches - 1 else n
    batch = df.iloc[start:end]
    batch.to_csv(f'data/incoming/batch_{i+1:02d}.csv', index=False)
    print(f'batch_{i+1:02d}.csv: {len(batch)} строк')

print(f'Исходная часть: {len(initial)} строк')
print(f'Всего: {n} строк')
