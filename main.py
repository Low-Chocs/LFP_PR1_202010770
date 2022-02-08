opcion=0

def cargarData():
    print("Opcion 1")
def cargarInstrucciones():
    print("Opcion 2")

def analizar():
    print("Opcion 3")
def reportes():
    print("Opcion 4")


while(opcion!=5):
    print("El gran menú \n 1. Cargar Data \n 2. Cargar instrucciones\n"+
    " 3. Analizar \n 4. Reportes \n 5. Salir\n")

    try:
        opcion= int(input("Seleccione un valor \n"))
    except:
        print("Formato no permitido")
        continue
    

    if opcion < 1 or opcion > 5:
        print("Ingrese un valor entre 1 y 5")
    elif opcion ==1:
        cargarData()
    elif opcion ==2:
        cargarInstrucciones()
    elif opcion==3:
        analizar()
    elif opcion==4:
        reportes()