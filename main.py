from ctypes import Array
import os

from numpy import array


POLYNOMIAL = {
    'CRC': 'CRC-32',
    'code': 32,
    'generator': 'x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1',
    'hexa': 0x104C11DB7,
    'binary': [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
}

POLYNOMIAL2 = {
    'CRC': 'CRC-3',
    'code': 3,
    'generator': 'x3 + x2 + 1',
    'hexa': 0x104C11DB7,
    'binary': [1, 1, 0, 1]
}


def xor(a, b):
    return [int(x) ^ int(y) for x, y in zip(a, b)]


def calcular_crc(generator: Array, trama: Array) -> Array:

    while True:
        # Paso 3.1: Obtener el residuo
        print('----------VUELTA----------')
        residuo = xor(generator, trama[:len(generator)])
        print('generador')
        print(generator)
        print('trama con el tamaño del generador')
        print(trama[:len(generator)])
        print('Residuo')

        print(residuo)

        # Paso 3.2: Quitar los ceros a la izquierda de residuo
        ceros = 0
        while residuo[0] == 0:
            ceros += 1
            residuo.pop(0)

        # Paso 3.3: Recortar la trama la cantidad de ceros a la izquierda
        print('trama original')
        print(trama)
        trama = trama[len(generator):]
        print('Trama recortada: ')
        print(trama)

        trama = residuo + trama
        print('Trama con residuo: ')
        print(trama)

        input('Paso 3.3')

        # Paso 3.3: Verificar si la trama ya esta dividida
        if len(trama) < len(generator):
            # agregar a residuo seros a la izquierda hasta que tenga longitud 3
            while len(residuo) < 3:
                residuo.insert(0, 0)
            print('residuo final', residuo)
            break


'''def calcular_crc(generator: Array, trama: Array) -> Array:
    ceros = 0
    # Recortamos la trama para que sea igual al generador, la guardamos en una variable temporal
    temp = trama[:len(generator)]
    # Realizamos la operación XOR entre temp y el generador
    residuo = xor(temp, generator)

    print(generator)
    print(temp)
    print(residuo)

    # Eliminamos los ceros a la izquierda de residuo
    while residuo[0] == 0:
        ceros += 1
        residuo.pop(0)

    #Recorto a ceros la trama
    trama = trama[ceros:]

    # Si el residuo es mayor que la trama, significa que ya se terminó la división
    if len(residuo) > len(trama):
        print('Residuo: ', residuo)
        print('Trama: ', trama)
        return residuo
'''


def main():
    while True:
        os.system('cls')
        print(' ------ Calculo de código CRC -------\n1.Ingrese cualquier cadena\n2.Ingrese: @Salir para cerrar el programa\n')
        string = input('# Ingrese la cadena de Texto > ')
        if string == '@Salir':
            print('------Programa terminado por el usuario-----')
            break

        # Paso 1: Recibo la trama y la convierto en binario
        binary_string = list(
            map(int, (''.join(format(ord(x), 'b') for x in string))))
        #print('Trama en binario: ', binary_string)

        # Paso 2: Agrego el residuo a la trama
        for _ in range(len(POLYNOMIAL2.get('binary'))-1):
            binary_string.append(0)
        #print('Trama con residuo: ', binary_string)

        # Paso 3 Resolver la división
        binary_string = [1, 1, 1, 1, 0, 1, 0, 0, 0]
        calcular_crc(generator=POLYNOMIAL2.get('binary'), trama=binary_string)

        os.system('pause')


if __name__ == '__main__':
    main()
