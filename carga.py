import xml.etree.ElementTree as ET
from xml.dom import minidom
import matriz

class Carga_archivo:
    cadena=""

    def xmlCarga(self, link):

        try:
            tree=ET.parse(link)
            self.root=tree.getroot()
            self.txt = minidom.parse(link)#aqui se pone el self.link
            print('terreno cargado con exito')

        except:
            print("Error al subir el archivo")
        
        
    def xmlGenerarTerreno(self, nombre):  

        try:
  
            bandera=0
            etqTerreno = self.txt.getElementsByTagName('terreno')#lista con todas las etiquetas "terrenos" 
            etqFila = self.txt.getElementsByTagName('n')
            etqColumna = self.txt.getElementsByTagName('m')#ver cual es fila y cual es columna
            etqPIX = self.txt.getElementsByTagName('x')
            etqPIY = self.txt.getElementsByTagName('y')
            etqPFX =self.txt.getElementsByTagName('x')
            etqPFY = self.txt.getElementsByTagName('posicionfin')

        
            

            for i in etqTerreno:
                #print(i)
                self.terrenoNombre = etqTerreno[bandera].attributes['nombre'].value
                if(nombre==self.terrenoNombre):
                    print("entro")
                    fila = etqFila[bandera].firstChild.data
                    columna = etqColumna[bandera].firstChild.data

                    self.xI = etqPIX[bandera].firstChild.data
                    self.yI = etqPIY[bandera].firstChild.data
                    
                    self.xF = etqPIX[bandera+1].firstChild.data
                    self.yF = etqPIY[bandera+1].firstChild.data
                    
                    self.crearTerreno(fila, columna, nombre)
                    self.indice=bandera
                    break
                    #self.crearTerreno(fila, columna, nombre, bandera)

                
                #print(self.indice].attributes['nombre'].value)#obtiene el atributo de la etiqueta terreno con id nombre
                bandera=bandera+1

            #pos iniciom y fin
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
            #self.var.recorrer()
            self.var.crearGrafica()
            self.var.calculo(self.xI,self.yI,self.xF,self.yF)

        
        except:
            print("Error 404")

    def crearTerreno(self, m, n, nombre):
        print('Procesando terreno...')
        print('Calculando camino...')
        self.texto()
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
        try:
            self.var.llamarReporte(nombre)
       
        except:
            print("Error al generar grafica")

    def salida(self, ruta):
        file=open(ruta,"w")
        file.write(self.cadena)
        file.close()

    def texto(self):
       
        self.cadena='<terreno nombre="'+self.terrenoNombre+'_Salida">\n'
        self.cadena=self.cadena+'<posicioninicio>\n<x>'+self.xI+' </x> \n <y> '+self.yI+' </y> \n <posicioninicio>'
        self.cadena=self.cadena+'<posicionfin>\n<x>'+self.xF+' </x> \n <y> '+self.yF+' </y> \n <posicionfin>'
        self.cadena=self.cadena+'<combustible></combustible>'
        #print(m_n)
        
        self.cadena=self.cadena+'</terreno>'
       