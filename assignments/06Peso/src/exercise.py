def main():
    #escribe tu código abajo de esta línea
    peso_i= float(input("Dame el peso inicial: "))
    peso_f= float(input("Dame el peso final: "))
    meses= int(input("Dame la cantidad de meses: "))
     
    meta= peso_i - peso_f
    bajarpormes= meta/meses
    float(bajarpormes)
    print("Lo que debes bajar por mes es:",bajarpormes)





if __name__ == '__main__':
    main()
