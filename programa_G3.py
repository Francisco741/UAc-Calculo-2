import matplotlib.pyplot as plt
import numpy as np
from time import sleep


#Função matemática
def f(x):
    return np.log(x / (x**2 - 9))


# Função para calcular a derivada
def calcular_derivada(a):
    h = 1
    b1 = (f(a + h) - f(a)) / h
    h = h / 10
    b2 = (f(a + h) - f(a)) / h
    while abs(b2 - b1) >= 0.000001:
        b1 = b2
        h = h / 10
        b2 = (f(a + h) - f(a)) / h
    return b2


# Função para calcular a ordenada de todos os pontos da reta tangente
def y_reta_tangente(x, x0):
    m = calcular_derivada(x0)
    b = f(x0) - m * x0
    y = m * x + b
    return y


# Função para calcular a equação da reta tangente
def reta_tangente(x0):
    m = calcular_derivada(x0)
    b = f(x0) - m * x0
    if b >= 0:
        return f"{round(m, 2)}x +{round(b, 2)}"
    else:
        return f"{round(m, 2)}x {round(b, 2)}"


# Função para desenhar o gráfico da função e da reta tangente
def desenhar_grafico(a):
    x = np.linspace(-50, 50, 100000)
    y = f(x)
    x0 = a
    y0 = f(x0)
    plt.plot(x, y, label='Função ln(x / (x^2 - 9))')
    plt.plot(x, y_reta_tangente(x, x0), label=f'Reta tangente y = {reta_tangente(x0)}')
    plt.scatter(x0, y0, color='red', label=f'Ponto de interseção ({round(x0, 2)}, {round(y0, 2)})')
    plt.title('Gráfico da função ln(x / (x^2 - 9))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-10, 10)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.legend()
    plt.show()


# Função principal do programa
def main():
    a = float(input("Introduza o valor de a: "))
    if (a > -3 and a < 0) or a > 3:
        print(f"f\'({a}): {calcular_derivada(a)}")
        desenhar_grafico(a)
    else:
        print("Número não pertence ao domínio")
    sleep(60)
    return None


main()
