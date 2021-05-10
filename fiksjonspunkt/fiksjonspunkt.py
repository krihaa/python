import matplotlib.pyplot as plt
import math

# x,y startpunkt, c: antall iterasjoner, a: 2d array for plottet
# itererer til fiksjonspunkt for formelen 1/5(xy+y^2-1, x^3-y^2+3)
def fiksjon(x,y,c, a):
	if c <= 0:
		return x,y,a
	x,y,a = fiksjon(x,y,c-1, a)
	a[0].append(x)
	a[1].append(y)
	return (x*y+pow(y,2)-1)/5, (pow(x,3)-pow(y,2)+3) / 5, a

a = [[],[]]
a2 = [[],[]]

fiksjon(0,0,30, a)
fiksjon(-1,1,30, a2)

plt.plot(a[0], a[1])
plt.plot(a2[0], a2[1])
plt.show()
