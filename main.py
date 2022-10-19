from ctypes import Array
import os


POLYNOMIAL = {
    'CRC': 'CRC-16',
    'code': 16,
    'generator': 'P(x) = x^16 + x^15 + x^2 + 1',
    'hexa': '0x18005',
    'binary': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
}

#insertar un 0 cada 8 posiciones de izquuierda a derecha
def convert_a_binario(string):
    binario = ''
    for i in string:
        binario += f'{ord(i):08b}'
    return binario

#Convertir string a vector
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


def calcular_residuo(generator: Array, trama: Array) -> Array:
    while True:
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

        # Paso 3.3: Recortar la trama la cantidad de ceros a la izquierda
        trama = trama[len(generator):]

        trama = residuo + trama

        if len(trama) <= len(generator):
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

        # Paso 1: Recibo la trama y la convierto en binario
        binary_string = convert_a_vector(convert_a_binario(string))

        os.system('cls')
        print('-----------Resultado----------- \n')
        print('Texto ingresado: ', string)
        print('Texto en binario: ', convertir_a_string(binary_string))
        print('Polinomio generador: ', POLYNOMIAL.get(
            'CRC'), '|', POLYNOMIAL.get('generator'), '|', POLYNOMIAL.get('hexa'), '|', convertir_a_string(POLYNOMIAL.get('binary')))

        # Paso 2: Agrego el residuo a la trama

        for _ in range(len(POLYNOMIAL.get('binary'))-1):
            binary_string.append(0)

        # Paso 3 Resolver la división
        residuo = calcular_residuo(POLYNOMIAL.get('binary'), binary_string)

        for _ in range(len(POLYNOMIAL.get('binary'))-1):
            binary_string.pop(-1)

        print('Residuo de la división: ', convertir_a_string(residuo))
        print('Secuencia binaria de datos para la detección de errores: ',
              convertir_a_string(binary_string+residuo))
        os.system('pause')



        # Comprobacion de CRC


if __name__ == '__main__':
    main()
