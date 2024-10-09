from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
 def __init__(self, mensaje):
    try:
      raise LibroExistenteError("El libro ya existe en la lista")
    except LibroError as e:
        print(f"Error: {e}")
    super().__init__(mensaje)
  
