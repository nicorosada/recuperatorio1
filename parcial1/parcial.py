import random
"""
NOMBRE = Rosada Nicolas
DNI = 46740101

El centro de estudiantes de la UTN FRA realiza unas elecciones para definir a su próximo
presidente/a
Para ello requieren un sistema que logre contar los votos positivos de cada uno de los
alumnos.
Cada partido político va a guardar lo siguiente (Estructurar la matriz como crean
conveniente):
-Nro de lista (número positivo 3 cifras)
-Cantidad de votos (Turno mañana)
-Cantidad de votos (Turno tarde)
-Cantidad de votos (Turno noche)
"""

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int) -> list:
    matriz = []  
    for i in range(cantidad_filas):
        fila = [0] * cantidad_columnas 
        matriz += [fila]  
    return matriz  

T_MA = 1
T_TA = 2
T_NO = 3
"""
1. Cargar Votos: Se realiza una carga secuencial de todos los votos de cada una de las
cinco listas.
NOTA: Validar todos los ing
"""


def cargar_secuencial(matriz: list) -> list:
    for fill_i in range(len(matriz)):
        lista = int(input("Ingrese la lista: "))
        while lista <= 99 or lista >= 1000:
            lista = int(input("ERROR/Ingrese la lista: "))        
        matriz[fill_i][0] = lista 
        for col_j in range(1, len(matriz[fill_i])):
            votos = int(input(f"Los votos para la lista {lista} del turno {col_j} son: "))
            matriz[fill_i][col_j] = votos
                
matriz = inicializar_matriz(3,4)
matriz2 = inicializar_matriz(2,4)

def sumar_votos(matriz: list) -> int: 
    cant_votos = 0
    for i in range(len(matriz)):
        for j in range(1, len(matriz[i])):
            votos = matriz[i][j]
            cant_votos += votos

    return cant_votos

            
"""
2. Mostrar Votos: Muestra en un lindo formato los siguientes datos:
Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche,Porcentaje Voto:
"""


def mostrar_matriz(matriz:list):
    for i in range(len(matriz)):
        suma_matriz = (matriz[i][1] + matriz[i][2] + matriz[i][3])
        porcentaje = round(suma_matriz * 100 / sumar_votos(matriz),2)
        print(f"El numero de Lista {matriz[i][0]} es \nVOTOS DEL TURNO MAÑANA: {matriz[i][1]}\nVOTOS DEL TURNO TARDE: {matriz[i][2]}\nVOTOS DEL TURNO NOCHE:: {matriz[i][3]}\nPORCENTAJE DE VOTOS: {(porcentaje)}%")


"""
3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de
votos que tuvieron en el turno mañana.
"""

def ordenar_may_men(matriz:list) -> list:
    for fil_i in range(len(matriz)-1): 
        for fil_j in range(fil_i + 1,len(matriz)):
            if matriz[fil_i][T_MA] < matriz[fil_j][T_MA]:
                aux = matriz[fil_i]
                matriz[fil_i] = matriz[fil_j]
                matriz[fil_j] = aux


"""
4. No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos
los votos
"""

def encontrar_menos_votos(matriz:list) -> list:
    contador_0 = 0
    for i in range(len(matriz)):
        suma_matriz = (matriz[i][1] + matriz[i][2] + matriz[i][3])
        porcentaje = round(suma_matriz * 100 / sumar_votos(matriz),2)
        if porcentaje < 5:
            print(f"La lista {matriz[i][0]} está por debajo del 5% con {suma_matriz} votos.")
            contador_0 += 1
    if contador_0 == 0:
        print("Ninguna lista está por debajo del 5%")
                
    

"""
5.Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos
fueron a votar.
"""

def mostrar_mayor_votos(matriz:list) -> list:
    turno_mañana = 0
    turno_tarde = 0
    turno_noche = 0
    for i in range(len(matriz)):
        turno_mañana = turno_mañana + matriz[i][1]
        turno_tarde = turno_tarde + matriz[i][2]
        turno_noche = turno_noche + matriz[i][3]

    if turno_mañana > turno_tarde and turno_mañana > turno_noche:
        print("El Turno que mas fue a votar fue el de la mañana")
    elif turno_tarde > turno_noche:
        print("El Turno que mas fue a votar fue el de la tarde")
    else:
        print("El Turno que mas fue a votar fue el de la noche")

"""
6.Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única
forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.
"""

def verificar_ballotage(matriz:list) -> bool:
    bandera = True
    for i in range(len(matriz)):
        suma_matriz = (matriz[i][1] + matriz[i][2] + matriz[i][3]) 
        porcentaje = round(suma_matriz * 100 / sumar_votos(matriz),2)
        if porcentaje > 50:
            bandera = False
            if bandera == False:
                print(f"No se necesita hacer ballotage")
                break
        else:
            print("Se necesita hacer ballotage")
            break
    
    return bandera


