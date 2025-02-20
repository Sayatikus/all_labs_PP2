def square_of_numbers(N):  
    for num in range(N + 1):
        yield num ** 2  # Возвращает квадрат числа

N = int(input("Введите число: "))  # Читаем число
gen = square_of_numbers(N)  # Исправлено название функции

for i in gen:
    print(i)  # Вывод квадрата каждого числа от 0 до N