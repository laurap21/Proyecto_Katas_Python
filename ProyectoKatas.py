# PROYECTO LÓGICA: Katas de Python

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
# 
# - Para recorrer cada elemento de la cadena de texto, se utiliza el bucle *for*. 
# - Para normalizar mayúsculas/minúsculas se utiliza el método *.lower()*.
# - Con el primer condicional *if* se ignoran los espacios, en caso de haberlos. 
# - Con el segundo condicional *if* se comprueba si la letra que está recorriendo el bucle exista ya como clave en el diccionario (previamente en la función se ha creado un diccionario vacío): si ya existe, se suma uno al valor correspondiente a esa clave; si no (*else*), se añade el par calve-valor al diccionario con el valor de 1.
# - La función devuelve el diccionario completo.
# 
# Mejoras/futuros pasos: 
# - Utilizar la función *.get()*.

# DEFINICIÓN DE LA FUNCIÓN

def contar_letras(texto):
    """ Esta función recorre una cadena de texto y devuelve un diccionario con las frecuencias de cadaa letra en la cadena, ignorando los espacios.
        ARGUMENTOS: 
            - texto (str) --> cadena de texto
        RETURNS:
            - diccionario (dict) --> diccionario con el recuento completo
        """
    diccionario = {}
    for i in texto.lower():
        if i != ' ':
            if i in diccionario: 
                diccionario[i] = diccionario[i] + 1
            else:
                diccionario[i] = 1

    return diccionario


# COMPROBACIÓN DEL FUNCIONAMIENTO DE LA FUNCIÓN

texto = input('Inserta un texto: ')
type(texto)

resultado = contar_letras(texto)

print(resultado)


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función *map()*.
# 
# La función *map()* necesita dos argumentos para funcionar: una función y un iterable. En este caso, el iterable será una lista y se utilizará una función lambda para duplicar el valor de cada elemento en la lista 1. 
# La función *amp()* no devuelve una lista, por lo que hay que convertirlo con la función *list()*.


lista_numeros = [1, 2, 3, 4, 5]

lista_numeros2 = list(map((lambda x: x*2), lista_numeros))

lista_numeros2


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
# 
# Para la correcta definición de la función se ha empleado un control de errores que genera un TypeError si la lista que se le pasa como parámetro contiene algún elemento distinto a un string. 
# En la función se emplea el método *.lower()* para cada iterable de la lista para normalizar mayúsculas y minúsculas. 
# Si la lista contiene solamente strings, la función devuelve la lista solicitada, es decir, una lista solo con las palabras de la lista original que contengan la palabra objetivo.
# - Puntos de mejora: ¿qué ocurre cuando la *palabra_objetivo* no es una palabra? Hace falta comprobación también. También puedo ignorarlo y no incluir ese iterable en la lista --> CORREGIDO
#
# COMENTARIOS CORRECCIÓN:
# - No se valida que palabra_objetivo sea un string, lo que puede provocar errores.
# - El nombre del parámetro lista pisa el nombre de la función built-in list, lo cual es mala práctica.

# DEFINICIÓN DE LA FUNCIÓN - CORREGIDA

def filtrar_palabra2(palabra_objetivo, lista_palabras):

    """ La función busca una palabra objetivo en una lista de palabras y devuelve una nueva lista con las palabras originales que contentan la palabra objetivo.
        ARGUMENTOS:
        - palabra_objetivo (str) --> palabra a buscar en la lista de palabras.
        - lista_palabras (list) --> conjunto de palabras a comparar con la palabra objetivo
        RETURN:
        - lista_objetivo (list) --> lista con las palabras que cumplen la condución de la función"""
    
    if not all(isinstance(x, str) for x in lista_palabras):
        raise TypeError('La lista debe contener solo strings')
    
    lista_objetivo = []
    
    for palabra in lista_palabras:
        if palabra_objetivo.lower() in palabra.lower():
            lista_objetivo.append(palabra)
    return lista_objetivo
              

# COMPROBACIÓN DEL FUNCIONAMIENTO

frutas = ['manzana', 'banana', 'naranja', 'mandarina', 'mango', 'pera']
palabra_objetivo = 'man'

lista_objetivo = filtrar_palabra2(palabra_objetivo, frutas)
lista_objetivo

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función *map()*.
# La función creada emplea la función *map()* para restar elemento a elementos los iterables de una lista. 
# Si las listas no tienen la misma longitud, se muetra un mensaje que explica que solo se han tenido en cuenta las longitudes coincidentes de ambas lista, ya que no es un impedimento para realizar el objetivo solicidato pero no es exactamente correcto.

