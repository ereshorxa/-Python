a = 0
b = 0
c = str(input("выберите действие : 1.сложение, 2.вычитание, 3.умножение, 5.деление, 6.целочисленное деление, 7.остаток от деления, 8.возведение в стемень, 9.сравнение, 10.Положительны ли оба числа "))
if c == "1":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ ", a+b)
elif c == "2":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ ", a-b)
elif c == "3":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ ", a*b)
elif c == "5":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ ", a/b)
elif c == "6":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ ", a//b)
elif c == "7":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ ", a%b)
elif c == "8":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите степень числа 2 "))
    print("ваш ответ ", a**b)
elif c == "9":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    print("ваш ответ a==b", a==b)
    print("ваш ответ a!=b", a!=b)
    print("ваш ответ a>b", a>b)
    print("ваш ответ a<b", a<b)
    print("ваш ответ a>=b", a>=b)
    print("ваш ответ a<=b", a<=b)
elif c == "10":
    a = float(input("Напишите число 1 "))
    b = float(input("Напишите число 2 "))
    my_list = [a, b]
    if not (a <= 0 or b <= 0):
        print("Оба числа положительны")
    elif a > 0 or b > 0:
        print("Одно из чисел отрицательно : ")
        print(min(my_list))
    else:
        print("оба числа отрицательные")
else:
    print("всё")