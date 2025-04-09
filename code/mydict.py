student = {"имя": "Иван", "возраст": 19, "курс": 2}
print(student)

d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)

key = "возраст"
if key in student:
    print("Ключ найден:", student[key])
else:
    print("Ключ не найден")