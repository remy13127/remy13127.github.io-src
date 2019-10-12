import matplotlib.pyplot as plt
import numpy as np

pi=np.pi
N=1000
D=0.5

x = np.linspace(-5,5,1000)
t = [0.1,0.2,0.5,2]

for time in t:
	plt.plot(x,N/np.sqrt(4*pi*D*time)*np.exp(-x**2/(4*D*time)),label="t = "+str(time))

plt.ylabel(r"f(x,t)")	
plt.xlabel(r"x")
plt.title("Diffusion of N = "+str(N)+" Brownian particles, with D = "+str(D))
plt.legend()
plt.savefig("/home/remy13127/Desktop/Website/content/images/brownian_gaussian.png")
