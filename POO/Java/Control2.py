altura = float(input("Ingrese su altura(cm): "))
cintura = float(input("Ingrese su cintura(cm): "))

if(cintura / altura < 0.5 ):
    print("Su ICA es de: ", round(cintura / altura, 2),"cm por lo tanto estas en la categoria NORMAL")
elif(cintura / altura >= 0.536 and cintura / altura <= 0.583):
    print("Tu ICA es de: ", round(cintura / altura, 2), "cm por lo tanto estas en la categoria ROBUSTO")
else:
    print("Tu ICA es de: ", round(cintura / altura, 2), "cm por lo tanto estas en RIESGO FATAL")