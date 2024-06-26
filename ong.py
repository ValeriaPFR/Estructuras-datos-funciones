def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#Se define como productoria a la función de Python que devuelve el resultado de la multiplicación de
# dos o más elementos de una lista
def productoria(lista):
    result = 1
    for num in lista:
        result *= num
    return result
"""Investigación personal: key.startswith es una condición dentro de la instrucción 'if' que indica que la cadena comience con esos caracteres."""
def calcular(**kwargs):
    for key, value in kwargs.items():
        # Verifica si la clave comienza con 'fact_'
        if key.startswith('fact_'):
            n = value
            # Calcula el factorial
            print(f"El factorial de {n} es {factorial(n)}")
        # Verifica si la clave comienza con 'prod_', 
        elif key.startswith('prod_'):
            lista = value
            # Calcula la productoria
            print(f"La productoria de {lista} es {productoria(lista)}")

if __name__ == "__main__":
    # Prueba de funcionamiento del script, de acuerdo a las instrucciones del desafío
    calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)
