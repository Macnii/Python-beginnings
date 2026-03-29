#   By: Macni 
#   Date: 28 de marzo del 2026
print("==============================================================\n")
#Ciclo para preguntar al usuario si quiere continuar o salir
carrito = []
while True:
    
    #Ciclo para pregunar al usuario si quiere agregar un producto
    while True:
        pregunta1 = input(f"Quieres agregar un producto? (s/n): \n").lower().strip()
        if pregunta1 == "s":
            agregar = carrito.append(input("AGREGAR: \n"))
        elif pregunta1 == "n":
            print(f"Tu carrito tiene {carrito}")
            break
        else:
            print("Invalido: ingresa (s / n) ")
    #Ciclo para pregunar al usuario si quiere eliminar un producto
    while True:
        eliminar1 = input("Quieres eliminar un proucto? (s/n): \n").lower().strip()
        if eliminar1 == "s":
            if not carrito:
                print("Tu carrito esta vacio")
            else:
                eliminar_producto = carrito.remove(input("¿Cual quires eliminar? \n"))
            
        elif eliminar1 == "n":
            print(f"Tu carrito tiene {carrito}")
            break 
        else:
            print("Invalido: ingresa (s / n) ")
    #Ciclo para pregunar al usuario si quiere salir del programa
    while True:
        
        pregunta2 = input(f"¿Quieres salir? (s/n): \n").lower().strip()
        if pregunta2 == "s":
            break
        elif pregunta2 == "n":
            print(f"Tu carrito tiene {carrito}")
        else:
            print("Invalido: ingresa (s / n) ")
    #Si cumple sale del programa
    if pregunta2 == "s":
        print("Gracias por usar el programa, adios!\n")
        break



    