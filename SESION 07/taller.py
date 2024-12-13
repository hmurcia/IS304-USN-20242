"""
ejercicio solicita crear un programa que genere una lista con los números del 1 al 100, pero sustituyendo ciertos valores por palabras específicas:

Los múltiplos de 3 deben ser reemplazados por "fizz".
Los múltiplos de 5 deben ser reemplazados por "buzz".
Los múltiplos de 3 y de 5 a la vez deben ser reemplazados por "fizzbuzz".
"""

def fizzbuzz():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)
    return result

# Llamada a la función y mostrar la lista
fizzbuzz_list = fizzbuzz()
print(fizzbuzz_list)
#append= aregamos 
# result= lista
# % divisor de 3 y 5
