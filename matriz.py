class nodo:
    def __init__(self, x, y, dato):
        self.x=x
        self.y=y
        self.dato=dato
        self.adelante=None
        self.atras=None
        self.arriba=None
        self.abajo=None
        




import lista
class matriz_dato:
    def __init__(self, m, n, nombre):
        
        self.inicio = nodo( m, n, nombre)

    def crear(self, fila, columna):
        
        i=0
        j=0
        fila=int(fila)
        columna=int(columna)
        aux_x=self.inicio
        aux_y=self.inicio
        while i <= fila:            
            nuevo = nodo(i, 0, 0)
            aux_x.atras=nuevo
            nuevo.adelante=aux_x
            aux_x=nuevo
            #print(str(i))
            i=i+1
            
        #print("-")
        while j <= columna:           
            nuevo = nodo(0, j, 0)
            aux_y.abajo=nuevo
            nuevo.arriba=aux_y
            aux_y=nuevo
            #print(str(j))
            j=j+1

        #### rellena por columnas
        i=1
        j=1
        
        aux_x=self.inicio.atras
        aux_y=self.inicio.abajo
        temp=aux_y         
        while i<= fila:            
            while j<= columna:
                nuevo = nodo(i, j, 0)
                aux_x=self.recorridoY(aux_x)              
                aux_y.atras=nuevo
                nuevo.adelante=aux_y
                
                aux_x.abajo=nuevo
                nuevo.arriba=aux_x
                
                aux_y=nuevo
                aux_x=aux_x.atras
                #print(str(i)+'-'+str(j))
                j=j+1
            #while fin 
            #print('****')
            temp=temp.abajo
            aux_y=temp
            aux_x=self.inicio.atras
            i=i+1
            j=1


       

            

        
    def recorridoY(self, nodo):
        regreso=nodo        
        while regreso.abajo != None:
            regreso=regreso.abajo        
        return regreso

    def recorridoX(self, nodo):
        regreso=nodo
        while regreso.atras != None:
            regreso=regreso.atras
        return regreso

    def recorrer(self):
        temporal=self.inicio.abajo
        aux=temporal.atras

        while temporal.abajo != None:
            while aux != None:
                #print(str(aux.x)+'-'+str(aux.y)+'/'+str(aux.dato))
                
                aux=aux.atras
            temporal=temporal.abajo
            aux=temporal.atras

            

    def reemplazo(self, i, j, dato):       
        temporal=self.inicio.abajo
        aux=temporal.atras

        while temporal.abajo != None:
            
            while aux != None:
                
                if i == str(aux.x) and j == str(aux.y):
                    aux.dato=dato 
                    
                
                    
                aux=aux.atras

            temporal=temporal.abajo
            aux=temporal.atras
            if aux ==None:
                break

    def crearGrafica(self):
        texto='''   graph g{ \n
       layout=dot \n
       label="grid" \n
       labelloc = "t" \n
       node [shape=circle]\n  ''' 

        temporal=self.inicio.abajo
        aux=temporal.atras
        nombre=self.inicio.dato

        while temporal.abajo != None:#primer linea crea variables
            while aux != None:
                texto=texto +'N'+str(aux.x) + str(aux.y) + ';'+ '\n'
                texto=texto +'N'+ str(aux.x) + str(aux.y)+'[label="'+str(aux.dato)+'"];'+ '\n'
                
                aux=aux.atras
            temporal=temporal.abajo
            aux=temporal.atras

        temporal=self.inicio.abajo
        aux=temporal.atras

        #crea el primer bloque
        while temporal.abajo != None:
            while aux != None:
                texto=texto +'N'+ str(aux.x) + str(aux.y)
                if(aux.atras != None):
                    texto=texto+'--'
                else:
                    texto=texto+'\n'
                    
                
                aux=aux.atras
            temporal=temporal.abajo
            aux=temporal.atras

        #crea el segundo bloque
        temporal=self.inicio.abajo
        aux=temporal.atras

        while temporal.atras != None:
            texto=texto+'rank=same {'
            while aux != None:
                texto=texto +'N'+ str(aux.x) + str(aux.y)
                if(aux.abajo != None):
                    texto=texto+'--'
                else:
                    texto=texto+ '} \n'
                
                aux=aux.abajo
            
            temporal=temporal.atras
            aux=temporal.atras
        
        texto=texto+'}'

        #print(texto)
        self.var=lista.matriz_dato("nombre","texto","recorrido")
        self.var.crear(nombre ,texto, "recorrido")
        #self.var.revisar()

    def llamarReporte(self, nombre):
        self.var.buscarGraf(nombre)

    #COSA IMPORTANTE QUE NO SE COMO HACER

    def calculo(self, xi, yi, xf, yf):
        #print(xi)
        #print(yi)
        #print(xf)
        #print(yf)

        temporal=self.inicio.abajo
        aux=temporal.atras
        carrito=self.inicio
        meta=self.inicio

        while temporal.abajo != None:#recorrido de pos inicio y final
            while aux != None:
                #print(str(aux.x)+'-'+str(aux.y)+'/'+str(aux.dato))
                if(str(aux.x)==str(xi) and str(aux.y)==str(yi)):
                    carrito=aux
                if(str(aux.x)==str(xf) and str(aux.y)==str(yf)):
                    meta=aux
                aux=aux.atras
            temporal=temporal.abajo
            aux=temporal.atras




        


    