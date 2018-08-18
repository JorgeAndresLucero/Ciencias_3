#AUTOR: Luis García
#CARRERA: Ingenieía en Computación
#PROGRAMA: Pila en python 3

#Importando la biblioteca para el manejo de funciones del systema operativo
import os

#Definiendo una clase en Python 3 
class Vuelo():
    #Definiendo el constructor
    def __init__(self):
        self.origen = ""
        self.destino = ""
        self.distancia = ""

    def __str__(self):
        return "\nOrigen->    "+self.origen+"\nDestino->   "+self.destino+"\nDistancia-> "+str(self.distancia)

    def set_value(self, data):
        if len(data)==3:
            self.origen    	= data[0]
            self.destino  	= data[1]
            self.distancia      = data[2]
            
    def get_value(self,pos):
            
            data[0] = origen
            return data[0]
    
class Pila():
	def __init__(self):
		self.lista_DE_Vuelos = []
		
	def mostrar(self):
		print(self.lista_DE_Vuelos)
		
  #Definiendo una función de la clase pila con'def'
	def tamanio(self):
		if len(self.lista_DE_Vuelos) > 0:
			return len(self.lista_DE_Vuelos)
		else:
			print("\nNO hay elementos en la pila")

	def desapilar(self):
		if len(self.lista_DE_Vuelos) > 0:
			print("\nVUELO EN EL TOPE DE LA PILA A ELIMINAR:\n", self.lista_DE_Vuelos[-1])
			self.lista_DE_Vuelos.remove(self.lista_DE_Vuelos[-1])
			print("\nVuelo eliminado...")
		else:
			print("\nNO hay elementos en la pila...")

	def tope(self):
		if len(self.lista_DE_Vuelos) > 0:
			print("\nEl tope de la pila es:\n", self.lista_DE_Vuelos[-1])
		else:
			print("\nNO hay elementos en la pila...")

	def vaciar(self):
		if len(self.lista_DE_Vuelos) > 0:
			self.__init__()
			print("\nVuelos eliminados")
		else:
			print("\nNO hay elementos en la pila...")
	def vacial(self):
		if len(self.lista_DE_Vuelos) > 0:
		for i in range (3)	
			print("\npila :",self.lista_DE_Vuelos)
		break
		else:
			print("\nNO hay elementos en la pila...")

	          
opc = 0
buscado = ""
#Creando un objeto de la clase pila
adm_Obj_pila = Pila()
ob = Vuelo()
while opc != 9:
    os.system("cls")
    print("PROGRAMA PILA, Ejemplo: \n")
    print("ADMINISTRADOR DE VUELOS\n")
    #Capturando la opción del usuario en la variable 'opc'
    opc = input("1.- Tamaño de la pila \n2.- Apilar \n3.- Desapilar \n4.- Tope \n5.- Mostrar \n 9.- Salir \nElige una opcion -> ")
    #convirtiendo a entero la variable 'opc' para poder evaluar la elección del menú
    opc = int(opc)
    if opc == 1:
      #Mandando llamar la función tamanio de la clase pila que esté dentro del objeto instanciado anteriormente
    	adm_Obj_pila.tamanio()
    elif opc == 2:
        print()
        #Definiendo una variable booleana
        bandera = True
        while bandera == True:
            origen    = input("Ingrese el origen:    ")
            if origen.isdigit():
                input("Error, no ingrese unicamente numeros, ingrese caracteres validos...")
            else:
                break
        while bandera == True:
            destino   = input("Ingrese el destino:   ")
            if destino.isdigit():
                input("Error, no ingrese unicamente numeros, ingrese caracteres validos...")
            else:
                break
        while bandera == True:
            distancia = input("Ingrese la distancia: ")
            if not distancia.isdigit():
                input("Error, ingrese unicamente digitos...")
            else:
                distancia = int(distancia)
                objVuelos = Vuelo()
                objVuelos.set_value([origen, destino, distancia])
                #Agregando los valores capturados a la pila con el comando o función de las listas 'append()'
                adm_Obj_pila.lista_DE_Vuelos.append(objVuelos)
                break
    elif opc == 3:
        adm_Obj_pila.desapilar()
    elif opc == 4:
        adm_Obj_pila.mostrar()
    elif opc== 5:
        # buscado  = input("Ingrese el origen : ")
       # if buscado.isdigit():
               # input("Error, no ingrese unicamente numeros, ingrese caracteres validos...")
        #else:
            i=0
            print(adm_Obj_pila.vacial())
            #for i in range(adm_Obj_pila.tamanio()):
                    #if buscado == adm_Obj_pila.lista_DE_Vuelos.pop(ob.get_value):
                        #print(adm_Obj_pila.lista_DE_Vuelos[i])
                        #break
                    
                    
    print("\n")

    
    
   
        
                        
               
    
    #Llamando la función del sistema operativo 'pause' 
    os.system("pause")
input("\nSaliendo, presione una tecla para continuar...")
