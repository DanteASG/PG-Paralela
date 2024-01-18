def sumar():
    print("Ejecutando la función sumar()")
    n = int(input("Ingrese la cantidad de números a sumar: "))
    resultado = 0
    for _ in range(n):
        numeros = float(input("Ingrese un número: "))
        resultado += numeros
    return resultado

def restar():
    print("Ejecutando la función restar()")
    n = int(input("Ingrese la cantidad de números a restar: "))
    resultado = float(input("Ingrese el primer número: "))
    for _ in range(1, n):
        numero = float(input("Ingrese un número: "))
        resultado -= numero
    if resultado < 0:
        print("Error de cálculo, resta negativa")
    else:
        return resultado

def multiplicar():
    print("Ejecutando la función multiplicar()")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    resultado = num1 * num2 * num3
    return resultado

def dividir():
    print("Ejecutando la función dividir()")
    numerador = float(input("Ingrese el numerador: "))
    denominador = float(input("Ingrese el denominador: "))
    if denominador == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = numerador / denominador
        return resultado

resultado_suma = sumar()
print(f"Resultado de la suma: {resultado_suma}")

resultado_suma = sumar()
print(f"Resultado de la suma: {resultado_suma}")

resultado_resta = restar()
if resultado_resta is not None:
    print(f"Resultado de la resta: {resultado_resta}")

resultado_multiplicacion = multiplicar()
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")

resultado_division = dividir()
if resultado_division is not None:
    print(f"Resultado de la división: {resultado_division}")
