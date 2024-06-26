# Detalles de la evaluación

Una biblioteca necesita desarrollar una aplicación que permita gestionar el préstamo de libros y calcular el total de libros prestados por cada usuario. La aplicación debe cumplir con las siguientes funcionalidades:
1. Registrar libro
2. Prestar libro
3. Listar todos los libros
4. Imprimir reporte de préstamos
5. Salir del Programa

Cada una de estas opciones de la aplicación debe estar desarrollada en una función que debe ser llamada desde el programa principal.

## Registrar libro
Para registrar un libro se requiere los siguientes datos: Título, Autor, Año de Publicación, SKU. Debe validar que
todos los datos sean ingresados.
Nota: El SKU es el identificador único de cada libro, facilitando su búsqueda y adquisición en librerías y bibliotecas.
Ejemplo de SKU es las 6 primeras letras del título del libro – las 3 primeras letras del autor – año de publicación.

## Prestar libro
Para prestar un libro se requiere: Nombre del usuario y SKU del libro. Debe validar que el libro exista y que no esté ya prestado.

## Listar todos los libros
Debe mostrar en la pantalla la lista de todos los libros registrados.

## Imprimir reporte de préstamos
Debe generar un archivo de texto (.txt) con el detalle de los préstamos realizados, incluyendo el nombre del usuario, título del libro y fecha del préstamo.

## Salir del programa
La aplicación deberá finalizar para salir el programa mostrando un mensaje con sus datos