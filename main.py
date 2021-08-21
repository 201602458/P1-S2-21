import os.path

class Index:
    opcion="1"

    def __init__ (self, opcion):
        self.opcion=opcion

    
       

def main():

        menu='''Menu Principal:
        1.- Cargar Archivos
        2.- Procesar Archivo
        3.- Escribir Archivo Salida
        4.- Mostrar Datos Del Estudiante
        5.- Mostrar Grafica
        6.- Salir'''

        while True:
            print(menu)
            op=input("Ingrese una opcion: ")
            if op == '1':               
                rt=input("Ingrese la ruta del archivo: ")
                ext=os.path.splitext(rt)
                
                if ext[1]==".xml":
                    var=carga.Carga_archivo(rt)
                    var.cargar()                   
                else:
                    print("Archivo incorrecto")

            elif op == '2':              
                print("op2")
                          
            elif op == '3':
                rt=input("Ingrese la ruta del archivo de salida: ")
                ext=os.path.splitext(rt)

                if ext[1]==".xml":
                    var2.salida(rt)                  
                else:
                    print("Ruta de Archivo Incorrecto")

            elif op == '4':
                texto='''
                Maria Luisa Fernanda calderon Molina
                201602458
                Introduccion a la Programacion y Computacion 2
                Seccion "A"
                4to Semestre'''
                print(texto)

            elif op == '5':
               print("op5")


                
            elif op == '6':
                break
            else:
                print("Opcion Invalida")
                #break

    


if __name__ == "__main__":
    main()
