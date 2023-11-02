num = int(input("Введите первое число: "))
num1 = int(input("Введите второе число: "))
num2 = int(input("Введите третье число: "))

list_num = []

list_num.append(num); list_num.append(num1); list_num.append(num2)
list_num.sort()
for n in list_num:
    print(f"{n}\n")