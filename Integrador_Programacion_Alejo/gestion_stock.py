productos_disponible = {"enlataditos": [], "frutita": [], "congeladito": [], "pancito": []}
cantidad_disponible = {"enlataditos": [], "frutitas": [], "congeladito": [], "pancito": []}
def cargar_sistema():
    for categoria in productos_disponible:
        productos_disponible[categoria] = []
    for categoria in cantidad_disponible:
        cantidad_disponible[categoria] = []
def subir_stock():
    print("las categorías disponibles son \n",productos_disponible.keys)
    categoria = input("elegi la categoria")
    if categoria in productos_disponible:
        producto = input("cual es el nombre del producto")
        try: 
            cantidad = int(input(" que cantidad vas a añadir"))
            productos_disponible[categoria].append(producto)
            cantidad_disponible[categoria].append(cantidad)
            print(f"{cantidad} unidad(es) de '{producto}' agregadas a '{categoria}'")
        except ValueError:
            print("esta mal la cantidad debe ser un numero entero")
        else:
             print("categoria no valida ")
def ver_stock():
    print("el total de stock es \n")
    for categoria in productos_disponible:
        print(f"categoría {categoria} \n")
        productos = productos_disponible[categoria]
        cantidades = cantidad_disponible[categoria]
        if len(productos) == 0:
            print("no hay productos")
        else:
             for i in range(len(productos)):
                print(f"{productos[i]}: {cantidades[i]} unidades")
def contar(lista_cantidades):
    varieda = len(lista_cantidades)
    unidades = sum(lista_cantidades)
    print(f"la cnt de productos distintos es de{varieda} \n")
    print(f"la suma total de unidades es de{unidades} \n") 