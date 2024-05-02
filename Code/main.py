## PROYECTO 01
## Britney Valoy

import matplotlib.pyplot as plt

# Definiendo los algoritmos a utilizar a travez de funciones
def algoritmo_DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_incremento = dx / steps
    y_incremento = dy / steps
    
    x = x1
    y = y1
    puntos = [(round(x), round(y))]
    
    for _ in range(steps):
        x += x_incremento
        y += y_incremento
        puntos.append((round(x), round(y)))
    
    return puntos

def algoritmo_Bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x = x1
    y = y1
    puntos = [(x, y)]
    if dx > dy:
        p = 2 * dy - dx
        incremento = [(1 if x2 > x1 else -1), 1]
        constante = [2 * dy, 2 * (dy - dx)]
        steps = dx
    else:
        p = 2 * dx - dy
        incremento = [1, (1 if y2 > y1 else -1)]
        constante = [2 * dx, 2 * (dx - dy)]
        steps = dy

    for _ in range(steps):
        if p >= 0:
            x += incremento[0]
            y += incremento[1]
            p += constante[1]
        else:
            p += constante[0]
            x += incremento[0]
            y += incremento[1]
        puntos.append((x, y))
    
    return puntos

def algoritmo_circunferencia(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    puntos = []
    puntos.extend(graficar_circunferencia(xc, yc, x, y))
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        puntos.extend(graficar_circunferencia(xc, yc, x, y))
    
    return puntos

def graficar_circunferencia(xc, yc, x, y):
    puntos = []
    puntos.append((xc + x, yc + y))
    puntos.append((xc - x, yc + y))
    puntos.append((xc + x, yc - y))
    puntos.append((xc - x, yc - y))
    puntos.append((xc + y, yc + x))
    puntos.append((xc - y, yc + x))
    puntos.append((xc + y, yc - x))
    puntos.append((xc - y, yc - x))
    return puntos

def algoritmo_elipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = ry ** 2 - rx ** 2 * ry + 0.25 * rx ** 2
    dx = 2 * ry ** 2 * x
    dy = 2 * rx ** 2 * y

    puntos = []
    puntos.extend(graficar_elipse(xc, yc, x, y))
    while dx < dy:
        x += 1
        dx += 2 * ry ** 2
        if p1 < 0:
            p1 += dx + ry ** 2
        else:
            y -= 1
            dy -= 2 * rx ** 2
            p1 += dx - dy + ry ** 2
        puntos.extend(graficar_elipse(xc, yc, x, y))
    
    p2 = ry ** 2 * (x + 0.5) ** 2 + rx ** 2 * (y - 1) ** 2 - rx ** 2 * ry ** 2
    while y > 0:
        y -= 1
        dy -= 2 * rx ** 2
        if p2 > 0:
            p2 += rx ** 2 - dy
        else:
            x += 1
            dx += 2 * ry ** 2
            p2 += dx - dy + rx ** 2
        puntos.extend(graficar_elipse(xc, yc, x, y))

    return puntos

def graficar_elipse(xc, yc, x, y):
    puntos = []
    puntos.append((xc + x, yc + y))
    puntos.append((xc - x, yc + y))
    puntos.append((xc + x, yc - y))
    puntos.append((xc - x, yc - y))
    return puntos

def graficar_puntos(puntos):
    x, y = zip(*puntos)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Definiendo el menu principal
def main():
    while True:
        print("Seleccione un algoritmo:")
        print("1. Presentación formal")
        print("2. Algoritmo DDA para dibujar líneas")
        print("3. Algoritmo de Bresenham para dibujar líneas")
        print("4. Algoritmo de punto medio para la circunferencia")
        print("5. Algoritmo de punto medio para la elipse")
        print("6. Salir")
        opcion = int(input("Ingrese su elección: "))
        
        if opcion == 1:
            print("\n" * 2)  
        
            print("                                                    Universidad Tecnológica de Panamá")
            print("                                            Facultad de Ingeniería y Sistemas Computacionales")
            print("                                                  Licenciatura en Ingeniería de Software")
            print("                                                              Proyecto 01")
            print("                                                  Asignatura: Computación Gráfica Visual")
            print("                                                        Estudiante: Britney Valoy")
            print("                                                              Grupo: 1SF142")
            print("                                                     Sometido a criterio de : Marck Tack")
            print("                                                  Fecha de entrega: 06 de mayo del 2024")

            print("\n" * 2)  
        elif opcion == 2:
            x1, y1 = map(int, input("Ingrese las coordenadas del punto inicial (x1 y1): ").split())
            x2, y2 = map(int, input("Ingrese las coordenadas del punto final (x2 y2): ").split())
            puntos = algoritmo_DDA(x1, y1, x2, y2)
            graficar_puntos(puntos)
        elif opcion == 3:
            x1, y1 = map(int, input("Ingrese las coordenadas del punto inicial (x1 y1): ").split())
            x2, y2 = map(int, input("Ingrese las coordenadas del punto final (x2 y2): ").split())
            puntos = algoritmo_Bresenham(x1, y1, x2, y2)
            graficar_puntos(puntos)
        elif opcion == 4:
            xc, yc = map(int, input("Ingrese las coordenadas del centro del círculo (xc yc): ").split())
            r = int(input("Ingrese el radio del círculo: "))
            puntos = algoritmo_circunferencia(xc, yc, r)
            graficar_puntos(puntos)
        elif opcion == 5:
            xc, yc = map(int, input("Ingrese las coordenadas del centro de la elipse (xc yc): ").split())
            rx = int(input("Ingrese el radio en x de la elipse: "))
            ry = int(input("Ingrese el radio en y de la elipse: "))
            puntos = algoritmo_elipse(xc, yc, rx, ry)
            graficar_puntos(puntos)
        elif opcion == 6:
            print("Nos vemos pronto...")
            break
        else:
            print("Selección no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
