num, num1, num2 = int(input("Введите первое число: ")), int(input("Введите первое число: ")), int(input("Введите третье число: "))


if num == num1 and num2 == num and num1 == num2:
    print("3")
elif num != num1 or num == num1 and num1 == num2 or num1 != num2 and num == num2 or num != num2:
    print("2")
elif num != num1 and num2 != num and num1 != num2:
    print("0")

# years = []
# for year in range(0, 3000):
#     years.append(year)
#     year = int()
#
# def years_v(year_imp):
#     year_imp = input("Введите год: ")
#     if year_imp in years:
#         if year % 10 == 4:
#             print("v")
#         else:
#             print("a")
#
# years_v()


