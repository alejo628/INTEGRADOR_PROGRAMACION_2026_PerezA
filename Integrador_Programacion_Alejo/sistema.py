import menu
import gestion_stock
def main():
    gestion_stock.cargar_sistema()
    while True:
        opcion = menu.menu_stock()
        if opcion == 1:
            print("CARGAR STOCK")
            gestion_stock.subir_stock()
        elif opcion == 2:
            gestion_stock.ver_stock()
        elif opcion == 3:
            categoria = input("ingresa la categoria que queres contar: (enlatados, frutas, congelados, panaderia) \n")
            if categoria in gestion_stock.cantidad_disponible:
                lista_cantidades = gestion_stock.cantidad_disponible[categoria]
                gestion_stock.contar(lista_cantidades)
            else:
                print("la categoria no es valida")       
        elif opcion == 4:
            print("adios banana(Nico y ale porfa apruevenme)")
            break
        else:
            print("la opcion no es valida maestro intenta de nuevo")
            
if __name__ == "main":
    main()
    