from carro_compra import CarroCompras
from item_compra import ItemCompra
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError
from libro import Libro
class TiendaLibros:
   def __init__(self):
      self.catalogo=dict(ItemCompra(self.isbn,self.precio))
      self.carrito=CarroCompras
   def __str__(self):
      ItemCompra(self.isbn) and ItemCompra(self.titulo) in self.carrito
      print(f"el isbn {ItemCompra(self.isbn)} y el titulo {ItemCompra(self.titulo)} ya esta en el carro compra")
      
   def adicionar_libro_a_catálogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError("El libro con ISBN {} ya existe en el catálogo".format(isbn))
        else:
            libro = Libro(isbn, titulo, precio, existencias)
            self.catalogo[isbn] = libro
            return libro
   def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        elif libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)
        else:
            self.carrito[libro.isbn] = cantidad
            libro.existencias -= cantidad

   def retirar_item_de_carrito(self, isbn):
        del self.carrito[isbn]