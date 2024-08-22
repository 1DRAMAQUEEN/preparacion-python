# intro-dev-lab-04

### Introducción al Valor Absoluto

El valor absoluto de un número se refiere a su magnitud sin tener en cuenta su signo. Es decir, es la distancia que hay entre el número y el cero en la recta numérica. Se denota como \(|n|\), donde \(n\) es cualquier número real. El valor absoluto siempre es un número no negativo.

Por ejemplo, el valor absoluto de \(-3\) es 3, porque la distancia entre \(-3\) y 0 en la recta numérica es 3. Del mismo modo, el valor absoluto de \(3\) es también 3, ya que está a la misma distancia de 0, pero en la dirección opuesta.

#### Ejemplo: Encontrar la distancia entre dos números utilizando el valor absoluto

Vamos a usar un ejemplo simple para entender cómo se aplica el valor absoluto para encontrar la distancia entre dos números, como \(15\) y \(4\).

#### Paso 1: Restar los números

Primero, restamos uno de los números del otro:

\[
15 - 4 = 11
\]

#### Paso 2: Tomar el valor absoluto

Luego, tomamos el valor absoluto del resultado, aunque en este caso no es necesario porque el resultado es positivo:

\[
|11| = 11
\]

Así que, la distancia entre \(15\) y \(4\) es \(11\) unidades en la recta numérica.

### Orden inverso: 

Este proceso también funciona si restamos en el orden inverso:

\[
4 - 15 = -11
\]

Tomamos el valor absoluto:

\[
|-11| = 11
\]

De nuevo, la distancia es \(11\) unidades, independientemente del orden de la resta.


Si te fijas, sin importar el orden en que hagamos la resta entre los 2 números, siempre el resultado es el mismo, por lo cuál, siempre podremos calcular la distancia entre 2 números usando el valor absoluto.

#### Usando el valor absoluto en Python

Podemos usar Python para realizar cálculos sobre la distancia entre 2 números de manera rápida y sencilla. Aquí tienes un ejemplo de cómo hacerlo:

```python
# Definir los números
num1 = 15
num2 = 4

# Calcular la distancia usando valor absoluto
distance = abs(num1 - num2)

# Mostrar el resultado
print(f"La distancia entre {num1} y {num2} es {distance} unidades.")
```

## Tarea: Adivina el número

### Objetivo

El objetivo de esta tarea es practicar la generación de números aleatorios, la comparación de valores, y el uso de condicionales para proporcionar retroalimentación al usuario.

Además evaluaremos tu capacidad de investigar sobre conceptos y poder usarlos para resolver un problema, en este caso, la forma de encontrar la distancia entre 2 números.

### Instrucciones

1. **Generar un número aleatorio:**
   - Escribe un programa que genere un número aleatorio entre 0 y 20.
   
2. **Solicitar una adivinanza:**
   - Pide al usuario que intente adivinar el número generado por el programa.
   - El usuario tiene un máximo de 3 intentos para adivinar correctamente.

3. **Proporcionar retroalimentación:**
   - Después de cada intento, calcula la distancia entre el número generado y el número proporcionado por el usuario.
   - Muestra un mensaje según la distancia:
     - **`¡Caliente, caliente!`** si la distancia es menor que 3.
     - **`¡Tibio, tibio!`** si la distancia está entre 3 y 6 (inclusive).
     - **`¡Frío, frío!`** si la distancia es mayor a 6.

4. **Finalización:**
   - Si el usuario adivina el número correcto en cualquiera de los intentos, muestra un mensaje de felicitación y termina el programa. Debe contemplar el siguiente texto:
      `¡Felicitaciones! ¡Has adivinado el número!`

   - Si después de 3 intentos el usuario no ha adivinado el número, muestra el número correcto y finaliza el programa.
  
      `Lo siento, no adivinaste el número. El número correcto era`

### Ejemplos de Ejecución

#### El jugador pierde

```plaintext
Adivina el número entre 0 y 20:
Intento 1: 6
¡Frío, frío!

Intento 2: 19
¡Tibio, tibio!

Intento 3: 15
¡Caliente, caliente!

Lo siento, no adivinaste el número. El número correcto era 16.
```

#### El jugador gana

```plaintext
Adivina el número entre 0 y 20:

Intento 1: 17
¡Tibio, tibio!

Intento 2: 13
¡Caliente, caliente!

Intento 3: 14

¡Felicitaciones! Has adivinado el número 14
```

