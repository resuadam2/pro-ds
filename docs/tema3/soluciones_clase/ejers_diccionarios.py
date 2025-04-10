# Ejercicios con diccionarios

# Ejercicio 1

# Escribir una función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.    

def aprobadas(diccionario: dict) -> dict:
    try:
        return {asignatura.upper(): nota for asignatura, nota in diccionario.items() if nota >= 5}
    except AttributeError:
        print("Error: el argumento debe ser un diccionario")
        return {}
    except TypeError:
        print("Error: las notas deben ser números")
        return {}
    except:
        print("Error inesperado")
        return {}

def aprobadas_v2(diccionario: dict) -> dict:
    try:
        aprobadas = {}
        for asignatura, nota in diccionario.items():
            if nota < 0 or nota > 10:
                raise ValueError("Las notas deben estar entre 0 y 10")
            if nota >= 5:
                aprobadas[asignatura.upper()] = nota
        return aprobadas
    except AttributeError:
        print("Error: el argumento debe ser un diccionario")
        return {}
    except TypeError:
        print("Error: las notas deben ser números")
        return {}
    except ValueError as e:
        print(e)
        return {}
    except:
        print("Error inesperado")
        return {}
    
def aprobadas_v3(diccionario: dict) -> dict:
    try:
        aprobadas = {}
        for asignatura, nota in diccionario.items():
            if nota < 0 or nota > 10:
                print("Error en la nota de "+ asignatura +": las notas deben estar entre 0 y 10")
                continue
            if nota >= 5:
                aprobadas[asignatura.upper()] = nota
        return aprobadas
    except AttributeError:
        print("Error: el argumento debe ser un diccionario")
        return {}
    except TypeError:
        print("Error: las notas deben ser números")
        return {}
    except:
        print("Error inesperado")
        return {}
    
# Pruebas
print(aprobadas({"Matemáticas": 4, "Lengua": 6, "Historia": 5, "Inglés": 3})) # {'LENGUA': 6, 'HISTORIA': 5}    
print(aprobadas({"Matemáticas": 5, "Lengua": 15, "Historia": 5, "Inglés": 5})) # {'MATEMÁTICAS': 5, 'LENGUA': 5, 'HISTORIA': 5, 'INGLÉS': 5} 
print(aprobadas({})) # {}
print(aprobadas({"Matemáticas": "asdf", "Lengua": 13, "Historia": -2, "Inglés": 1})) # {}
print(aprobadas([1, 2, 3])) # {} # Error
print(aprobadas(1234)) # {} # Error
print(aprobadas_v2({"Matemáticas": 5, "Lengua": 15, "Historia": 5, "Inglés": 5})) # {'MATEMÁTICAS': 5, 'LENGUA': 5, 'HISTORIA': 5, 'INGLÉS': 5} 
print(aprobadas_v3({"Matemáticas": 5, "Lengua": 15, "Historia": 5, "Inglés": 5})) # {'MATEMÁTICAS': 5, 'LENGUA': 5, 'HISTORIA': 5, 'INGLÉS': 5} 

# Ejercicio 2

# Escribir una función que reciba un diccionario con el horario de un alumno y lo recorra imprimiendo los días de la semana y las asignaturas que tiene en cada uno.

def imprimir_horario(diccionario: dict) -> None:
    try:
        for dia, asignaturas in diccionario.items():
            if isinstance(asignaturas, str):
                print(f"{dia}: {asignaturas}")
                continue
            print(f"{dia}: {', '.join(asignaturas)}")
    except AttributeError:
        print("Error: el argumento debe ser un diccionario")
    except TypeError:
        print("El valor de cada día debe ser un elemento iterable, pero no una string")
    except:
        print("Error inesperado")

def imprimir_horario_v2(diccionario: dict) -> None:
    for dia, asignaturas in diccionario.items():
        print(f"{dia}: ", end="")
        for i in range(len(asignaturas)-1):
            print(asignaturas[i], end=", ")
        print(asignaturas[-1])

def imprimir_horario_v3(diccionario: dict) -> None:
    for dia, asignaturas in diccionario.items():
        print(f"{dia}: ", end="")
        for i in enumerate(asignaturas):
            print(asignaturas[i], end=", ")
        print(asignaturas[-1])

# Pruebas
imprimir_horario({"Lunes": ["Matemáticas", "Lengua"], "Martes": ["Historia", "Inglés"], "Miércoles": ["Física", "Química"]})    
# Lunes: Matemáticas, Lengua
# Martes: Historia, Inglés
# Miércoles: Física, Química

