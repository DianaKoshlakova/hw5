# Вводится десятичное число. Реализовать алгоритм его 
# перевода в двоичную систему счисления через рекурсию.
# Нельзя использовать функцию bin()

def func(n) :
    if n == 0 :
        return result
    result.insert(0, n%2)
    func(n//2)
    
x = int(input("Введите десятичное число: "))
func(x)
result = []
for i in result :
    print(i, end='')
