libros = []

def registrar_libro():
    print( 'Ingrese el título del libro:' )
    titulo_libro = input()
    print( 'Ingrese el nombre del autor del libro:' )
    autor_libro = input()
    print( 'Ingrese el año de publicación del libro:' )
    fecha_publicacion = input()
    print( 'Ingrese el SKU del libro:' )
    sku_libro = input()

    if not titulo_libro or not autor_libro or not fecha_publicacion or not sku_libro:
        print( 'Todos los datos deben ser ingresados correctamente.' )
        return
    
    libro = {
        "titulo": titulo_libro,
        "autor": autor_libro,
        "date": fecha_publicacion,
        "sku": sku_libro
    }

    libros.append( libro )

    print( 'Libro registrado correctamente' )



def prestar_libro():
    print( 'Opción 2: Prestar libro' )

def listar_libros():
    print( 'Todos los libros' )
    print( '-----------------' )
    print( libros )

def imprimir_reporte_prestamos():
    print( 'Opción 4: Imprimir reporte de préstamos' )

def salir():
    print( 'Programa finalizado…' )
    print( 'Desarrollado por Camilo López' )
    print( 'RUN: 18.054.436-4' )


  