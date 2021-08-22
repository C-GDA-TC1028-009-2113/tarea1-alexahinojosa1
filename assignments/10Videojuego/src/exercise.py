def main():
    #escribe tu código abajo de esta línea
    vnuevos= int(input("Dame la cantidad de juegos nuevos: "))
    vusados= int(input("Dame la cantidad de juegos usados: " ))
    
    total = (vnuevos*1000)+(vusados*350)
    print ("El total de la compra es:", total)

if __name__ == '__main__':
    main()
