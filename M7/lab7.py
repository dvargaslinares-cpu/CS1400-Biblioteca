# pedir un numero
num1 = int(input("dame un numero: "))

#pedir un segundo numero
num2 = int(input("otro numero: "))

# solicituar una operacion
operacion = input("dame una operacion (+, -, *, /): ")

# si es una suma, sumar
if operacion == "+":
    suma = num1 + num2
    print(suma)

#si es una resta, restar
if operacion == "-":
    resta = num1 -num2
    print(resta)
#si es una multiplicacion, multiplicar
if operacion == "*":
    multiplicacion = num1 * num2
    print(multiplicacion)
#si es una division, dividir
if operacion == "/":
    divicion = num1 / num2
    print(divicion)
else:
    print("operacion no valida")

