# Tema 1 - Algoritmos y estructuras de datos

En este primer tema nos centraremos en conocer los tipos básicos de datos comunes a la mayoría de los lenguajes de programación. Veremos peculiaridades de Python y nos centraremos en las principales estructuras básicas de la programación como son:
- Las estructuras secuenciales.
- Las estructuras condicionales.
- Las estructuras repetitivas o bucles.

Veremos también típicas soluciones a ejercicios básicos, problemas de conversión de tipos, las peculiaridades de un lenguaje de tipado dinámico como es Python y también pequeñas peculiaridades de que sea interpretado en lugar de compilado.

## Glosario de términos generales

- [Glosario](./apuntes_y_ejemplos/glosario.md)

## Apuntes y ejemplos

- [Estructuras básicas de programación](./apuntes_y_ejemplos/estructuras_basicas.py)
- [Operadores básicos de Python](./apuntes_y_ejemplos/operadores_basicos.py)
- [Las sentencias break y continue](./apuntes_y_ejemplos/ejemplo_break_continue.md)
- [Funciones básicas con cadenas](./apuntes_y_ejemplos/funciones_basicas_con_cadenas.py)
- [Comprobando tipos de datos](./apuntes_y_ejemplos/comprobadores_tipos.md)
- [Ejercicio bucles y letras grandes - ejemplo "U"](apuntes_y_ejemplos/ercicio_tipo_examen.mdx)
- [Ejemplo de una posible solución del examen](./solucionario/sol_examen_ud1.py)

## Enunciados ejercicios

### Ejercicio 1

Diseñar un algoritmo que convierta una temperatura leída en grados Farenheit a  grados Celsius, usando la fórmula: C=(5/9)*(F-32).

### Ejercicio 2

Diseñar un algoritmo que calcule y muestre en pantalla el volumen y el área de una esfera para un radio dado

### Ejercicio 3

Diseñar un algoritmo que pida una nota (valor entero) por teclado y dependiendo de su valor visualice la nota en letras. Por ejemplo, si nota es igual a 7 tiene que mostrar el texto "Notable".

### Ejercicio 4

Diseñar un algoritmo que lea 20 caracteres de teclado y muestre por pantalla el número de veces que se repiten cada una de las vocales.

### Ejercicio 5

Diseñar un algoritmo que lea del teclado dos números enteros y un carácter. El caracter puede ser +, -, *, /, %, ^, y en  función del carácter introducido se mostrará el resultado de la operación correspondiente. 
Por ejemplo, si se introduce '7', '3' y '+' se mostrará 10.

### Ejercicio 6

Diseñar un algoritmo que obtenga el promedio de una lista de varlores reales leídos por teclado. El algoritmo
terminará cuándo el usuario introduzca 20 valores.

### Ejercicio 7

Diseñar un algoritmo que calcule y muestre en pantalla el factorial de un número entero dado.

### Ejercicio 8

Realizar un algoritmo que calcule y muestre en la pantalla la suma de los n primeros enteros impares. El valor de n se solicitará al usuario.

### Ejercicio 9

Diseñar un algoritmo que calcule la suma de todos los números comprendidos entre 1 y 500 que cumplan la condición de ser múltiplos de 5 y de 7. Para verificar si un número X es múltiplo de otro número Y, basta con comprobar si el resto de la división entera de X entre Y es igual a 0.

### Ejercicio 10

Implementar un programa que verifique si un texto es "Twiteable" (tiene 280 caracteres o menos) o no. El programa debe pedir un texto por teclado y mostrar un mensaje indicando si el texto es Twiteable o no.

### Ejercicio 11

Diseñar un algoritmo que lea del teclado un número entero correspondiente a una cantidad de minutos y nos diga cuántos días, horas y minutos son. Por ejemplo, si introducimos 1000 minutos, el algoritmo mostrará por pantalla que son 0 días, 16 horas y 40 minutos.

### Ejercicio 12

Diseñar un algoritmo que lea del teclado tres números enteros y escriba en pantalla un mensaje indicando si
al menos dos de esos tres números son pares.

### Ejercicio 13

Diseñar un algoritmo, que dados dos números, determine si su producto es positivo, nulo o negativo, sin realizar la multiplicación.

### Ejercicio 14

Diseñar un algoritmo que calcule la potencia para dos números naturales x e y mediante una acumulación sucesiva de productos. Previo al cálculo se verificará que ambos valores son positivos.

### Ejercicio 15

Diseñar un algoritmo que lea una secuencia de 20 números reales introducidos por teclado. Al acabar
la secuencia, debe mostrar el valor máximo y mínimo introdcidos.

### Ejercicio 16

