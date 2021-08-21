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

    def __init__(self, fila, columna):
        
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

    