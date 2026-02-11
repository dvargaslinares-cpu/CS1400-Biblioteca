# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
# Tiene 18 años o más y Tiene permiso
edad = int(input("cual es tu edad? "))
print(edad)
if edad >= 18 and tiene_permiso:
    print("true, puedes salir")
else: 
    print("puedes salir solo con una persona mayor de 18")



# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso

permiso = int(input("tienes permiso para salir este fin de semana? "))
if permiso == "si" or tiene_permiso:
    print("true, puedes salir")
else: 
    print("tiene permiso solo con una persona mayor de 18")



# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
permiso = input("tienes permiso para salir este fin de semana? ")
if permiso == "no" and not tiene_permiso: # type: ignore
    print("fals, puedes salir")
else: 
    print("no tiene permiso por que no hizo sus deberes")



# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
conducir = int(input("tienes licencia para conducir? "))
tiene_licencia = True
if conducir >= 18 and not tiene_licencia: 
    print("fals, puedes salir")
else: 
    print("no puede conducir por que no tiene licencia")



