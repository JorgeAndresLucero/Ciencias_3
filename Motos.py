class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def mostrar_cola(self):
        if self.es_vacia() == True:
            print("La cola está vacía\n")
        
        else:
            print(self.items)


c = Cola()

band = 0
opc = 0
lista = []
while opc != 4  :

    print("\n Bienvenido al módulo de asignación de cupos para motos ")
    opc = int(input(" \nSeleccione lo que desea realizar:  \n 1) Ver cola.\n 2) Pedir turno.\n 3) Atender cola\n 4) Salir.   :\n"))
    if opc == 1:
        c.mostrar_cola()
    elif opc == 2:
        nombre = input("Ingrese su nombre: ")
        documento = input("Ingrese su documento: ")
        placa = input("Ingrese la placa de su moto: ")
        lista = [nombre,documento,placa]
        c.encolar(lista)
        
        while nombre.isdigit():
            print("Error, escriba algo valido")
            nombre = input("Ingrese su nombre: ")
        
    elif opc == 3:
        
         c.desencolar()
        


