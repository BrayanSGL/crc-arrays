# Calculadora de CRC con multiples polinomios elegibles
Este programa permite calcular el código de redundancia cíclica (CRC) de una trama de datos utilizando distintos polinomios generadores elegidos por el usuario.

## Uso
Para utilizar el programa, primero se debe seleccionar un polinomio generador de la lista de polinomios disponibles. Luego, se debe ingresar la trama de datos a la que se le desea calcular el CRC en formato cadena de caracteres. El programa retornará el valor del CRC en formato binario y hexadecimal.

## Polinomios disponibles
- CRC-3/ROHC: polinomio generador x^3 + x^2 + 1
- CRC-3: polinomio generador x^3 + 1
- CRC-4/ITU: polinomio generador x^4 + x + 1
- CRC-8: polinomio generador x^8 + x^2 + x + 1
- CRC-16: polinomio generador x^16 + x^15 + x^2 + 1
- CRC-32: polinomio generador x^32 + x^29 + x^28 + x^24 + x^23 + x^22 + x^20 + x^19 + x^17 + x^16 + x^15 + 1
