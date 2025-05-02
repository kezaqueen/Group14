def add(a, b):
    answer = a+b
    return answer


def subtract(a, b):
    result= a - b
    return result

def divide(a, b):
    division= a / b
    return division

def modulation(a, b):
    modulated = a % b
    return modulated

def exponation(a, b):
    exponended = a * b
    return exponended

def squaring(a):
    squared = a **2
    return squared

def cubing(a):
    cubed = a ** 3
    return cubed

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

