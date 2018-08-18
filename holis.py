class Pila():
	def __init__(self):
		self.lista_DE_libros = ['Ana','Terror','burros']
		self.lista_DE_libros1 = ['Ana','Comedia','burros']
		self.lista_DE_libros2 = ['Jacinto','Acción','burros']
		self.lista_DE_libros2 = ['Jacinto','Acción','burros']
		self.lista_DE_libros2 = ['Jacinto','Acción','burros']
		self.lista_DE_libros2 = ['Jacinto','Acción','burros']
  
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
pi=Pila()
nombre=""
print("Seleccione como quiere buscar: \n 1)Título.\n2.)Categoría.\n3.)Autor")
opcion = int(input())

if opcion == 1:
	print("Escriba el nombre")
	nombre = input()
	
if nombre == pi.sacar(opcion):
	print(pi.lista_DE_libros)
