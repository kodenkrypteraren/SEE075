
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,1500)
y = -x**2 + x  + 0.75

plt.ylabel('x_n+1')
plt.xlabel('x_n')
plt.plot(x,y)

# %%

#logistic map
#x_n+1 = r*x_n(1-x_n)
def population(xn, r):
    return (r*(xn)*(1-xn))  

#långsiktigt beteende för givna initial conditions xn, r, över tiden nrOfIterations
def longTerm(xn, r, nrOfIterations):
    storlek = []
    for i in range(0,nrOfIterations):
            storlek.append(population(xn,r))
            xn = r*np.sin(xn)*(1-np.sin(xn)) 
    return storlek

# %%
xn = 0.6
r = 1.7
nrOfIterations = 20
nrOfIterationsList = [i for i in range(nrOfIterations)]
plt.plot(nrOfIterationsList,  longTerm(xn,r,nrOfIterations))
plt.xlabel('tid, xn =' + str(xn) + ' r = ' + str(r))
plt.ylabel('jämviktspopulation')
# %% bipartitionsgraf, zoom, fraktal
antalIterationer = 150
xn = 0.4
#skapar många punkter r på x-axeln
rAxeln = np.linspace(0,4,200)  # zoomar genom begränsning av r 

#beräknar jämviktsvärdet för varje r. y == f(x) == f(r)
yAxeln = list(map(lambda a: longTerm(xn, a, antalIterationer), rAxeln))

plt.plot(rAxeln, yAxeln)
plt.xlabel('reproduktionsvärdet r' + ' 3 till 3.5')
plt.ylabel('populationsjämvikten xn' + xn )

# %% bipartitionsgraf, zoom, fraktal
antalIterationer = 1000
xn = 0.4
rAxeln = np.linspace(0,4,200) # zoomar genom begränsning av r 
#beräknar jämviktsvärdet för varje r. y == f(x) == f(r)
yAxeln = list(map(lambda a: longTerm(xn, a, antalIterationer), rAxeln))

plt.plot(rAxeln, yAxeln)
plt.xlabel('reproduktionsvärdet r' + ' 3.45 till 3.5')
plt.ylabel('populationsjämvikten xn' + xn )


# %% bipartitionsgraf
antalIterationer = 150
xn = 0.4
rAxeln = np.linspace(0,4,200)
#beräknar jämviktsvärdet för varje r. y == f(x) == f(r)
yAxeln = list(map(lambda a: longTerm(xn, a, antalIterationer), rAxeln))

plt.plot(rAxeln, yAxeln)
plt.xlabel('reproduktionsvärdet r' + ' 0 till 4')
plt.ylabel('populationsjämvikten xn' + xn )


