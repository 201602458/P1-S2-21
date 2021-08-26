class nodo_lista:

    def __init__(self, nombre, textoGraf, textoRec):
        self.nombre=nombre
        self.textoGraf=textoGraf
        self.textoRec=textoRec       
        self.siguiente=None
import os
class matriz_dato:

    def __init__(self, nombre, textoG, textoR):   
        self.inicio = nodo_lista(nombre, textoG, textoR)
        self.fin = nodo_lista(nombre, textoG, textoR)

    def crear(self, nombre, textoG, textoR):
        
        nuevo=nodo_lista(nombre, textoG, textoR)
        if self.inicio.siguiente == None:
            #verificar si esta vacia        
            #print("vacia")
            self.inicio.siguiente=nuevo
            nuevo.siguiente=self.inicio
            self.fin=nuevo
        else:
            #no vacia
            #print("no vacia")
            aux=self.fin
            aux.siguiente=nuevo
            nuevo.siguiente=self.inicio
            self.fin=nuevo



    def verificar(self, nodo):
        regreso=nodo        
        while regreso.siguiente != None:
            regreso=regreso.siguiente        
        return regreso

    def revisar(self):
        aux=self.inicio.siguiente
        while aux != self.inicio:
            #print(aux.nombre)
            aux=aux.siguiente

    def buscarGraf(self, nombre):

        aux=self.inicio.siguiente
        print(aux.nombre)
        print(nombre)

        while aux != self.inicio:

            if aux.nombre==nombre:
                #crear el texto y mostrar la imagen
                print("Se a generado la grafica")
                file = open("graficaDoble.dot", "w")
                file.write(aux.textoGraf)
                file.close()
            
            #import os
            os.system("dot graficaDoble.dot -Tpng -o grafsnake.png")
            #os.system("eog, grafsnake.png")
            aux=aux.siguiente
            
        
    def buscarN(self, nombre):

        aux=self.inicio.siguiente

        while aux != self.inicio:

            if aux.nombre==nombre:
                #crear el texto y mostrar la imagen
                print("Matriz existente")
            else:
                self.buscarGraf(nombre)
            
            
            aux=aux.siguiente
    

        