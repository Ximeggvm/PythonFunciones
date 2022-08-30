# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
def area_rec(base,altura):
    a_r=(base*altura)
    return a_r
def volumen_rec(base,altura,prof):
    v_r=(base*altura*prof)
    return v_r
a_v=input("¿Qué quieres sacar: área o volúmen?")
if a_v=="área":
    base=float(input("Dame la base del rectangulo: "))
    altura=float(input("Dame el área del rectangulo:"))
    area=print("El área es igual a: ",(round(area_rec(base,altura))))
if a_v=="volúmen":
    base=float(input("Dame la base del rectangulo: "))
    altura=float(input("Dame el área del rectangulo:"))
    prof=float(input("Dame la profundidad del rectangulo: "))
    volumen=print("El volumen es igual a: ",(round(volumen_rec(base,altura,prof))))


if __name__ == '__main__':
    main()

