import numpy as np
from funciones import*
from persona import*

arreglo = np.full((10,10),'---')
lista_asistente = []
ciclo = True


def agregarasistente(lista_asistente,num_asiento):
    p = persona()
    p.run = int(input('ingrese rut: '))
    p.num_asiento = num_asiento
    if num_asiento >= 1 and num_asiento <= 20:
        p.valor = 120000
    if num_asiento >= 21 and num_asiento<=50:
        p.valor = 80000
    if num_asiento >= 51 and num_asiento <= 100:
        p.valor= 50000
    lista_asistente.append(p)

def comprarboleto(arreglo,lista_asistente):
    try:
        ubicaciones = int(input('ingrese cantidad a comprar (1-3): '))
        if ubicaciones >= 1 and ubicaciones <= 3:
            compra = 0
            while compra < ubicaciones:
                mostrar(arreglo)
                num_asiento = int(input('ingrese el numero de asiento : '))
                if num_asiento>= 1 and num_asiento <= 100:
                    disponible = comprobarasiento(arreglo,num_asiento)
                    if disponible == True:
                        agregarasistente(lista_asistente,num_asiento)
                        comprar(arreglo,num_asiento)
                        compra = compra + 1
                    else:
                        print("no esta disponible")
                else:
                    print('ingrese del 1 a 100')
        else:
            print('ingrese ubicaciones de 1 a 3')
    except:
        print('Ingrese de nuevo')

def listaasistentes(lista_asistente):
    for p in lista_asistente:
        print(f'Rut Asistente: {p.run}')


def salir():
    print('hasta luego!')

    return False


llenar(arreglo)

ciclo = True

while ciclo:
    print('-----creativos.cl-----')
    print('1) Comprar entradas')
    print('2) Mostrar ubicaciones disponibles')
    print('3) Ver listado de asistentes')
    print('4) Mostrar ganancias totales')
    print('5) Salir')
    try:
        op = int(input('Ingrese una opcion: '))
        match op:
            case 1:
                comprarboleto(arreglo,lista_asistente)

            case 2:
                mostrar(arreglo)

            case 3:
                listaasistentes(lista_asistente)
            case 4:
                print('mostrar ganancias')
            case 5:
                ciclo = salir()
    except:
        print('ingrese opcion correcta')






