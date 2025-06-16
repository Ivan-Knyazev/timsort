import time
import random

from timsort import timsort

data = [random.randint(0, 10000) for _ in range(10000)]

# Тест встроенной функции
data1 = data.copy()
start_time = time.time()
sorted_builtin = sorted(data1)
end_time = time.time()
print(f"Встроенный sorted(): {end_time - start_time:.6f} секунд")

# Тест написанной реализации
data2 = data.copy()
start_time = time.time()
sorted_custom = timsort(data2)
end_time = time.time()
print(f"Ручной Timsort: {end_time - start_time:.6f} секунд")
