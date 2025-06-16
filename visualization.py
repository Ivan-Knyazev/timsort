import matplotlib.pyplot as plt
import random

from timsort import MIN_RUN, insertion_sort, merge


def full_timsort_for_plot(arr):
    """Полная процедура Timsort для получения финального результата."""
    n = len(arr)
    for i in range(0, n, MIN_RUN):
        end = min((i + MIN_RUN - 1), (n - 1))
        insertion_sort(arr, i, end)

    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = min((start + size - 1), (n - 1))
            end = min((start + 2 * size - 1), (n - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2
    return arr

# ----- Функции для визуализации -----


def plot_array(arr, title, filename):
    plt.figure(figsize=(12, 7))
    plt.bar(range(len(arr)), arr, color='skyblue', width=1.0)
    plt.title(title, fontsize=16)
    plt.xlabel("Индекс")
    plt.ylabel("Значение")
    plt.xlim(-1, len(arr))
    plt.ylim(0, max(arr) * 1.05)
    plt.savefig(filename)
    plt.close()
    print(f"Изображение сохранено как {filename}")


# ----- Основной процесс -----
n_elements = 128
data = [random.randint(10, 100) for _ in range(n_elements)]

# 1. Исходное состояние
plot_array(data, "Рис. 1. Исходное состояние массива",
           "timsort_step_0_initial.png")

# 2. После сортировки `runs`
temp_data_runs = data.copy()
for i in range(0, n_elements, MIN_RUN):
    end = min((i + MIN_RUN - 1), (n_elements - 1))
    insertion_sort(temp_data_runs, i, end)
plot_array(temp_data_runs, "Рис. 2. Массив после сортировки всех `runs`",
           "timsort_step_1_runs_sorted.png")

# 3. После первого этапа слияния
temp_data_merge = temp_data_runs.copy()
size = MIN_RUN
for start in range(0, n_elements, size * 2):
    mid = min((start + size - 1), (n_elements - 1))
    end = min((start + 2 * size - 1), (n_elements - 1))
    if mid < end:
        merge(temp_data_merge, start, mid, end)
plot_array(temp_data_merge, "Рис. 3. Результат первого этапа слияния",
           "timsort_step_2_first_merge.png")

# 4. Финальное состояние
timsort_final_data = data.copy()
sorted_data = full_timsort_for_plot(timsort_final_data)
plot_array(sorted_data, "Рис. 4. Финальное состояние — отсортированный массив",
           "timsort_step_3_final_CORRECTED.png")
