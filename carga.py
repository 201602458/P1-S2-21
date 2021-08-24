from xml.dom import minidom
class Carga_archivo:

    link = ""
    txt=""
    indice=0

    def xmlCarga(self, link):
        print(link)
        self.link=link
        self.txt = minidom.parse('prueba.xml')#aqui se pone el self.link

        
    def xmlGenerarTerreno(self, nombre):  
        #print(nombre)       
        bandera=0
        item = self.txt.getElementsByTagName('terreno')#lista con todas las etiquetas "terrenos" 

        for i in item:
            #print(i)
            terrenoNombre = item[bandera].attributes['nombre'].value
            if(nombre==terrenoNombre):
                print("entro")
            
            
            #print(self.indice].attributes['nombre'].value)#obtiene el atributo de la etiqueta terreno con id nombre
            bandera=bandera+1

    def crearTerreno(self, m, n, nombre, indice):
        print("XD")

