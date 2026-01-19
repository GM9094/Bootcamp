from ClaseContacto import clase_contacto
from ClaseGestor import clase_gestor


def interface_menu():
    print("\n------ SISTEMA DE GESTIÓN DE CONTACTOS ------")
    print("(1) Buscar contacto por Teléfono")
    print("(2) Buscar contacto por Nombre")
    print("(3) Agregar nuevo contacto")
    print("(4) Modificar contacto")
    print("(5) Eliminar contacto por Teléfono")
    print("(6) Imprimir lista de contactos")
    print("(0) Salir")


def ingresar_valor(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacío.")


def main():
    gestor = clase_gestor()

    while True:
        interface_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            telefono = ingresar_valor("Teléfono a buscar: ")
            contacto = gestor.buscar_telefono(telefono)
            print(contacto if contacto else "Contacto no encontrado.")

        elif opcion == "2":
            nombre = ingresar_valor("Nombre a buscar: ")
            resultados = gestor.buscar_nombre(nombre)
            if resultados:
                for c in resultados:
                    print(c)
            else:
                print("No se encontraron contactos.")

        elif opcion == "3":
            nombre = ingresar_valor("Nombre: ")
            telefono = ingresar_valor("Teléfono: ")
            correo = ingresar_valor("Correo: ")
            direccion = ingresar_valor("Dirección: ")

            contacto = clase_contacto(nombre, telefono, correo, direccion)
            resultado = gestor.agregar_contacto(contacto)

            if resultado is True:
                print("Contacto agregado correctamente.")
            else:
                print(resultado)

        elif opcion == "4":
            telefono = ingresar_valor("Teléfono del contacto a editar: ")

            print("Deja el campo vacío si no deseas modificarlo.")
            nombre_nuevo = input("Nuevo nombre: ").strip() or None
            telefono_nuevo = input("Nuevo teléfono: ").strip() or None
            correo_nuevo = input("Nuevo correo: ").strip() or None
            direccion_nueva = input("Nueva dirección: ").strip() or None

            exito = gestor.editar_contacto(
                telefono,
                nombre_nuevo,
                telefono_nuevo,
                correo_nuevo,
                direccion_nueva
            )

            print("Contacto actualizado." if exito else "No se pudo actualizar.")

        elif opcion == "5":
            telefono = ingresar_valor("Teléfono a eliminar: ")
            print(
                "Contacto eliminado."
                if gestor.eliminar_telefono(telefono)
                else "Contacto no encontrado."
            )

        elif opcion == "6":
            contactos = gestor.copiar_lista()
            if contactos:
                for c in contactos:
                    print(c)
            else:
                print("No hay contactos registrados.")

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
