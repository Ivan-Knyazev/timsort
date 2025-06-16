MIN_RUN = 32


def insertion_sort(arr, left, right):
    """Сортирует подмассив arr[left...right] вставками."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    """Сливает два отсортированных подмассива: arr[l...m] и arr[m+1...r]."""
    len1, len2 = m - l + 1, r - m
    left = arr[l: m + 1]
    right = arr[m + 1: r + 1]

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

    print(f"  Слияние блоков [{l}-{m}] и [{m+1}-{r}] завершено.")


def timsort(arr):
    """Основная функция сортировки Timsort с логированием."""
    n = len(arr)
    print(
        f"Начало Timsort для массива из {n} элементов. MIN_RUN = {MIN_RUN}\n")

    # Шаг 1: Сортировка всех `runs` размером MIN_RUN
    print("--- Этап 1: Сортировка начальных серий (runs) ---")
    for i in range(0, n, MIN_RUN):
        end = min((i + MIN_RUN - 1), (n - 1))
        insertion_sort(arr, i, end)
        print(f"Отсортирован run [{i}-{end}]")
    print("\n--- Этап 2: Стратегическое слияние серий ---\n")

    # Шаг 2: Слияние отсортированных `runs`
    size = MIN_RUN
    while size < n:
        print(f"-> Начало итерации слияния. Размер блоков: {size}")
        for start in range(0, n, size * 2):
            mid = min((start + size - 1), (n - 1))
            end = min((start + 2 * size - 1), (n - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2
        print("-" * 40)

    print("Сортировка Timsort завершена.")
    return arr
