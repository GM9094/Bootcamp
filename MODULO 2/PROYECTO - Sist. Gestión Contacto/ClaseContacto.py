class clase_contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion

    def get_nombre(self):
        return self._nombre

    def get_telefono(self):
        return self._telefono

    def get_correo(self):
        return self._correo

    def get_direccion(self):
        return self._direccion

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    def set_correo(self, nuevo_correo):
        self._correo = nuevo_correo

    def set_direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    def __str__(self):
        return (
            f"Nombre: {self._nombre}, "
            f"Teléfono: {self._telefono}, "
            f"Correo: {self._correo}, "
            f"Dirección: {self._direccion}"
        )