# DEFINICIÓN DE LA FUNCIÓN

def resta_listas(lista1, lista2):
    """
    La función hace la resta iterable a iterable entre dos listas y devuelve otra lista con la diferencia entre estos valores.
    ARGUMENTOS:
    - lista1 (list) --> lista 1 de iterables a restar.
    - lista2 (list) --> lista 2 de iterables a restar.
    RETURN:
    - resultado (list) --> lista con los resultados de las restas.
    """
    if len(lista1) != len(lista2):
        print('Las listas no tienen la misma longitud, solo se muestra el resultado del número de valores coincidentes.')
        
    resultado = list(map((lambda x,y: x-y), lista1, lista2))
    
    return resultado

# COMPROBACIÓN DEL FUNCIONAMIENTO

lista_1 = [2, 3, 4, 5]
lista_2 = [1, 3, 2]

resta_listas(lista_1, lista_2)


# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional *nota_aprobado*, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que *nota_aprobado*. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

# La función comprueba primero si la lista está vacía. Si no lo está, calcula la media y le asigna el estado.
# Si la función está vacía, devuelve por pantalla el fallo y asigna el valor 0 a la media y el estado será 'desconocido'.
# Puntos de mejora:
# - Error si la lista no contiene valores numéricos.

# DEFINICIÓN DE LA FUNCIÓN

def comparacion_notas(notas, nota_aprobado=5):
    """ 
    La función calcula la media de una lista de notas y la compara con la nota_aprobado. Si la media está por encima de la nota_aprobado, el estado será "aprobado", si no, "suspenso".
    ARGUMENTOS:
    - notas (list) --> lista de notas.
    - nota_aprobado (int) --> 5 por defecto. Valor con el que se compará la media de notas.
    RETURN:
    - resultado (tuple) --> tupla con la nota media calculada y el estado.
    """
    
    if notas:
        media = sum(notas)/len(notas)
        if media < nota_aprobado:
            estado = 'Suspenso'
        else:
            estado = 'Aprobado'

    else:
        print('La lista no puede estar vacía.')
        media = 0
        estado = 'desconocido'

    resultado = (media, estado)

    return resultado 


# COMPROBACIÓN DEL FUNCIONAMIENTO

notas = [3, 6, 7, 9, 10]
comparacion_notas(notas)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
# Matemáticamente, solo aplica a a números enteros y positivos.
# Para evitar un error recursivo (RecursionError) y que se entre en un bucle infinito, se pone un *if* para cuando n valga 1. En ese caso, devuelve 1.
#
# COMENTARIOS CORRECCIÓN:
# - No se controla que n sea entero positivo.
# - Si n es 0 o negativo, la función entra en recursión infinita.

# DEFINCIÓN DE LA FUNCIÓN - CORREGIDA

def factorial(n):
    """ 
    La función calcula el factorial de n, siempre que n sea un número entero positivo.
    ARGUMENTOS:
    - n (int) --> número entero positivo.
    RETURN:
    - int --> valor del factorial calculado de n 
    """
    if not isinstance(n, int) or n > 1:
        raise ValueError('El número deve ser entero positivo.')
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(5)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función *map()*.
# En esta función se siguen dos pasos simultáneos:
# 1. Cada tupla de la lista de tuplas se convierte a string.
# 2. Para hacer más limpia la lista final, se unen los iterables de cada string creado con una ", " como separación.


# DEFINICIÓN DE LA FUNCIÓN
def lista_tuplas_a_strings(lista_tuplas):
    """ La función convierte una lista de tuplas en una lista de strings.
        ARGUMENTOS:
        - lista_tuplas (list) --> lista de tuplas inicial
        RETURN:
        - list --> lista de strings """
    
    return list(map(lambda t: ", ".join(map(str,t)), lista_tuplas))


lista_tuplas = [('hola', 'laura'), ('adios', 'pedro')]
lista_strings = lista_tuplas_a_strings(lista_tuplas)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
# Se solicitan dos valores numéricos al usuario y se intentan convertir a *float* y dividir entre ellos:
# - Si alguno de los valores introducidos no se puede convertir a *float* salta un TypeError capturado por el primer *except*. 
# - Si se intenta dividir por cero, ocurre lo mismo con el segundo *except*.
# - Si todo es correcto, se muestra que la división es exitosa y su resultado.

