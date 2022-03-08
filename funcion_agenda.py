agenda = {}
#Función añadir o modificar#
def añadirModificarJcaballero():
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        print("%s es un contacto que ya existe, su número de teléfono es %s" % (nombre,agenda[nombre]))
        selec = input("Pulsa la tecla 's' si quiere modificarlo. Cualquier otra tecla para continuar.")
        if selec == "s":
            telefono = input("Dime el nuevo número de teléfono: ")
            agenda[nombre]=telefono
    else:
        telefono = input("Dime el número de teléfono: ")
        agenda[nombre]=telefono