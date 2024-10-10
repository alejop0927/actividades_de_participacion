from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return "El libro con titulo {} y isbn {} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {}, existencias: {}".format(self.titulo, self.isbn, self.cantidad_a_comprar, self.existencias)
