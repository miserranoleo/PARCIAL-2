#Ejercicio 3: La Magia de las Listas Numéricas
#Crea una función llamada magia_numerica() que realice varias transformaciones en una lista de números sin modificar la lista original. Las tareas son las siguientes:
#Eliminar los elementos duplicados.
#Ordenar la lista de mayor a menor.
#Eliminar todos los números impares.
#Sumar todos los números que quedan.
#Colocar esta suma como el primer elemento de la lista.
#Verifica que la suma de todos los números a partir del segundo elemento es igual al primer número de la lista.

import random

def generar_lista_numeros(n):
    return [random.randint(1, 20) for _ in range(n)]

def magia_numerica(lista_numeros):
    # 1. Eliminar elementos duplicados
    lista_sin_duplicados = list(set(lista_numeros))

    # 2. Ordenar la lista de mayor a menor
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)

    # 3. Eliminar todos los números impares
    lista_pares = [num for num in lista_ordenada if num % 2 == 0]

    # 4. Sumar todos los números que quedan
    suma_total = sum(lista_pares)

    # 5. Colocar esta suma como el primer elemento de la lista
    lista_final = [suma_total] + lista_pares

    # Verificar que la suma de todos los números a partir del segundo elemento es igual al primer número de la lista
    verificacion = suma_total == sum(lista_final[1:])

    return lista_final, verificacion

# Ejemplo de uso
nueva_lista = generar_lista_numeros(10)
resultado, verificacion = magia_numerica(nueva_lista)

print(f"Lista original: {nueva_lista}")
print(f"Resultado después de la magia: {resultado}")
print(f"Verificación: {verificacion}")
