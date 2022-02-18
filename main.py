import cargarData
import cargarInstrucciones
import analizar
import reportes

opcion=0
prueba=0
dataList=[]
instructions={}

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
            prueba+=1

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
            prueba+=1

    elif opcion==3:
        analizar.analizar(dataList, instructions)
    elif opcion==4:
        reportes.reportes()