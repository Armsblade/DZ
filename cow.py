a = True
while a:

    cow_list = []
    for cow in range(100):
        cow_list.append(cow)

    cow_num = int(input("Введите число коров: "))

    if cow_num in cow_list and cow_num == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif cow_num in cow_list and cow_num <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif cow_num in cow_list and cow_num <= 20:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 2 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 2 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 2 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 3 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 3 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 3 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 4 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 4 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 4 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 5 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 5 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 5 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 6 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 6 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 6 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 7 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 7 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 7 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 8 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 8 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 8 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif (cow_num % 100) // 10 == 9 and cow_num % 10 == 1:
        print(f"На лугу пасётся {cow_num} корова")
    elif (cow_num % 100) // 10 == 9 and cow_num % 10 <= 4:
        print(f"На лугу пасётся {cow_num} коровы")
    elif (cow_num % 100) // 10 == 9 and cow_num % 10 <= 9:
        print(f"На лугу пасётся {cow_num} коров")

    elif cow_num == 100:
        print(f"На лугу пасётся {cow_num} коров")

    elif cow_num != cow_list:
        print("нет такого числа в списке")
        break