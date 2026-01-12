"""
Este módulo contiene la lógica principal de la biblioteca.
"""

from biblioteca import biblioteca,book

objbiblioteca=biblioteca("central")

book1=book("Python","Guido",1)
book2=book("Java","Gosling",2)

objbiblioteca.addb(book1)
objbiblioteca.addb(book2)

objbiblioteca.show()

print(book1.prest())
print(book1.prest())
book1.ret()
print(book1.prest())
