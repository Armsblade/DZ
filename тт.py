num = input("Введите число: ")
if len(num) == 1:
    print(f"Вы ввели однозначное число {num}")
elif len(num) == 2:
    print(f"Вы ввели двузначное число {num}")
elif len(num) == 3:
    print(f"Вы ввели трёхначное число {num}")