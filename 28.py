# Вводится десятичное число. Реализовать алгоритм его 
# перевода в двоичную систему счисления через рекурсию.
# Нельзя использовать функцию bin()

def func(n) :
    if n == 0 or n == 1:
        return f'{n}'
    return func(n//2) + f'{n%2}'
    
x = int(input("Введите десятичное число: "))
print(func(x))
