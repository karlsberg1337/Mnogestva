def find_common_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_numbers = sorted(set1.intersection(set2))
    return common_numbers

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_numbers = find_common_numbers(list1, list2)
print("Числа, которые входят и в первый, и во второй список:")
for number in common_numbers:
    print(number)