try:    
    x = float(input('Ingresa un valor numérico: '))
    y = float(input('Ingresa otro valor numérico: '))

    division = x/y

except ValueError:
    print('Los valores introducidos ndeben ser numéricos para poder realizar la división.')

except ZeroDivisionError:
    print('No se puede dividir entre cero.')

else:
    print(f'La división fue exitosa. El resultado es: {division}')

# ### 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']. Usa la función *filter()*.
# Para la función *filter()* se emplea una función lambda que determine si cada elemento de la lista de animales se encuentra o no (True/False) en la lista de mascotas excluidas.

# DEFINICIÓN DE LA FUNCIÓN
def mascotas(lista_mascotas):
    mascotas_excluidas = ['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']
    return list(filter(lambda x: x not in mascotas_excluidas, lista_mascotas))

lista_mascotas = ['Mapache', 'Perro', 'Gato', 'Tigre', 'Tortuga', 'Pez', 'Serpiente Pitón', 'Cocodrilo', 'Oso']
mascotas(lista_mascotas)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
# Para crear excepciones personalizadas, se crea una clase heredada de *Exception*.
# En la definición de la función, se incluye la excepción personalizada si la lista introducida como argumento está vacía.
# Se maneja el error con *try...except*

lista_promedio = []

# CREACIÓN DE LA EXCEPCIÓN PERSONALIZADA

class ExcepcionListaVacia(Exception):
    """ Excepción que se lanza cuando una lista de números está vacía """
    pass

# DEFINICIÓN DE LA FUNCIÓN

def promedio(lista_numeros):
    """ Función que calcula el promedio de los valores de una lista
        ARGUMENTOS:
        - lista_numeros (list) --> lista de valores inicial
        RETURN:
        - float --> valor promedio """
    if not lista_numeros:
        raise ExcepcionListaVacia('La lista no puede estar vacía')
    
    return float(sum(lista_numeros)/len(lista_numeros))

# MANEJO DEL ERROR

try:
    resultado = promedio(lista_promedio)
    print(f'El promedio es: {resultado}')

except ExcepcionListaVacia as e:
    print(f'Error: {e}')

# 11. Escribe un programa que le pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# Para separar los dos posibles errores (ValueError) se utiliza el manejo de errores *try/except/else* para que ambos se muestren de forma diferenciada en caso de ocurrir.

# CÓDIGO CON MANEJO DE ERRORES
try:

    edad = int(input('Escribe tu edad: '))

except ValueError:
    print('Error: el valor introducido debe ser un número.')

else:
    if edad not in range(0,121):
        print('La edad debe estar entre 0 y 120.')
    else:
        print(f'La edad del usuario es: {edad}')

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función *map()*.

# DEFINICIÓN DE LA FUNCIÓN
def lista_longitudes(frase):
    """La función devuelve una lista con las longitudes de cada palabra del string inicial.
        ARGUMENTOS:
        - frase (str) --> frase inicial sobre la que devolver la lista.
        RETURN:
        - list --> lista de las longitudes de cada palabra"""
    
    lista_frase = frase.split()
    return list(map(len, lista_frase))

# COMPROBACIÓN DEL FUNCIONAMIENTO
frase = 'Hola me llamo Laura'
lista_longitudes(frase)


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función *map()*.
# Para segurar que las letras del conjunto de caracteres no está repetido, se convierte el string inicial a *set* en minúsculas.
# Con la función *map()* y una función *lambda* se crean las tuplas para cada iterable del string y se crea la lista final, ordenada con la función *sorted()*.
# - Conjunto de caracteres inicial --> ¿set?

# DEFINCIÓN DE LA FUNCIÓN
def lista_tuplas_caracteres(conjunto_caracteres):
    conjunto_unico = set(c.lower() for c in conjunto_caracteres)
    return list(map(lambda x: (x.upper(), x.lower()), sorted(conjunto_unico)))


conjunto_caracteres = 'Pepa'
lista_tuplas_caracteres(conjunto_caracteres)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Usa la función *filter()*.
#
# COMENTARIOS CORRECCIÓN:
# - No se normaliza letra_especifica a minúsculas, lo que puede provocar resultados incorrectos.

# DEFINICIÓN DE LA FUNCIÓN

