n = int(input("Введите число n: "))

# Вывод чисел от n до 1
print(f"Числа от {n} до 1:")
current = n
while current >= 1:
    print(current, end=' ')
    current -= 1
print()

# Вычисление факториала
factorial = 1
counter = 1
while counter <= n:
    factorial *= counter
    counter += 1

print(f"Факториал числа {n}: {factorial}")