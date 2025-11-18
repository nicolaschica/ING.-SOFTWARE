#CALCULADORA COMPLETA
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

print("\nOperaciones disponibles:")
print("1. Sumar")
print("2. Restar")

opcion = input("\nElige una operación (1-2): ")

print()
if opcion == "1":
    print(f"Resultado: {sumar(num1, num2)}")
elif opcion == "2":
    print(f"Resultado: {restar(num1, num2)}")
else:
    print("Opción inválida")