import math

# Завдання 1
def task1():
    nums = [float(input(f"Введіть число {i+1}: ")) for i in range(3)]
    results = [num**2 if num >= 0 else num**4 for num in nums]
    print("Результати:", results)

# Завдання 2
def task2():
    x1, y1 = float(input("Введіть x1: ")), float(input("Введіть y1: "))
    x2, y2 = float(input("Введіть x2: ")), float(input("Введіть y2: "))
    dist_a = math.sqrt(x1**2 + y1**2)
    dist_b = math.sqrt(x2**2 + y2**2)
    if dist_a < dist_b:
        print("Точка A ближче до початку координат.")
    elif dist_a > dist_b:
        print("Точка B ближче до початку координат.")
    else:
        print("Точки A і B знаходяться на однаковій відстані від початку координат.")

# Завдання 3
def task3():
    angle1 = float(input("Введіть величину першого кута: "))
    angle2 = float(input("Введіть величину другого кута: "))
    angle3 = 180 - angle1 - angle2
    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник існує і він прямокутний.")
        else:
            print("Трикутник існує і він не прямокутний.")
    else:
        print("Трикутник не існує.")

# Завдання 4
def task4():
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))
    if x < y:
        x, y = (x + y) / 2, x * y * 2
    else:
        y, x = (x + y) / 2, x * y * 2
    print("Результати: x =", x, "y =", y)

# Завдання 5
def task5():
    x = float(input("Введіть координату x: "))
    y = float(input("Введіть координату y: "))
    if x == 0 and y == 0:
        print("Точка знаходиться на початку координат.")
    elif x == 0:
        print("Точка знаходиться на осі Y.")
    elif y == 0:
        print("Точка знаходиться на осі X.")
    elif x > 0 and y > 0:
        print("Точка знаходиться в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка знаходиться в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка знаходиться в третьому квадранті.")
    else:
        print("Точка знаходиться в четвертому квадранті.")

# Завдання 6
def task6():
    a = int(input("Введіть ціле число a: "))
    b = int(input("Введіть ціле число b: "))
    if a != b:
        if a > b:
            b = a
        else:
            a = b
    else:
        a = b = 0
    print("Результати: a =", a, "b =", b)

# Завдання 7
def task7():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    negative_count = sum(1 for num in [a, b, c] if num < 0)
    print("Кількість негативних чисел:", negative_count)

# Завдання 8
def task8():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    positive_count = sum(1 for num in [a, b, c] if num > 0)
    print("Кількість додатних чисел:", positive_count)

# Завдання 9
def task9():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    integer_count = sum(1 for num in [a, b, c] if num.is_integer())
    print("Кількість цілих чисел:", integer_count)

# Завдання 10
def task10():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))
    k = int(input("Введіть число k: "))
    divisible = [num for num in [a, b, c] if num % k == 0]
    print("Число k є дільником чисел:", divisible)

# Викликаємо всі завдання по черзі
task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()