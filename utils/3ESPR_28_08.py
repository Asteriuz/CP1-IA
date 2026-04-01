import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def derivadas():
    a = np.sum((x_r - np.mean(x_r))*(y_r - np.mean(y_r)))/np.sum((x_r - np.mean(x_r))**2)
    b = np.mean(y_r) - a*np.mean(x_r)
    return a,b
def calcula_erro(a,b):
    erro = 0
    for k in range(len(x_r)):
        y_p = a * x_r[k] + b
        erro += (y_p - y_r[k]) ** 2
    return erro

data = pd.read_excel('C:\\Users\\labsfiap\\Downloads\\data.xlsx')
x_r = data['x']
y_r = data['y']

N = 100
A = np.linspace(-10,10,N)
B = np.linspace(-10,10,N)

erros = np.zeros(shape = (N,N))
menor_a = A[0]
menor_b = B[0]
menor_erro = calcula_erro(A[0],B[0])
for i,a in enumerate(A):
    for j,b in enumerate(B):
        erro = calcula_erro(a,b)
        erros[i][j] = erro
        if erro < menor_erro:
            menor_erro = erro
            menor_a = a
            menor_b = b
a,b = derivadas()
melhor_reta = menor_a * x_r + menor_b
plt.plot(x_r,melhor_reta,'r',label= f'Melhor a: {menor_a:.2f}\nMelhor b: {menor_b:.2f}')
plt.plot(x_r, a*x_r + b,'g',label = f"Via derivadas: a = {a}, b = {b}")
plt.plot(x_r,y_r,'bo',label='Dados')
plt.legend()
plt.figure()
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(A, B)
# ax.plot_surface(X, Y, erros, cmap='viridis')
plt.show()
