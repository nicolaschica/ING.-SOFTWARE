# Calculadora Básica - Versión completa

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: División por cero"
    return num1 / num2

print("\nOperaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("\nElige una operación (1-4): ")

print()
if opcion == "1":
    print(f"Resultado: {sumar(num1, num2)}")
elif opcion == "2":
    print(f"Resultado: {restar(num1, num2)}")
elif opcion == "3":
    print(f"Resultado: {multiplicar(num1, num2)}")
elif opcion == "4":
    print(f"Resultado: {dividir(num1, num2)}")
else:
    print("Opción inválida")