def lista_letra_especifica(lista_palabras, letra_especifica):
    """La función devuelve las palabras de una lista que empiezan por una letra específica.
        ARGUMENTOS:
        - lista_palabras (list) --> lista de palabras en la que buscar.
        - letra_especifica (str) --> letras por la que queremos que empiecen las palabras resultado.
        REUTURN:
        - list --> lista de palabras que comienzan por la letra específica."""
    
    letra_especifica = letra_especifica.lower()
    return list(filter(lambda x: x[0].lower() == letra_especifica, lista_palabras))


lista_palabras = ['Palabra', 'Plátano', 'Avion', 'Estuche', 'Pelota']
letra_especifica = 'p'

lista_letra_especifica(lista_palabras, letra_especifica)

# 15. Crea una función *lambda* que sume 3 a cada número de una lista dada.
#
# COMENTARIOS CORRECCIÓN:
# - La lambda ignora el parámetro recibido y una una variable externa (lista_numeros3).

# DEFINCIÓN DE LA FUNCIÓN LAMBDA
sumar_tres = lambda lista: list(map(lambda x: x+3, lista))

lista_numeros3 = [1, 2, 3, 4, 5]
sumar_tres(lista_numeros3)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función *filter()*.

# DEFINICIÓN DE LA FUNCIÓN
def palabras_n(cadena_texto, n):
    lista_cadena = cadena_texto.split()
    return list(filter(lambda x: len(x) > n, lista_cadena))

cadena_texto = 'Hola me llamo Laura'
n = 4
palabras_n(cadena_texto, n)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5, 7, 2] corresponde al número quinientos setenta y dos (572). Usa la función *reduce()*.

from functools import reduce


# DEFINICIÓN DE LA FUNCIÓN
def crear_numero(lista_digitos):
    return reduce(lambda x,y: x*10 + y, lista_digitos)

lista_digitos = [1,2,3,4]
numero = crear_numero(lista_digitos)
print(numero)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función *filter()* para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función *filter()*.

# DATOS INICIALES
nombres = ['Laura', 'Alex', 'Maria', 'Pedro']
edades = [30, 28, 29, 30]
calificaciones = [91, 80, 55, 90]

cal_valida = 90

# CREACIÖN DE LA LISTA DE DICCIONARIOS + USO DE FILTER()
alumnos = []

for nombre, edad, calificacion in zip(nombres, edades, calificaciones):
    estudiante = {'nombre': nombre, 'edad': edad, 'calificacion': calificacion}
    alumnos.append(estudiante)

alumnos_mas_90 = list(filter(lambda alumno: alumno['calificacion'] >= cal_valida, alumnos))

alumnos_mas_90

# 19. Crea una función *lambda* que filtre los números impares de una lista dada.

# DEFINICIÓN DE LA FUNCIÓN
filtrar_impares = lambda lista_numeros: list(filter(lambda x: x%2 != 0, lista_numeros))

lista_numeros4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtrar_impares(lista_numeros4)

# 20. Para una lista con elementos tipo interger y string obtén una nueva lista sólo con los valores int. Usa la función *filter()*.

lista_int_str = ['Laura', 30, 'Azul', 572]

lista_int = list(filter(lambda x: isinstance(x, int), lista_int_str))

lista_int

# 21. Crea una función que calcule el cubo de un número dado mediante una función *lambda*.

cubo_numero = lambda x: x**3

cubo_numero(2)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función *reduce()*.

lista_num = [1, 2, 3, 4, 5]

reduce(lambda x,y : x*y, lista_num)

# 23. Concatena una lista de palabras. Usa la función *reduce()*.

lista_palabras2 = ['Hola', 'me', 'llamo', 'Laura']

reduce(lambda x,y: x + " " + y, lista_palabras2)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función *reduce()*.

lista_num2 = [19, 3, 5]

reduce(lambda x,y: x - y, lista_num2)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
# Con la función *len()* se cuentan los caracteres de la cadena de texto, incluyendo espacios.

# DEFINICIÓN DE LA FUNCIÓN
def contar_catacteres(cadena):
    return len(cadena)

cadena = 'Hola'
contar_catacteres(cadena)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda a, b: a%b
resto_division(40,6)

# 27. Crea una función que calcule el promedio de una lista de números.

