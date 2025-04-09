num = int(input("Введите число: "))
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

a = int(input("Первое число: "))
b = int(input("Второе число: "))
print("Большее число:", max(a, b))

age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Вы можете получить права.")
else:
    print("Вы пока не можете получить права.")