imprimir_horario_v2({"Lunes": ["Matemáticas", "Lengua"], "Martes": ["Historia", "Inglés"], "Miércoles": ["Física", "Química"]})    
imprimir_horario_v2({"Lunes": "Matemáticas", "Martes": ["Historia", "Inglés"], "Miércoles": ["Física", "Química"]})
imprimir_horario({"Lunes": "Matemáticas", "Martes": ["Historia", "Inglés"], "Miércoles": ["Física", "Química"]})
imprimir_horario({"Lunes": ["Matemáticas"], "Martes": ["Historia", "Inglés"], "Miércoles": ["Física", "Química"]})

# Ejercicio 3

# Escribir una función que reciba un diccionario con los precios de distintos productos y un diccionario con los productos y la cantidad de cada uno que ha comprado un cliente y devuelva el precio total de la compra.

def precio_total(precios: dict, compra: dict) -> float:
    try:
        return sum(precios[producto] * cantidad for producto, cantidad in compra.items())
    except KeyError as e:
        print(f"Error: el producto {e} no está en el diccionario de precios")
        return 0
    except TypeError as e:
        print("Error: el diccionario de precios y el compra deben contener solo números")
        return 0
    except:
        print("Error inesperado")
        return 0
    
def precio_total_v2(precios: dict, compra: dict) -> float:
    total = 0
    for producto, cantidad in compra.items():
        total += precios[producto] * cantidad
    return total

# Pruebas
print(precio_total({"Manzanas": 1, "Peras": 2, "Plátanos": 3}, { "Peras": 1, "Manzanas": 2})) # 4    
print(precio_total({"Manzanas": 1, "Peras": 2, "Plátanos": 3}, {"Manzanas": 2, "Peras": 1, "Plátanos": 3})) # 13    
print(precio_total({"Manzanas": 1, "Plátanos": 3}, {"Peras": 1, "Manzanas": 2, "Plátanos": 3})) # KeyError: 'Peras'
print(precio_total({"Manzanas": "adsf", "Peras": 2, "Plátanos": 3}, {"Manzanas": 2, "Peras": 1, "Plátanos": 3}))
print(precio_total({"Manzanas": 1, "Peras": 2, "Plátanos": 3}, {"Manzanas": "asdf", "Peras": 1, "Plátanos": 3}))
print(precio_total({"Manzanas": "adsf", "Peras": 2, "Plátanos": 3}, {"MANZANAS": 2, "Peras": 1, "Plátanos": 3}))



# Ejercicio 4

# Escribir una función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva la media de las notas. 

def media_notas(diccionario: dict) -> float:
    try: 
        return sum(diccionario.values()) / len(diccionario)   
    except ZeroDivisionError:
        print("Error: el diccionario está vacío")
        return 0
    except AttributeError:
        print("Error: el argumento debe ser un diccionario")
        return 0
    except TypeError:
        print("Error: las notas deben ser números")
        return 0
    except:
        print("Error inesperado")
        return 0

    
# Pruebas
print(media_notas({"Matemáticas": 4, "Lengua": 6, "Historia": 5, "Inglés": 3})) # 4.5
print(media_notas({"Matemáticas": 5, "Lengua": 5, "Historia": 5, "Inglés": 5})) # 5.0
print(media_notas({}))
print(media_notas({"Matemáticas": "adsf", "Lengua": 5, "Historia": 5, "Inglés": 5})) 
print(media_notas(1234)) 


# Ejercicio 5

# Escribir una función que reciba un diccionario con los planetas del sistema solar y sus distancias al sol, además debe recibir un planeta y devolver su distancia a la Tierra
# Las distancias se expresan en millones de kilómetros.
# La distancia de la Tierra al Sol es de 149.6 millones de kilómetros.
# La distancia de los planetas al Sol son las siguientes:
# Mercurio: 57.9
# Venus: 108.2
# Tierra: 149.6
# Marte: 227.9
# Júpiter: 778.5
# Saturno: 1433.4
# Urano: 2872.5
# Neptuno: 4495.1
# Plutón: 5906.4

def distancia_a_tierra(planetas: dict, planeta: str) -> float:
    try:
        return round(abs(planetas[planeta] - 149.6), 2)
    except AttributeError:
        print("Por favor, introduzca un diccionario con los planetas y sus distancias al sol y un planeta")
        return -1
    except TypeError:
        print("Por favor, introduzca un diccionario con los planetas y sus distancias al sol y un planeta")
        return -1
    except KeyError:
        print("Por favor, introduzca un planeta válido")
        return -1
    except:
        print("Error inesperado")
        return -1

