from ClaseContacto import clase_contacto


class clase_gestor:

    def __init__(self):
        self._contactos = []
        self._telefonos = {}

    def agregar_contacto(self, contacto: clase_contacto):
        telefono = contacto.get_telefono().strip()

        if telefono in self._telefonos:
            return f"El teléfono {telefono} ya está registrado"

        self._contactos.append(contacto)
        self._telefonos[telefono] = contacto
        return True

    def buscar_telefono(self, telefono):
        return self._telefonos.get(telefono.strip())

    def buscar_nombre(self, nombre):
        nombre = nombre.strip()
        return [c for c in self._contactos if c.get_nombre() == nombre]

    def eliminar_telefono(self, telefono):
        telefono = telefono.strip()
        contacto = self._telefonos.get(telefono)

        if contacto is None:
            return False

        self._contactos.remove(contacto)
        del self._telefonos[telefono]
        return True

    def editar_contacto(
        self,
        telefono,
        nombre_nuevo=None,
        telefono_nuevo=None,
        correo_nuevo=None,
        direccion_nueva=None
    ):
        telefono = telefono.strip()
        contacto = self._telefonos.get(telefono)

        if contacto is None:
            return False

        if telefono_nuevo:
            telefono_nuevo = telefono_nuevo.strip()
            if telefono_nuevo != telefono and telefono_nuevo in self._telefonos:
                return False

            del self._telefonos[telefono]
            contacto.set_telefono(telefono_nuevo)
            self._telefonos[telefono_nuevo] = contacto

        if nombre_nuevo:
            contacto.set_nombre(nombre_nuevo)
        if correo_nuevo:
            contacto.set_correo(correo_nuevo)
        if direccion_nueva:
            contacto.set_direccion(direccion_nueva)

        return True

    def copiar_lista(self):
        return list(self._contactos)
