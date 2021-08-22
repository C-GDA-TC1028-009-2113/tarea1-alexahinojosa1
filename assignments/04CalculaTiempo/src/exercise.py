def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Dame tu edad: "))
    a = int(input("Dame el año actual: "))

    faltante =100- edad
    a_final= faltante+a

    print("Cumplirás 100 años en el año:",a_final)

if __name__ == '__main__':
    main()
