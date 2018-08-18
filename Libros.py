#Importando la biblioteca para el manejo de funciones del systema operativo
import os

#Definiendo una clase en Python 3 
class Libro():
    #Definiendo el constructor
    def __init__(self):
        self.titulo = ""
        self.categoria = ""
        self.autor = ""

    def __str__(self):
        return "\nTitulo->    "+self.titulo+"\nCategoria->   "+self.categoria+"\nAutor-> "+str(self.autor)

    def set_value(self, data):
        if len(data)==3:
            self.titulo    	=data[0]
            self.categoria  	=data[1]
            self.autor          =data[2]
    def get_value(self,data):

        return self.titulo
 

class Pila():
	def __init__(self):
		self.lista_DE_libros = []
  
  #Definiendo una función de la clase pila con'def'
	def tamanio(self):
		if len(self.lista_DE_libros) > 0:
			print("El tamaño de la pila es: ",len(self.lista_DE_libros))
		else:
			print("\nNO hay elementos en la pila")

	def desapilar(self):
		if len(self.lista_DE_libros) > 0:
			print("\nVUELO EN EL TOPE DE LA PILA A ELIMINAR:\n", self.lista_DE_libros[-1])
			self.lista_DE_libros.remove(self.lista_DE_libros[-1])
			print("\nVuelo eliminado...")
		else:
			print("\nNO hay elementos en la pila...")

	def tope(self):
		if len(self.lista_DE_libros) > 0:
			print("\nEl tope de la pila es:\n", self.lista_DE_libros[-1])
		else:
			print("\nNO hay elementos en la pila...")

	def vaciar(self):
		if len(self.lista_DE_libros) > 0:
			self.__init__()
			print("\nLibros eliminados")
		else:
			print("\nNO hay elementos en la pila...")
	

opc = 0
#Creando un objeto de la clase pila
adm_Obj_pila = Pila()
obj_libro = Libro()
while opc != 6:
    os.system("cls")
    print("PROGRAMA PILA, Ejemplo: \n")
    print("ADMINISTRADOR DE LIBROS\n")
    #Capturando la opción del usuario en la variable 'opc'
    opc = input("1.- Tamaño de la pila \n2.- Llenar pila \n3.- Desapilar \n4.- Tope \n5.- Vaciar  \n6.- Salir \nElige una opcion -> ")
    #convirtiendo a entero la variable 'opc' para poder evaluar la elección del menú
    opc = int(opc)
    if opc == 1:
      #Mandando llamar la función tamanio de la clase pila que esté dentro del objeto instanciado anteriormente
    	adm_Obj_pila.tamanio()
    elif opc == 2:
        for i in range(23):
           # titulo    = """ aqui va el manejo de atchivos libron.origen"""
            
        
            #categoria   = """ aqui va el manejo de atchivos libron.origen"""
          
        
            #autor = """ aqui va el manejo de atchivos libron.origen"""
           
                
                objlibros = Libro()
                objlibros.set_value([titulo, categoria, autor])
                #Agregando los valores capturados a la pila con el comando o función de las listas 'append()'
                adm_Obj_pila.lista_DE_Libros.append(objLibros)

                
    elif opc == 3:
        adm_Obj_pila.desapilar()
    elif opc == 4:
        adm_Obj_pila.tope()
    elif opc== 5:
        adm_Obj_pila.vaciar()
    elif opc == 6:
        band= False
        print "Busqueda por Titulo"
        valor = input("Ingrese un titulo ")
        while adm_Obj_pila.lista_DE_libros and not band:
            if obj_libro.get_value() == valor:
                band = True

                if band:
                    print "Estos libros se encuentran en la pila:"
                    print (adm_Obj_pila.lista_DE_libros)
            
        
   
        
    print("\n")
    #Llamando la función del sistema operativo 'pause' 
    os.system("pause")
input("\nSaliendo, presione una tecla para continuar...")
