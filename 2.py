def count_common_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_numbers = set1.intersection(set2)
    return len(common_numbers)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
count = count_common_numbers(list1, list2)
print(f"Количество чисел, содержащихся одновременно в обоих списках: {count}")
