#Autor: José María Caballero Muñoz   Fecha de creación: 08-03-2022#
#Este es el código de Chema de la función de añadir modificar# 
def añadirModificarJcaballero(nombre, agenda):
    if nombre in agenda:
        print("%s es un contacto que ya existe, su número de teléfono es %s" % (nombre,agenda[nombre]))
        selec = input("Pulsa la tecla 's' si quiere modificarlo. Cualquier otra tecla para continuar.")
        if selec == "s":
            telefono = input("Dime el nuevo número de teléfono: ")
            agenda[nombre]=telefono
    else:
        telefono = input("Dime el número de teléfono: ")
        agenda[nombre]=telefono
