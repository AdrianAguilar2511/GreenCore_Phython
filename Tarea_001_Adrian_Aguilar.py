"""
Tarea 001
Profesor: Pedro Guzman
Author: Adrian Aguilar
Fecha: 11 02 2018
Cree un programa que solicite dos números. Verifique que estos números son positivos
y verifique que el primero número es menor por al menos 50 que el segundo número.
Si los números ingresados son correctos, el programa debe calcular la suma de todos los números
entre el primer número y el segundo que son múltiplos de 5 y múltiplos de 3
"""


# Variable Definition

numero_positivo_001 = -1
numero_positivo_002 = -1
go_numero_uno = False
go_numero_dos = False

exit_validar_numero_positivo = False
exit_validar_numero_mas_50 = False
exit_multiplo_de_5 = False

# Function definition

def encabezado_del_programa():
    print("----------------------------------------------------------------------")
    print("------------------------Tarea 01 GreenCore----------------------------")
    print("----------------------------------------------------------------------")


def fin_del_programa():
    print("----------------------------------------------------------------------")
    print("------------------------Fin del Programa------------------------------")
    print("----------------------------------------------------------------------")


def validar_numero_positivo(numero_uno):
    if numero_uno > 0:
        print("Numero es positivo es Correcto")
        exit_validar_numero_positivo = True
    else:
        print("Numero es negativo NO es Correcto")
        exit_validar_numero_positivo = False
    return exit_validar_numero_positivo

def validar_numero_mas_50(numero_uno,numero_dos):
    numero_mayor_50 = numero_dos - numero_uno

    if numero_mayor_50 > 49:
        print("Segundo numero es correcto > 50")
        exit_validar_numero_mas_50 = True
    else:
        print("Segundo numero NO es correcto")
        print("Recuerde el segundo numero 50 veces mayor que el primero")
        exit_validar_numero_mas_50 = False
    return exit_validar_numero_mas_50


def sumar_numeros_multiplos(numero_uno,numero_dos):
    suma_de_numeros_positivos = 0;
    for contador_de_num_positivos in range(numero_positivo_001, numero_positivo_002):
        ##if (multiplo_de_5(numero_uno,numero_dos)):
        suma_de_numeros_positivos = contador_de_num_positivos + suma_de_numeros_positivos
        print(suma_de_numeros_positivos)
    return suma_de_numeros_positivos

def multiplo_de_5(numero_uno,numero_dos):
    multiplo_5_mod = numero_uno % 2 # debe ser cero
    multiplo_5_res = numero_uno / 5 # debe ser 5

    if ( multiplo_5_mod == 0 ) and (multiplo_5_res == 0 and multiplo_5_res == 5 ):
        print("numero multiplo de 5",str(multiplo_5_mod))
        print("numero multiplo de 3",str(multiplo_5_res))
        exit_multiplo_de_5 = True
    else:
        print("Segundo numero NO es correcto")
        print("Recuerde el segundo numero 50 veces mayor que el primero")
        exit_multiplo_de_5 = False

    return exit_multiplo_de_5

# Main Program

if __name__== "__main__":
    encabezado_del_programa()

    while not go_numero_uno:
        numero_positivo_001 = int(input("Ingrese un número mayor que 0: "))
        go_numero_uno=validar_numero_positivo(numero_positivo_001)

    while not go_numero_dos:
        numero_positivo_002 = int(input("Ingrese un mumero 50 veces mayor que el primero: "))
        go_numero_dos=validar_numero_mas_50(numero_positivo_001,numero_positivo_002)

   # sumar_numeros_multiplos(numero_positivo_001,numero_positivo_002)
    r = validar_numero_mas_50(numero_positivo_001,numero_positivo_002)
    print(str(r))
    fin_del_programa()
