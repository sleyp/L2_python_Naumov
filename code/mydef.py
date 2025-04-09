def add(a, b):
    return a + b
print(add(3, 5))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

def average(lst):
    return sum(lst) / len(lst)
print(average([1, 2, 3, 4, 5]))