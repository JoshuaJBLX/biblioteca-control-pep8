class Biblioteca:
 def __init__(self,name):
  self.name = name 
  self.libro=[]

 def addb(self,book):
  self.libro.append(book)

 def show(self):
  for libro in self.libro:
   print(libro.titulo,libro.autor,libro.indice)

class Book:
 def __init__(self,titulo,autor,indice):
  self.titulo=titulo
  self.autor=autor
  self.indice=indice
  self.existe=True

 def lend(self):
  if self.existe==True:
   self.existe=False
   return True
  else:
   return False

 def back(self):
  self.existe=True