# DEFINCICIÓN DE LA FUNCIÓN
def promedio2(lista_numeros):
    """ Función que calcula el promedio de los valores de una lista
        ARGUMENTOS:
        - lista_numeros (list) --> lista de valores inicial
        RETURN:
        - float --> valor promedio """
    
    return float(sum(lista_numeros)/len(lista_numeros))

num_list = [2, 3, 4]
promedio2(num_list)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# Dentro de la función se crea un set para almacenar los elementos de la lista inicial. Como no se admiten duplicados en los set, solo se almacena una vez cada elemento en caso de estar repetido.
# Una vez encuentra un duplicado (dentro del bucle *for* de acuerdo al condicional *if*), devuelve el primer duplicado que encuentre o None si no encuentra ninguno

# DEFINICIÓN DE LA FUNCIÓN

def primer_duplicado(lista_dada):
    """ La función busca y devuelve el primer duplicado de una lista dada.
        ARGUMENTOS:
        - lista_dada (list) --> lista en la que buscar elementos duplicados.
        RETURN:
        - Si existen duplicados --> devuelve el duplicado (str, int, float)
        - Si no existen duplicados --> devuelve None """
    
    duplicado = set()
    for x in lista_dada:
        if x in duplicado:
            return x
        duplicado.add(x)
    return None

lista_dada = [1, 2, 3, 5, 3, 5]
primer_duplicado(lista_dada)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el caracter *#*, excepto los últimos 4. 

# DEFINICIÓN DE LA FUNCIÓN
def enmascarar_cadena(variable):
    """ La función convierte la variable en cadena de texto (str) y oculta todos los caracteres con # salvo los 4 úlimos.
        ARGUMENTOS:
        - variable (any) --> variable que convertiremos a string.
        RETURN:
        - resultado (string) --> cadena de caracteres con los primeros enmascarados. """

    variable_str = str(variable)

    resultado = ''

    for indice in range(len(variable_str)):
        if indice < (len(variable_str)-4):
            resultado = resultado + '#'
        else:
            resultado = resultado + variable_str[indice]

    return resultado

# COMPROBACIÓN DEL FUNCIONAMIENTO
variable = input('Introduce una variable')

# Opción 2:
def enmascarar_cadena2(variable):
    """La función convierte la variable en cadena de texto (str) y oculta todos los caracteres con # salvo los 4 úlimos.
        ARGUMENTOS:
        - variable (any) --> variable que convertiremos a string.
        RETURN:
        - resultado (string) --> cadena de caracteres con los primeros enmascarados. """

    variable_str = str(variable)

    resultado = '#' * (len(variable_str)-4) + variable_str[-4:]

    return resultado

print(enmascarar_cadena(variable))
print(enmascarar_cadena2(variable))

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagramas(palabra1, palabra2):
    """Devuelve True si las palabras introducidas son anagramas.
        ARGUMENTOS:
        - palabra1 (str) --> palabra a comparar 1.
        - palabra2 (str) --> palabra a comparar 2.
        RETURN:
        - True --> las palabras son anagramas.
        - False --> las palabras no son anagramas."""
    
    palabra1_espacios = palabra1.replace(' ', '')
    palabra2_espacios = palabra2.replace(' ', '')

    if sorted(palabra1_espacios.lower()) == sorted(palabra2_espacios.lower()):
        return True
    else:
        return False

palabra1 = 'cata'
palabra2 = 'Taca'

anagramas(palabra1, palabra2)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
# La función pide una lista de nombres, separados por una coma y un espacio y transforma la cadena introducida a una lista haciendo uso de *strip()* para eliminar los espacios y de *split(',')* para la transformación a lista separados por una coma.
# La función comprueba si el nombre buscado está en la lista introducida y transformada y si no está, devuelve un error. 
# Para normalizar mayúsculas y minúsculas, se emplea el método *lower()* tanto para la lista de nombres como para el nombre buscado.

def buscar_nombre():
    """La función solicita una lista de nombres y un nombre a buscar y comprueba si este nombre está en la lista."""
    
    nombres_str = (input('Ingresa una lista de nombres separados por una coma (,) y un espacio: '))
    lista_nombres = [nombre.strip().lower() for nombre in nombres_str.split(',')]

    nombre_buscado = input('Ingresa el nombre a buscar: ').lower()
        
    if nombre_buscado in lista_nombres:
        print(f'El nombre buscado es {nombre_buscado} y se encuentra en la lista.')
    else:
        raise ValueError('Nombre no encontrado')

buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# En este caso no se hace normalización de mayúsculas y minúsculas.
#
# COMENTARIOS CORRECCIÓN:
# - Las comillas dentro de f-string general un SyntaxError

# Variables iniciales: str --> nombre_completo a buscar // lista de diccionarios de los trabajadores donde se guarda también su puesto.
nombre_completo = 'Dani Pastora'
trabajadores = [
    {'nombre': 'Laura Pomares', 'puesto': 'Comercial'},
    {'nombre': 'Alex Gomex', 'puesto': 'Programador'},
    {'nombre': 'Dani Pastor', 'puesto': 'Project Manager'}
]

# DEFINICIÓN DE LA FUNCIÓN
def puesto_trabajador(trabajadores, nombre_completo):
    """La función busca el nombre del trabajador en la lista. Si existe, devuelve el puesto del trabajador.
        ARGUMENTOS:
        - trabajadores (list) --> lista de diccionarios con el nombre y el puesto de los trabajadores.
        - nombres_completo(str) --> nombre completo del trabajador a buscar
        RETURN:
        - puesto de trabajo de la persona buscada.
        - mensaje 'La persona buscada no trabaja aquí.'"""
    
    for trabajador in trabajadores:
        if trabajador['nombre'] == nombre_completo:
            return f"Puesto: {trabajador['puesto']}"

    return 'La persona buscada no trabaja aquí.'

puesto_trabajador(trabajadores, nombre_completo)

# 33. Crea una función *lambda* que sume elementos correspondientes de dos listas dadas.
suma_listas = lambda lista_A, lista_B: [a + b for a,b in zip(lista_A, lista_B)]

lista_A = [2, 3, 4, 6]
lista_B = [3, 7, 8, 1]

suma_listas(lista_A, lista_B)

# 34. Crea la clase *Arbol*, define un árbol genérico con un tronco y ramas con atributos. Los métodos disponibles son: *crecer_tronco*, *nueva_rama*, *crecer_ramas*, *quitar_rama* e *info_arbol*. El objetivo es implementar estos métodos para manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método *crecer_tronco* para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método *nueva_rama* para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método *crecer_ramas* para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método *quitar_rama* para eliminar una rama en una posición específica.
# 6. Implementar el método *info_arbol* para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# 
# CASO DE USO:
# 1. Crea un árbol.
# 2. Hacer crecer una nueva rama al árbol.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol en una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

# DEFINCIÓN DE LA CLASE Árbol
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self, unidades=1):
        """Hace crecer el tronco en una unidad."""
        self.tronco += unidades

    def nueva_rama(self, num_ramas=1):
        """Añade una nueva rama a la lista de ramas con longitud 1."""
        for x in range(num_ramas):
            self.ramas.append(1)
    
    def crecer_ramas(self, unidades=1):
        """Hace crecer a todas las ramas en una unidad."""
        self.ramas = list(map(lambda x: x + unidades, self.ramas))

    def quitar_rama(self, posicion):
        """Si la posición indicada es correcta, elimina la rama de dicha posición."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print('Posición incorrecta')

    def info_arbol(self):
        """Muestra la información del árbol"""
        return {'tronco': self.tronco,
                'número de ramas': len(self.ramas),
                'longitud de las ramas': self.ramas}

# CASO DE USO
# 1. Crear arbol:
arbol1 = Arbol()
# 2. Hacer crecer el tronco del arbol en una unidad:
arbol1.crecer_tronco()
# 3. Añadir una nueva rama al arbol:
arbol1.nueva_rama()
# 4. Hacer crecer todas las ramas del arbol una unidad: 
arbol1.crecer_ramas()
# 5. Añadir dos nuevas ramas al árbol:
arbol1.nueva_rama(2)
# 6. Retirar la rama situada en la posición 2:
arbol1.quitar_rama(2)
# 7. Obtener información sobre el árbol:
arbol1.info_arbol()


# 36. Crea la clase *UsuarioBanco*, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante *True* y *False*.
# 2. Implementar el método *retirar_dinero* para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método *transferir_dinero* para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método *agregar_dinero* para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# 1. Crea dos usuarios: Alicia, con saldo inidial de 100 y Bob con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agrega 20 unidades de saldo de Bob.
# 3. Hacer una transferencia de 80 unidades desde Bob a Alicia.
# 4. Retirar 50 unidades de saldo a Alicia.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Comprueba si la cantidad a retirar es mayor que 0 y si existe esa cantidad en la cuenta corriente del usuario. Si no, lanza un error."""
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError('Imposible hacer la operación.')
        
    def transferir_dinero(self, otro_usuario, cant_transf):
        """ Hace la transferencia de un usuario a otro si el primer usuario pertenece al banco, si la cantidad a transferir es mayor que 0 y si el otro usuario tiene cantidad suficiente en el banco.
            Si no, lanza un error."""
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError('Ambos usuarios deben pertenecer al banco.')

        if cant_transf < 0:
            raise ValueError('La cantidad a transferir debe ser mayor que 0.')
        
        if otro_usuario.saldo < cant_transf:
            raise ValueError('El usuario no dispone de esta cantidad para transferirle.')
        
        otro_usuario.saldo -= cant_transf
        self.saldo += cant_transf

        print('La transferencia se ha realizado con éxito.')

    def agregar_dinero(self, cantidad):
        """Si la cantidad de dinero a transferir es positiva, lo agrega a la cuenta corriente del usuario."""
        if cantidad > 0:
            self.saldo += cantidad

    # Se ha añadido el método info_usuario para comprobar el correcto funcionamiento del ejercicio y el estado de cada usuario.
    def info_usuarios(self):
        """Muestra la información del usuario"""
        return {'nombre': self.nombre,
                'saldo': self.saldo,
                'cuenta corriente': self.cuenta_corriente}

