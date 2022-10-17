from ctypes import Array
import os

from numpy import array


POLYNOMIAL = [
    {
        'CRC': 'CRC-32',
        'code': 32,
        'generator': 'x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1',
        'hexa': 0x104C11DB7,
        'binary': [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    },
    {'CRC': 'CRC-3',
        'code': 3,
        'generator': 'x3 + x2 + 1',
        'hexa': 0x104C11DB7,
        'binary': [1, 1, 0, 1]
     }

]

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
    binary_of_generator = generator[0].get('binary')
    while True:
        # Paso 3.1: Obtener el residuo
        print('----------VUELTA----------')
        residuo = xor(binary_of_generator, trama[:len(binary_of_generator)])
        print('generador')
        print(binary_of_generator)
        print('trama con el tamaño del generador')
        print(trama[:len(binary_of_generator)])
        print('Residuo')

        print(residuo)

        # Paso 3.2: Quitar los ceros a la izquierda de residuo si existen
        ceros = 0
        try:
            while residuo[0] == 0:
                ceros += 1
                residuo.pop(0)
        except IndexError:
            return [0] * len(binary_of_generator)

        # Paso 3.3: Recortar la trama la cantidad de ceros a la izquierda
        print('trama original')
        print(trama)
        trama = trama[len(binary_of_generator):]
        print('Trama recortada: ')
        print(trama)

        trama = residuo + trama
        print('Trama con residuo: ')
        print(trama)


        # Paso 3.3: Verificar si la trama ya esta dividida
        if len(trama) < len(binary_of_generator):
            # agregar a residuo seros a la izquierda hasta que tenga longitud 3
            while len(residuo) < generator[0].get('code'):
                residuo.insert(0, 0)
            return residuo

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
        print('Trama en binario: ', binary_string)

        # Paso 2: Agrego el residuo a la trama
        for _ in range(len(POLYNOMIAL[0].get('binary'))-1):
            binary_string.append(0)
        print('Trama con residuo: ', binary_string)

        # Paso 3 Resolver la división
        #binary_string = [1, 1, 1, 1, 0, 1, 0, 0, 0]
        crc = calcular_crc(generator=POLYNOMIAL, trama=binary_string)
        print('Residuo: ', crc)
        os.system('pause')

        #Comprobacion de CRC
        
        comprobacion = calcular_crc(generator=POLYNOMIAL, trama=binary_string+crc)
        print('Comprobacion: ', comprobacion)
        os.system('pause')

if __name__ == '__main__':
    main()
