def count_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
unique_count = count_unique_numbers(numbers)
print(f"Количество различных чисел: {unique_count}")