# Pruebas
# Distancia de la Tierra al Sol: 149.6
# Distancia de Marte al Sol: 227.9
# Distancia de Marte a la Tierra: 78.3
# Distancia de Plutón al Sol: 5906.4
# Distancia de Plutón a la Tierra: 5756.8
# Distancia de Venus al Sol: 108.2
# Distancia de Venus a la Tierra: 41.4
# Distancia de Saturno al Sol: 1433.4
# Distancia de Saturno a la Tierra: 1283.8
# Distancia de Júpiter al Sol: 778.5
# Distancia de Júpiter a la Tierra: 628.9
# Distancia de Neptuno al Sol: 4495.1
# Distancia de Neptuno a la Tierra: 4345.5
# Distancia de Urano al Sol: 2872.5
# Distancia de Urano a la Tierra: 2722.9
# Distancia de Mercurio al Sol: 57.9
# Distancia de Mercurio a la Tierra: 91.7

planetas = {"Mercurio": 57.9, "Venus": 108.2, "Tierra": 149.6, "Marte": 227.9, "Júpiter": 778.5, "Saturno": 1433.4, "Urano": 2872.5, "Neptuno": 4495.1, "Plutón": 5906.4}
print(distancia_a_tierra(planetas, "Marte")) # 78.3
print(distancia_a_tierra(planetas, "Plutón")) # 5756.8
print(distancia_a_tierra(planetas, "Venus")) # 41.4
print(distancia_a_tierra(planetas, "Saturno")) # 1283.8
print(distancia_a_tierra(planetas, "Júpiter")) # 628.9
print(distancia_a_tierra(planetas, "Neptuno")) # 4345.5
print(distancia_a_tierra(planetas, "Urano")) # 2722.9
print(distancia_a_tierra(planetas, "Mercurio")) # 91.7
print(distancia_a_tierra(planetas, "Tierra")) # 0.0
print(distancia_a_tierra(planetas, "Alderaan")) # -1

# Ejercicio 6

# Escribir una función que reciba una lista de palabras y devuelva un diccionario con las palabras como claves y su longitud como valor.

def longitud_palabras(lista: list) -> dict:
    try:
        return {palabra: len(palabra) for palabra in lista}  
    except TypeError:
        print("Por favor, introduzca una lista de palabras")
        return {}
    except:
        print("Ha ocurrido un error inesperado")
        return {}

def longitud_palabras(lista: list) -> dict:
    try:
        toret = {}
        for palabra in lista:
            toret[palabra] = len(palabra) 
        return toret
    except TypeError:
        print("Por favor, introduzca una lista de palabras")
        return {}
    except:
        print("Ha ocurrido un error inesperado")
        return {}
    
# Pruebas
print(longitud_palabras(["hola", "adiós", "buenos días", "buenas noches"])) # {'hola': 4, 'adiós': 5, 'buenos días': 10, 'buenas noches': 13}
print(longitud_palabras(["hola", "adiós", "buenos días", "buenas noches", ""])) # {'hola': 4, 'adiós': 5, 'buenos días': 10, 'buenas noches': 13, '': 0}    
print(longitud_palabras({"hola"}))

# Ejercicio 7

# Escribir una función que reciba una lista de palabras y devuelva un diccionario con las palabras como claves y el número de veces que aparecen como valor.

def frecuencia_palabras(lista: list) -> dict:
    try:
        toret = {}
        for palabra in lista:
            toret[palabra] = lista.count(palabra)
        return toret
    except TypeError:
        print("Por favor, introduzca una lista de palabras")
        return {}
    except:
        print("Ha ocurrido un error inesperado")
        return {}
    
def frecuencia_palabras(lista: list) -> dict:
    try:
        return { palabra: lista.count(palabra) for palabra in lista }
    except TypeError:
        print("Por favor, introduzca una lista de palabras")
        return {}
    except:
        print("Ha ocurrido un error inesperado")
        return {}
    
# Pruebas
print(frecuencia_palabras(["hola", "adiós", "hola", "buenos días", "buenas noches"])) # {'hola': 2, 'adiós': 1, 'buenos días': 1, 'buenas noches': 1}   
print(frecuencia_palabras(["hola", "adiós", "hola", "buenos días", "buenas noches", ""])) # {'hola': 2, 'adiós': 1, 'buenos días': 1, 'buenas noches': 1, '': 1}    



# Haz una función que pida al usuario los datos de un coche, los datos son:

"""
Marca - string
Color - string
Cilindrada - entero
"""

def diccionarioVehiculo():
    marca = input("Introduce la marca")
    color = input("Introduce el color del coche")
    cilindradaOk = False
    while not cilindradaOk:
        try:
            cilindrada = int(input("introduce la cilindrada"))
            if cilindrada < 1:
                raise AttributeError("La cilindrada debe ser positiva")
            cilindradaOk = True
        except AttributeError as e:
            print(e)
        except ValueError:
            print("La cilindrada debe ser un número entero")

    return {"Marca": marca, "Color": color, "Cilindrada": cilindrada}

print(diccionarioVehiculo())