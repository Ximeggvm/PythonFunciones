# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea.
def pies_cm(pies):
    p_cm=(pies*30.40)
    return p_cm
def pulgadas_cm(pulgadas):
    pl_cm=(pulgadas*2.54)
    return pl_cm
def yarda_cm(yardas):
    y_cm=(yardas*91.44)
    return y_cm

p_pl_y=input("¿Qué quieres convertir a cm:pies, pulgadas o yardas?")
if p_pl_y=="pies":
    pies=float(input("Dame los pies que quieres convertir: "))
    if pies==0:
        print ("Error")
    if  pies<0:
        print ("Error")
    if pies>3:
        print ("Error")
    piesf=print("Serían un total de: ",pies_cm(pies),"cm")
if p_pl_y=="pulgadas":
    pulgadas=float(input("Dame las pulgadas que quieres convertir: "))
    if pulgadas==0:
        print ("Error")
    if  pulgadas<0:
        print ("Error")
    if pulgadas>3:
        print ("Error")
    pulgadasf=print("Serían un total de: ",pulgadas_cm(pulgadas),"cm")
if p_pl_y=="yardas":
    yardas=float(input("Dame las yardas que quieres convertir: "))
    if yardas==0:
        print ("Error")
    if  yardas<0:
        print ("Error")
    if yardas>3:
        print ("Error")
    yardasf=print("Serían un total de: ",yarda_cm(yardas),"cm")    

    if __name__ == '__main__':
    main()
