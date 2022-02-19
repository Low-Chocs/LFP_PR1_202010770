import cargarData
import cargarInstrucciones
import analizar
import reportes

opcion=0
prueba=0
dataList=[]
instructions={}
boolean1=False
boolean2=False

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
        try:
            dataList.clear()
            dataList = cargarData.loadData()
            cargarData.showData(dataList)
        except:
            dataList.clear()
            print("Formato no soportado")
            continue

        if len(dataList)>0:
            boolean1=True

    elif opcion ==2:
        try:
            instructions.clear()
            instructions=cargarInstrucciones.cargarInstrucciones()
            print(instructions)
        except:
            instructions.clear()
            print("Formato no soportado")
            continue
        
        if len(instructions)>0:
            boolean2=True

    elif opcion==3:
        if(boolean1 and boolean2):
            analizar.analizar(dataList, instructions)
        elif(boolean1 and not boolean2):
            print("Te hace falta ingresar el archivo .lfp (Opcion 2)")
        elif(not boolean1 and boolean2):
            print("Te hace falta ingresar el archivo .data (Opcion 1)")
        else:
            print("Ningún archivo ha sido registrado")
    elif opcion==4:
        if(boolean1):
        
            reportes.reportes(dataList)
        else:
            print("Por favor ingresa un archivo en de tipo .data en la (opcion 1)")

            