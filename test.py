mixed_array = ['f', '1', 'b', '2', 'c', '3', 'd', '4', '2.5']

def check_type(mixed_array):
    letters = []
    numbers = []

    for item in mixed_array:
        try:
            num = float(item)
            numbers.append(num)
        except ValueError:
            letters.append(item)

    return letters, numbers

letters, numbers = check_type(mixed_array)

print("Буквы:", letters)
print("Числа:", numbers)

def test_son():
    assert check_type(["f", "b", "c", "d"]) == (["f", "b", "c", "d"], [])

    # Тест 2: Только числа
    assert check_type(["1", "2", "3", "4", "2.5"]) == ([], [1.0, 2.0, 3.0, 4.0, 2.5])

    # Тест 3: Смесь букв и чисел
    assert check_type(["f", "1", "b", "2", "c", "3", "d", "4", "2.5"]) == (
    ["f", "b", "c", "d"], [1.0, 2.0, 3.0, 4.0, 2.5])

    # Тест 4: Пустой список
    assert check_type([]) == ([], [])

    # Тест 5: Некорректные вводные данные (символы, которые не являются ни буквами, ни цифрами)
    assert check_type(["!", "@", "#", "$", "%"]) == (["!", "@", "#", "$", "%"], [])
