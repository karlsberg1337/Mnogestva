sequence = input("Введите последовательность чисел через пробел: ")
numbers = sequence.split()
seen_numbers = set()
for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)
