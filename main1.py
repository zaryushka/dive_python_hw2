# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


number = int(input('Введите число: '))
def convert(number):
    simbols = '0123456789abcdef'
    result = ''
    while number > 0:
        result = simbols[number % len(simbols)] + result
        number //= len(simbols)
    return result

print(convert(number))

print('Проверка с помощью функции hex: ', hex(int(number)))