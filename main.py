from ctypes import Array
import os

from numpy import array


POLYNOMIAL = {
    'CRC': 'CRC-32',
    'generator': 'x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1',
    'hexa': 0x104C11DB7,
    'binary': [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
}


def calc_crc(generator: Array, trama: Array) -> Array:
    i=0;
    crc=[]
    while len(generator) <= len(trama):
        for j in range(len(generator)):
            crc.append(trama[j]^generator[j])
        break 
    print(trama[:len(generator)])
    print(generator)   
    print(crc)

    #print(generator)
    #print(trama[:len(generator)])

def main():
    while True:
        # os.system('cls')
        print(' ------ Calculo de código CRC -------\n1.Ingrese cualquier cadena\n2.Ingrese: @Salir para cerrar el programa\n')
        string = input('# Ingrese la cadena de Texto > ')
        if string == '@Salir':
            print('------Programa terminado por el usuario-----')
            break

        # Paso 1: Recibo la trama y la convierto en binario
        binary_string = list(
            map(int, (''.join(format(ord(x), 'b') for x in string))))

       # print((binary_string))
        # Paso 2: Agrego el residuo a la trama
        for _ in range(len(POLYNOMIAL.get('binary'))-1):
            binary_string.append(0)

        #print((binary_string))
        #print(POLYNOMIAL.get('binary'))

        print('--------------')
        # Paso 3 Resolver la división
        calc_crc(generator=POLYNOMIAL.get('binary'),trama=binary_string)

        #print(POLYNOMIAL.get('binary')[0] ^ binary_string[1])
        # os.system('pause')


if __name__ == '__main__':
    main()