# CASO DE USO
# 1. Crear dos usuarios:
usuario1 = UsuarioBanco('Alicia', 100, True)
usuario2 = UsuarioBanco('Bob', 50, True)
# 2. Agregar 20 unidades de saldo de Bob:
usuario2.agregar_dinero(20)
# 3. Hacer una transferencia de 80 unidades desde Bob a Alicia.
usuario1.transferir_dinero(usuario2, 80)
# 4. Retirar 50 unidades de saldo a Alicia.
usuario1.retirar_dinero(50)

print(usuario1.info_usuarios())
print(usuario2.info_usuarios())

# 37. Crea una función llamada *procesar_texto* que procesa un texto según la opción especificada: *contar_palabras*, *reemplazar_palabras*, *eliminar_palabra*. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función *procesar_texto*.
# 
# Código a seguir:
# 1. Crear una función *contar_palabras* para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función *reemplazar_palabras* para reemplazar una *palabra_original* del texto por una *palabra_nueva*. Tiene que devolver el texto con el reemplazo de palabras.
# 3. Crear una función *eliminar_palabra* para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función *procesar_texto* que tome un texto, una opción entre ('contar', 'reemplazar', 'eliminar') y un número de argumentos variable según la opción indicada.
# 
# Caso de uso:
# Comprueba el funcionamiento completo de la función *procesar_texto*.
#
# COMENTARIOS CORRECCIÓN:
# - No se usan los argumentos *args.
# - Se usan variables globales en lugar de los argumentos recibidos.

texto = 'Hola, me llamo Laura y tengo 30 años. Tengo una hermana. Ella se llama Raquel y tiene 27 años.'

# FUNCIÓN contar_palabras.
def contar_palabras(texto):
    """La función recibe una cadena de texto y cuenta las veces que se repite cada palabra.
        ARGUMENTOS:
        - texto (str) --> texto inicial
        RETURN:
        - contar_palabras (dict) --> diccionario con cada palabra y el número de veces que aparece."""
    
    signos_puntuacion = '.,¿?¡!:;'

    for signo in signos_puntuacion:
        texto = texto.replace(signo,'')

    lista_texto = texto.lower().split()

    contar_palabras = {}
    for palabra in lista_texto:
        if palabra in contar_palabras:
            contar_palabras[palabra] += 1
        else:
            contar_palabras[palabra] = 1
    
    return contar_palabras


# FUNCIÓN reemplazar_palabras:
palabra_original = 'Laura'
palabra_nueva = 'Pepa'

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """La función toma una palabra y la reemplaza por la otra introducida."""
    return texto.replace(palabra_original, palabra_nueva)

# FUNCIÓN eliminar_palabra:
palabra_eliminada = 'años'

def eliminar_palabra(texto, palabra_eliminada):
    """La función toma una palabra y la elimina. No elimina espacios ni signos de puntuación."""
    return texto.replace(palabra_eliminada, '')

