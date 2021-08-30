import os.path
import carga
#import practica

class Index:
    
    
    def __init__ (self, opcion):
        self.opcion=opcion

def main():

        #var=carga.Carga_archivo()
        var=carga.Carga_archivo()
        menu='''Menu Principal:
        1.- Cargar Archivos
        2.- Procesar Terreno
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
                    
                    var.xmlCarga(rt)                   
                else:
                    print("Archivo incorrecto")

            elif op == '2':              
                rt=input("Ingrese nombre del terreno: ")
                var.xmlGenerarTerreno(rt)
                
                          
            elif op == '3':
                rt=input("Ingrese la ruta del archivo de salida: ")
                ext=os.path.splitext(rt)

                if ext[1]==".xml":
                    var.salida(rt)                  
                else:
                    print("Ruta de Archivo Incorrecto")

            elif op == '4':
                texto='''
                Maria Luisa Fernanda Calderon Molina
                201602458
                Introduccion a la Programacion y Computacion 2
                Seccion "A"
                4to Semestre'''
                print(texto)

            elif op == '5':
                rt=input("Ingrese nombre del terreno: ")
                var.generarGrafica(rt)


                
            elif op == '6':
                break
            else:
                print("Opcion Invalida")
                #break

    


if __name__ == "__main__":
    main()