"""
7.Realizar segunda vuelta:Se encarga de realizar la segunda vuelta electoral con los
dos candidatos más votados. Se le pide al usuario la cantidad de alumnos que fueron
a votar en cada turno en la segunda vuelta y de manera random se calculan los votos
del primer y segundo candidato en cada turno. Al final de ello se calcula el porcentaje
final de cada lista y se muestra al ganador de las elecciones.
NOTA: Solo se accede si hay la opción 6 verificó que hay segunda vuelta, sino indicar
que no hubo segunda vuelta.
"""    

def ordenar_may_men_todos(matriz: list) -> list:
    for fil_i in range(len(matriz) - 1):
        for fil_j in range(fil_i + 1, len(matriz)):
            for col in range(1, len(matriz[0])):
                if matriz[fil_i][col] < matriz[fil_j][col]:
                    aux = matriz[fil_i]
                    matriz[fil_i] = matriz[fil_j]
                    matriz[fil_j] = aux
                    break

    return matriz

def crear_matriz_ballotage(matriz:list,matriz2:list)-> list:
    ordenar_may_men_todos(matriz)
    turno_mañana = 0
    turno_tarde = 0
    turno_noche = 0

    for i in range(len(matriz)):
        turno_mañana = turno_mañana + matriz[i][1]
        turno_tarde = turno_tarde + matriz[i][2]
        turno_noche = turno_noche + matriz[i][3]

    for i in range(len(matriz2)):
        matriz2[i][0] = matriz[i][0] 
        matriz2[i][1] = turno_mañana
        matriz2[i][2] = turno_tarde
        matriz2[i][3] = turno_noche

    return matriz2
    
def generar_random(matriz:list,matriz2:list) -> list:
    crear_matriz_ballotage(matriz,matriz2)
    for i in range(1,4):
        votos_totales = matriz2[0][i]
        votos_lista1 = random.randint(1,votos_totales)
        votos_lista2 = votos_totales - votos_lista1
        matriz2[0][i] = votos_lista1 
        matriz2[1][i] = votos_lista2

    return matriz2

def generar_porcentaje_final(matriz:list,matriz2:list) -> list:
    generar_random(matriz,matriz2)
    votos_totales = sumar_votos(matriz)
    lista_porc = [0] * len(matriz2)
    for i in range(len(matriz2)):
        suma_matriz = (matriz2[i][1] + matriz2[i][2] + matriz2[i][3]) 
        lista_porc[i] = round((suma_matriz * 100) / votos_totales,2)
    
    return lista_porc

def mostrar_ballotage_final(matriz:list,matriz2:list) -> list:
    lista_porc = generar_porcentaje_final(matriz,matriz2)
    if lista_porc[0] > lista_porc[1]:
        print(f"La lista numero {matriz[0][0]} con el {lista_porc[0]}% ha sido la ganadora.")
    else:
        print(f"La lista numero {matriz[1][0]} con el {lista_porc[1]}% ha sido la ganadora.")


def menu():
    bandera = True
    bandera2 = True
    print (f"**** ELECCIONES ELECTORALES UTN ****")
    while True:
        print("\nMenu de Opciones:")
        print("\n1. Cargar Votos")
        print("2. Mostrar Votos")
        print("3. Ordenar los votos del turno Mañana")
        print(f"4. Mostrar la lista que tuvo menos de 5% de los votos")
        print("5. Mostrar turno mas votado")
        print("6. Hay Ballotage?")
        print("7. Realizar segunda vuelta")
        print("8. Salir")

        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            cargar_secuencial(matriz)
            bandera = False
        elif opcion == 2:
            if bandera == False:
                mostrar_matriz(matriz)
            else:
                print("Todavia no se ingresó ninguna lista")
        elif opcion == 3:
            if bandera == False:
                ordenar_may_men(matriz)
                print("Se ha Ordenado Correctamente")
            else:
                print("Todavia no se ingresó ninguna lista")
        elif opcion == 4:
            if bandera == False:
                encontrar_menos_votos(matriz)
            else:
                print("Todavia no se ingresó ninguna lista")
        elif opcion == 5:
            if bandera == False:
                mostrar_mayor_votos(matriz)
            else:
                print("Todavia no se ingresó ninguna lista")
        elif opcion == 6:
            if bandera == False:
                verificar_ballotage(matriz)
                bandera2 = False
            else:
                print("Todavia no se ingresó ninguna lista")
        elif opcion == 7:
            if bandera2 == False:
                mostrar_ballotage_final(matriz,matriz2)
            else:
                print("Todavia no se verifico si hay segunda vuelta.")
        elif opcion == 8:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

menu()