# FUNCIÓN procesar_texto - CORREGIDA
def procesar_texto(texto, funcion, *args):
    """ La función toma un texto, una opción de función entre 'contar', 'reemplazar' o 'eliminar' y el número de argumentos correspondiente.
        ARGUMENTOS:
        - Función 'contar' --> contar_palabras --> ningún argumento.
        - Función 'reemplazar'' --> reemplazar_palabras --> dos argumentos: palabra_original (str), palabra_nueva (str)
        - Función 'eliminar' --> eliminar_palabra --> un argumetno: palabra_eliminada (str)
        RETURN:
        - La función devuelve el texto procesado según la función elegida. Si no, devuelve un error."""
    
    if funcion == 'contar':
        return contar_palabras(texto)
    
    elif funcion == 'reemplazar':
        if len(args) != 2:
            raise ValueError('La función reemplazar_palabras necesita dos argumentos: palabra original y palabra nueva.')
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif funcion == 'eliminar':
        if len(args) != 1:
            raise ValueError('La función eliminar necesita 1 argumento.')
        return eliminar_palabra(texto, args[0])
    
    else:
        raise ValueError('Función no válida.')

procesar_texto(texto, 'contar')

procesar_texto(texto, 'reemplazar', palabra_original, palabra_nueva)

procesar_texto(texto,'eliminar', palabra_eliminada)

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# 
# Rangos de horario:
# - Día --> 7h hasta 15h.
# - Tarde --> 15h hasta 22h.
# - Noche --> de 22h a 7h.
#     - De 0h a 7h.
#     - De 22h a 0h.
#
# COMENTARIOS CORRECCIÓN:
# - La condición 22 <= hora < 0 nunca se cumple.


hora = int(input('Por favor, introduce una hora (0-23): '))

if 0 <= hora < 7 or 22 <= hora <= 23:
    print('Es de noche.')
elif 7 <= hora < 15:
    print('Es de día.')
elif 15 <= hora < 22:
    print('Es por la tarde.')
else:
    print('Hora no válida.')

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: (0-69) insificiente, (70-79) bien, (80-89) muy bien, (90-100) excelente.
# 
# COMENTARIOS CORRECCIÓN:
# - El rango range(90,100) no incluye el 100.

calificacion_alumno = 70

rangos = {
    range(0, 70): 'Insuficiente',
    range(70, 80): 'Bien',
    range(80, 90): 'Muy bien',
    range(90, 101): 'Excelente'
}

for rango, texto in rangos.items():
    if calificacion_alumno in rango:
        print(f'La calificación del alumno es: {texto}')

# 40. Escribe una función que tome dos parámetros: *figura* (una cadena que puede ser 'rectángulo', 'círculo' o 'triángulo') y *datos* (una tupla con los datos necesario para calcular el área de la figura).
#
# COMENTARIOS CORRECCIÓN:
# - No se valida la longitud de la tupla de datos, lo que puede causar errores silenciosos.

# DEFINICIÓN DE LA FUNCIÓN
from math import pi

def calcular_area(figura, datos):

    if figura == 'rectangulo':
        if len(datos) != 2:
            raise ValueError('Rectángulo necesita base y altura.')
        return datos[0] * datos[1]
    
    elif figura == 'triangulo':
        if len(datos) != 2:
            raise ValueError('Triángulo necesita base y altura.')
        return (datos[0]*datos[1]/2)
    
    elif figura == 'circulo':
        if len(datos) != 1:
            raise ValueError('Círculo necesita el radio.')
        return pi*datos[0]**2

    else:
        raise ValueError('Figura no incluida.')
    

figura = 'triangulo'
datos = (7, 8)
print(calcular_area(figura, datos))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. 
# 
# El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.

try:
    precio_original = float(input('Introduce el precio del artículo: '))
    if precio_original <= 0:
        raise ValueError('El precio debe ser mayor que cero.')
    
    tiene_cupon = input('¿Dispone usted de un cupón de descuento? (si/no): ')

    precio_final = precio_original

    if tiene_cupon.lower() == 'si':
        valor_descuento = float(input('Por favor, introduce el valor del cupón de descuento (ej.: 15€): '))
        if valor_descuento > 0:
            precio_final = precio_original - valor_descuento
        else:
            raise ValueError('El valor del cupón introducido no es correcto.')

    print(f'El precio final del artículo es: {precio_final:.2f} €')

except ValueError as e:
    print(f'Error: {e}')