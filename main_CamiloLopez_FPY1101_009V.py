def main():
    while True:
        print( '=================================' )
        print( 'Menú principal' )
        print( '=================================' )
        print( '1. Registrar libro' )
        print( '2. Prestar libro' )
        print( '3. Listar todos los libros' )
        print( '4. Imprimir reporte de préstamos' )
        print( '5. Salir del programa' )
        print( '---------------------------------' )

        print( 'Seleccione una opción:' )
        option = input()

        if option == '1':
            print( 'Opción 1 seleccionada' )
        elif option == '2':
            print( 'Opción 2 seleccionada' )
        elif option == '3':
            print( 'Opción 3 seleccionada' )
        elif option == '4':
            print( 'Opción 4 seleccionada' )
        elif option == '5':
            print( 'Opción 5 seleccionada' ) 
            break
        else:
            print( 'Opción no válida. Intente nuevamente' )

main()