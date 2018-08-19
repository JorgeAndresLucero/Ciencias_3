class Pila():
	def __init__(self,lista):
		self.lista_DE_libros = lista
		
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
	def sacar(self,valor):
		if valor == 1:
			return self.lista_DE_libros[0]
		elif valor == 2:
			return self.lista_DE_libros[1]
		elif valor == 3:
			return self.lista_DE_libros[2]	
opcion=0
 #aca se meten los libros en cada lista independiente
l1 = ['El Cartero de los Sueños','cuentos infantiles','Laura Gallego']
l2 = ['Un fantasma en apuros','cuentos infantiles','Laura Gallego']
l3 = ['Max ya no hace reír','cuentos infantiles','Laura Gallego']
l4 = ['¿Donde está Alba?','cuentos infantiles','Laura Gallego']
l5 = ['Alba tiene una amiga muy especial','cuentos infantiles','Laura Gallego']
l6 = ['Por una rosa','relatos','Laura Gallego']
l7 = ['Mañana todavia','relatos','Laura Gallego']
l8 = ['El viaje del polizón','relatos','Laura Gallego']
l9 = ['Relatos insólitos','relatos','Laura Gallego']
l10 = ['Relatos de hoy II','relatos','Laura Gallego']
l11 = ['Atlántico. 30 historias de los dos mundos','relatos','Laura Gallego']
l12 = ['Historias para girar;relatos','relatos','Laura Gallego']
l13 = ['Topito Terremoto','cuentos ilustrados','Anna Llenas']
l14 = ['El Monstruo de Colores','cuentos ilustrados','Anna Llenas']
l15 = ['El buit','cuentos ilustrados','Anna Llenas']
l16 = ['Diario de las emociones','cuentos ilustrados','Anna Llenas']
l17 =  ['Te quiero (casi siempre) ','cuentos ilustrados','Anna Llenas']
l18 =  ['Si yo fuera un gato','cuentos ilustrados','Paloma Sánchez']
l19 = ['Mis opuestos','cuentos ilustrados','Olga Cuellar']
l20 = ['Mi Mascota','cuentos','Yolanda Reyes']
l21 = ['Tumaco','cuentos','Oscar Pantoja']
l22 = ['Cuando el mundo era así','cuentos','Triunfo Arciniegas']
l23 = ['Mi primer libro de poesía colombiana','cuentos','Beatriz Helena Robledo']

#se guardan los libros en esta lista 
librillos =[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23]

nombre=""
print("Seleccione como quiere buscar: \n1 )Título.\n2.)Categoría.\n3.)Autor.\n")
opcion = int(input())
print("Escriba el título,categoría o autor :")
nombre = input()

if opcion == 1:
	for i in range(23):
		# se mandan por parametro uno por uno a la clase pila
		pi=Pila(librillos[i])
		if nombre == pi.sacar(opcion):#se invoca la funcion sacar para sacar el libro que se necesita
			print(pi.lista_DE_libros)
elif opcion == 2:
	for i in range(23):
		pi=Pila(librillos[i])
		if nombre == pi.sacar(opcion):
			print(pi.lista_DE_libros)			
elif opcion == 3:
	for i in range(23):
		pi=Pila(librillos[i])
		if nombre == pi.sacar(opcion):
			print(pi.lista_DE_libros)	