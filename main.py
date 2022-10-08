import os


POLYNOMIAL = {
    'CRC': 'CRC-32',
    'generator': 'x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1',
    'hexa': 0x104C11DB7,
    'binary': 0b100000100110000010001110110110111
}


def main():
    while True:
        os.system('clear')
        print(' ------ Calculo de código CRC -------\n1.Ingrese caualquier cadena\n2.Ingrese: @Salir para cerrar el programa\n')
        string = input('# Ingrese la cadena de Texto > ')
        if string=='@Salir':
            print('------Programa terminado por el usuario-----')
            break
        binary_string = (''.join(format(ord(x), 'b') for x in string))
        print(binary_string)
        os.system('pause')


if __name__ == '__main__':
    main()
