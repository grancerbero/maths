import matplotlib.pyplot as plt


def calcular_probabilidad(k):
    numerador = 1
    for i in range(365 - k + 1, 366):
        numerador *= i
    denominador = 365 ** k
    return 1 - numerador / denominador

k_values = list(range(1, 101))  # Valores de k de 1 a 100
probabilidades = [calcular_probabilidad(k) for k in k_values]

plt.plot(k_values, probabilidades, marker='.', linestyle='')
plt.xlabel('Número de personas (k)')
plt.ylabel('Probabilidad de al menos una coincidencia')
plt.title('Probabilidad de coincidencia de cumpleaños vs Número de personas')
plt.grid(True)

# Línea en el 50%
plt.axhline(y=0.5, color='r', linestyle='-')
#plt.show()
plt.savefig('grafico_probabilidad_cumpleanos.png')