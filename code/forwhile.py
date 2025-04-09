for i in range(1, 11):
    print(i)

n = int(input("Введите число N: "))
for i in range(1, n+1):
    print(i)

total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print("Сумма:", total)