Diseñar un algoritmo que pida al usuario un número del 1 al 9 y le conteste diciendo si el número es primo o no. Por ejemplo, si el usuario introduce el número 7, el algoritmo le responderá que 7 es un número primo.

### Ejercicio 17

Diseñar un algoritmo que lea números enteros positivos de teclado y sólo acepte como válidos aquellos que sean mayores que el anterior número leído. El algoritmo terminará cuando se introduzca el 0.

### Ejercicio 18

Diseñar un algoritmo que lea una lista de 10 números enteros, visualice la suma de los pares, cuántos pares existen y cuál es la media aritmética de los números impares.  

### Ejercicio 19

Diseñar un algoritmo que lea un conjunto de números reales, los cuente y calcule y muestre la media, varianza y la desviación típica del conjunto de números. La media y la varianza se calculan con las fórmulas:    
- Media = (suma de los números) / (número de números).
- Varianza = ((suma de los cuadrados de los números) - (suma de los números)^2 / (número de números)).
- La desviación típica es la raíz cuadrada de la varianza. 

### Ejercicio 20

Diseñar un algoritmo que lea un número entero de teclado, visualice sus dígitos y calcule la suma de los dígitos que sean pares. Para extraer los dígitos de un número usaremos un bucle que divida el número por 10 sucesivamente. El resto de cada división corresponde a cada uno de los dígitos.

## Solucionario

1. [Farenheit a Celsius](./solucionario/ej1.py)
2. [Volumen y Área de una esfera](./solucionario/ej2.py)
3. Notas en letras
   1. [Versión con ifs](./solucionario/ej3.py)
   2. [Versión con match-case](./solucionario/ej3b.py)
   3. [Versión con if-elif-else](./solucionario/ej3c.py)
4. Contar vocales
   1. [Versión básica](./solucionario/ej4.py)
   2. [Versión avanzada (uso diccionario)](./solucionario/ej4b.py)
5. [Calculadora sencilla](./solucionario/ej5.py)
6. [Calculo del promedio](./solucionario/ej6.py)
7. [Calculo del factorial](./solucionario/ej7.py)
8. [Calculo de los n primeros impares](./solucionario/ej8.py)
9. [Suma de los múltiplos de 5 y 7](./solucionario/ej9.py)
10. [Texto "Tuiteable"](./solucionarioej10.py)
11. [Conversor minutos a días-horas-minutos](./solucionarioej11.py)
12. [Identificador de pares](./solucionarioej12.py)
13. [Producto sin operar](./solucionario/ej13.py)
14. Cálculo de la potencia por acumulación de productos.
    1.  [Versión básica](./solucionario/ej14.py)
    2.  [Versión comprobando números hasta operar](./solucionario/ej14b.py)
15. [Mínimo y máximo de la secuencia](./solucionario/ej15.py)
16. [Primos o no primos](./solucionario/ej16.py)
17. [Secuencia de números ascendente](./solucionario/ej17.py)
18. [Suma de pares, conteo y media impares](./solucionario/ej18.py)
19. [Cálculo de la media, varianza y desviación](./solucionario/ej19.py)
20. [Extractor de dígitos](./solucionario/ej20.py)

## Laboratorios del curso resueltos

- [Laboratorio 2.1.1.6](./labs/lab2-1-1-6.py)
- [Laboratorio 2.1.1.18](./labs/lab2-1-1-18.py)
- [Laboratorio 2.1.1.19](./labs/lab2-1-1-19.py)
- [Laboratorio 2.2.1.11](./labs/lab2-2-1-11.py)
- [Laboratorio 2.4.1.7](./labs/lab2-4-1-7.py)
- [Laboratorio 2.4.1.9](./labs/lab2-4-1-9.py)
- [Laboratorio 2.4.1.10](./labs/lab2-4-1-10.py)
- [Laboratorio 2.5.1.2](./labs/lab2-5-1-2.py)
- [Laboratorio 2.6.1.9](./labs/lab2-6-1-9.py)
- [Laboratorio 2.6.1.10](./labs/lab2-6-1-10.py)
- [Laboratorio 2.6.1.11](./labs/lab2-6-1-11.py)
- [Laboratorio 3.1.1.4](./labs/lab3-1-1-4.py)
- [Laboratorio 3.1.1.10](./labs/lab3-1-1-10.py)
- [Laboratorio 3.1.1.11](./labs/lab3-1-1-11.py)
- [Laboratorio 3.1.1.12](./labs/lab3-1-1-12.py)
- [Laboratorio 3.2.1.9](./labs/lab3-1-1-9.py)
- [Laboratorio 2.6.1.11](./labs/lab2-6-1-11.py)

### Así resolvimos los ejercicios en clase:
[Soluciones clase](./soluciones_clase/)
