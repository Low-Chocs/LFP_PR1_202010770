def reportes(dataList):
    for i in range(2, len(dataList)):
        print(dataList[i].getSales())
    ordenamientoBurbuja(dataList)

    text='''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Reportes</title>
  </head>
  <body>
    <h1>Tabla con los productos ordernados de mayor a menor</h1>
    
        <table class="table">
  <thead>
    <tr>
      <th scope="col">Producto</th>
      <th scope="col">Precio</th>
      <th scope="col">Cantidad</th>
       <th scope="col">Ventas</th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody>
  {'''
    for object in range(2,len(dataList)):'''}
        
    <tr>
      <th scope="row">1</th>
      <td>{'''+dataList[object].getProduct()+'''}></td>
      <td>dataList[object].getPrice()</td>
      <td>dataList[object].getQuantity()+</td>
      <td>str(dataList[object].getSales())</td>
    </tr>
  </tbody>
</table>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>
'''
    file = open("report.html", "w") 
    file.write(text)

def ordenamientoBurbuja(dataList):
    dataLen=len(dataList)
    dataList2=[]
    for lista in range(2,dataLen):
        for lista2 in range(2,dataLen-3):
            if(float(dataList[lista2].getSales())<float(dataList[lista2+1].getSales())):
                dataList2.append(dataList[lista2])
                dataList[lista2]=dataList[lista2+1]
                dataList[lista2+1]=dataList2[0]
                dataList2.clear()
    print()
    print("Lista ordenada")
    for i in range(2, len(dataList)):
        print(dataList[i].getSales())
