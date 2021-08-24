class nodo:
    def __init__(self, x, y, dato):
        self.x=x
        self.y=y
        self.dato=dato
        self.adelante=None
        self.atras=None
        self.arriba=None
        self.abajo=None


class matriz_dato:
    def __init__(self, m, n, nombre):
        
        self.inicio = nodo( m, n, nombre)

    def crear(self, fila, columna):
        
        i=0
        j=0
        aux_x=self.inicio
        aux_y=self.inicio
        while i <= fila+1:            
            nuevo = nodo(i, 0, 0)
            aux_x.adelante=nuevo
            nuevo.atras=aux_x
            aux_x=nuevo
            i=i+1

        while j <= columna+1:           
            nuevo = nodo(0, j, 0)
            aux_y.abajo=nuevo
            nuevo.arriba=aux_y
            aux_y=nuevo
            j=j+1

        #### rellena
        i=1
        j=1
        
        aux_x=self.inicio.atras
        aux_y=self.inicio.abajo
        temp=aux_y         
        while i<= fila:            
            while j<= columna+1:
                nuevo = nodo(i, j, 0)
                aux_x=self.recorridoY(aux_x)              
                aux_y.atras=nuevo
                nuevo.adelante=aux_y
                
                aux_x.abajo=nuevo
                nuevo.arriba=aux_x
                
                aux_y=nuevo
                aux_x=aux_x.atras
                
                j=j+1
            #while fin j
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
            while aux.atras != None:
                print(aux.x)
                print(aux.y)
                print(aux.dato)
                print(aux.binario)

                aux=aux.atras
            temporal=temporal.abajo
            aux=temporal.atras

    def reemplazo(self, i, j, dato):       
        temporal=self.inicio.abajo
        aux=temporal.atras

        while temporal.abajo != None:
            
            while aux.atras != None:
                
                if i == str(aux.x) and j == str(aux.y):
                    aux.dato=dato 
                    
                
                    
                aux=aux.atras

            temporal=temporal.abajo
            aux=temporal.atras
            if aux ==None:
                break
    