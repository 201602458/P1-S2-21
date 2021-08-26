import xml.etree.ElementTree as ET
from xml.dom import minidom
import matriz

class Carga_archivo:

    def xmlCarga(self, link):
        tree=ET.parse('prueba.xml')
        self.root=tree.getroot()
        self.txt = minidom.parse('prueba.xml')#aqui se pone el self.link

        
    def xmlGenerarTerreno(self, nombre):  
        bandera=0
        etqTerreno = self.txt.getElementsByTagName('terreno')#lista con todas las etiquetas "terrenos" 
        etqFila = self.txt.getElementsByTagName('n')
        etqColumna = self.txt.getElementsByTagName('m')#ver cual es fila y cual es columna

        for i in etqTerreno:
            #print(i)
            terrenoNombre = etqTerreno[bandera].attributes['nombre'].value
            if(nombre==terrenoNombre):
                print("entro")
                fila = etqFila[bandera].firstChild.data
                columna = etqColumna[bandera].firstChild.data
                
                self.crearTerreno(fila, columna, nombre)
                self.indice=bandera
                break
                #self.crearTerreno(fila, columna, nombre, bandera)

            
            #print(self.indice].attributes['nombre'].value)#obtiene el atributo de la etiqueta terreno con id nombre
            bandera=bandera+1

        #para rellenar el terreno
        for elem in self.root:
            for subelem in elem:
                if (elem.get('nombre')==nombre):
                    x=subelem.get('x')
                    y=subelem.get('y')
                    dato=subelem.text
                    self.rellenarTerreno(x,y,dato)

                #print()
                #print(subelem.attrib)
                #print(subelem.get('x')) XD
                #print(subelem.text)
                
        #print(self.root[0][4].attrib)
        self.var.recorrer()
        self.var.crearGrafica()

    def crearTerreno(self, m, n, nombre):
        print('Procesando terreno...')
        print('Calculando camino...')
        #print(n)
        #print(nombre)
        #print(indice)
        
        self.var=matriz.matriz_dato(m,n,nombre)
        self.var.crear(m,n)
        #self.var.recorrer()

    def rellenarTerreno(self, x, y, dato):
        self.var.reemplazo(x,y,dato)
        #self.var.recorrer()

    def generarGrafica(self, nombre):
        self.var.llamarReporte(nombre)