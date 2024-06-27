from funciones_CamiloLopez_FPY1101_009V import registrar_libro, prestar_libro, listar_libros, imprimir_reporte_prestamos, salir

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
            registrar_libro()
        elif option == '2':
            prestar_libro()
        elif option == '3':
            listar_libros()
        elif option == '4':
           imprimir_reporte_prestamos()
        elif option == '5':
            salir() 
            break
        else:
            print( 'Opción no válida. Intente nuevamente' )

main()