# Programa para el calculo de CRC con multiples polinomios alegibles
# Hecho por: Brayan Snader Galeano Lara
# @brayangaleanolara

from ctypes import Array
import os

POLYNOMIAL = [
    {
        'CRC': 'CRC-3/ROHC',
        'generator': 'x^3 + x^2 + 1',
        'hexa': '0x3',
        'binary': [1, 1, 0, 1]
    },
    {
        'CRC': 'CRC-3',
        'generator': 'x^3 + 1',
        'hexa': '0x##',
        'binary': [1,0,0,1]
    },
    {
        'CRC': 'CRC-4/ITU',
        'generator': 'x^4 + x + 1',
        'hexa': '0x##',
        'binary': [1, 0, 0, 1, 1]

    },
    {
        'CRC': 'CRC-8',
        'generator': 'x^8 + x^2 + x + 1',
        'hexa': '0x107',
        'binary': [1, 0, 0, 0, 0, 0, 1, 1, 1]
    },
    {
        'CRC': 'CRC-16',
        'generator': 'P(x) = x^16 + x^15 + x^2 + 1',
        'hexa': '0x18005',
        'binary': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    },
    {
        'CRC': 'CRC-32',
        'generator': 'P(x) = x^32 + x^29 + x^28 + x^24 + x^23 + x^22 + x^20 + x^19 + x^17 + x^16 + x^15 + 1',
        'hexa': '0x4C11DB7',
        'binary': [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    }
]


def convert_a_binario(string):
    binario = ''
    for i in string:
        binario += f'{ord(i):08b}'
    return binario


def convert_a_vector(string):
    vector = []
    for i in string:
        vector.append(int(i))
    return vector


def convertir_a_string(arreglo):
    string = ''
    for i in arreglo:
        string += str(i)
    return string


def xor(a, b):
    return [int(x) ^ int(y) for x, y in zip(a, b)]


def menu_polinomios():

    while True:
        os.system('cls')
        print('Lista de polinomios: \n')
        for i in range(len(POLYNOMIAL)):
            print(i+1, '. ', POLYNOMIAL[i].get('CRC'), '|', POLYNOMIAL[i].get('generator'), '|',
                  POLYNOMIAL[i].get('hexa'), '|', convertir_a_string(POLYNOMIAL[i].get('binary')))
        try:
            index_polinomio = int(
                input('\n# Ingrese el numero del polinomio que desea usar > '))

            if index_polinomio > len(POLYNOMIAL) or index_polinomio < 1:
                raise ValueError
            else:
                return index_polinomio-1
        except ValueError:
            print('Error: Ingrese un numero valido')
            os.system('pause')


def calcular_residuo(generator: Array, trama: Array) -> Array:
    while True:
        # print('------------Vuelta------------')
        # Paso 3.1: Obtener el residuo
        residuo = xor(generator, trama[:len(generator)])
        # Paso 3.2: Quitar los ceros a la izquierda de residuo si existen
        ceros = 0
        try:
            while residuo[0] == 0:
                ceros += 1
                residuo.pop(0)
        except IndexError:
            return [0] * len(generator)

        #print('Residuo: ', convertir_a_string(residuo))
        #input('Presione enter para continuar')
        # Paso 3.3: Recortar la trama la cantidad de ceros a la izquierda
        trama = trama[len(generator):]
        trama = residuo + trama

        if len(trama)+1 <= len(generator):
            # agregar a residuo seros a la izquierda hasta que tenga longitud 3
            while len(trama) < len(generator)-1:
                trama.insert(0, 0)
            return trama


def main():
    while True:
        os.system('cls')
        print(' ------ Calculo de código CRC -------\n \n1.Ingrese cualquier cadena\n2.Ingrese: @Salir para cerrar el programa\n')
        string = input('# Ingrese la cadena de Texto > ')
        if string == '@Salir':
            print('------Programa terminado por el usuario-----')
            break

        p = menu_polinomios()

        # Paso 1: Recibo la trama y la convierto en binario
        binary_string = convert_a_vector(convert_a_binario(string))

        os.system('cls')
        print('-----------Resultado----------- \n')
        print('Texto ingresado: ', string)
        print('Texto en binario: ', convertir_a_string(binary_string))
        print('Polinomio generador: ', POLYNOMIAL[p].get(
            'CRC'), '|', POLYNOMIAL[p].get('generator'), '|', POLYNOMIAL[p].get('hexa'), '|', convertir_a_string(POLYNOMIAL[p].get('binary')))

        # Paso 2: Agrego el residuo a la trama

        for _ in range(len(POLYNOMIAL[p].get('binary'))-1):
            binary_string.append(0)

        # Paso 3 Resolver la división

        residuo = calcular_residuo(POLYNOMIAL[p].get('binary'), binary_string)

        for _ in range(len(POLYNOMIAL[p].get('binary'))-1):
            binary_string.pop(-1)

        print('Residuo de la división: ', convertir_a_string(residuo))
        print('Secuencia binaria de datos para la detección de errores: ',
              convertir_a_string(binary_string+residuo))

        # Comprobacion de CRC
        residuo_verific = calcular_residuo(
            POLYNOMIAL[p].get('binary'), binary_string+residuo)
        verificacion = True if residuo_verific == [
            0] * len(POLYNOMIAL[p].get('binary')) else False
        print('Trama procesada correctammente :', verificacion,
              '\nResiduo de la verificación: ', convertir_a_string(residuo_verific))

        os.system('pause')


if __name__ == '__main__':
    main()
