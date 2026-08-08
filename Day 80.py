from collections import Counter


def find_unique_letters(str1, str2):
    count1 = Counter(str1)
    count2 = Counter(str2)

    unique_letters = count1 - count2

    result = []
    for char, count in unique_letters.items():
        result.extend([char] * count)

    return result


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

unique_letters = find_unique_letters(str1, str2)

print("Letters in the first string but not in the second string:", unique_letters)