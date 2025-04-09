import random

secret = random.randint(0, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Угадайте число (от 0 до 10): "))
    if guess == secret:
        print("Поздравляю! Вы угадали!")
        break
    elif guess < secret:
        print("Неверно! Загаданное число больше.")
    else:
        print("Неверно! Загаданное число меньше.")
    attempts -= 1

if attempts == 0:
    print("Увы, вы проиграли. Загаданное число было", secret)
