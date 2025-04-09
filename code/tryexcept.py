try:
    number = int(input("Введите число: "))
except ValueError:
    print("Это не число!")

try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден!")