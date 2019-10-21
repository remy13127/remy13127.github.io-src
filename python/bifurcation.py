import matplotlib.pyplot as plt
import numpy as np

mu = np.linspace(-10,0,1000)

plt.plot(mu,np.sqrt(-mu),'--',label = r"$x^* = \sqrt{-\mu}$",color="blue")
plt.plot(mu,-np.sqrt(-mu),label=r"$x^* = - \sqrt{-\mu}$",color="blue")
plt.plot(mu,np.zeros(len(mu)),color="red")
plt.plot(-mu,np.zeros(len(mu)),color="red")
plt.legend()
plt.xlabel(r'$\mu$')
plt.ylabel(r"$x^*$")
plt.title("Saddle-node bifurcation")
plt.savefig("/home/remy13127/Documents/ghpages/content/images/saddle_node_birfurcation.png")
plt.close()

plt.plot(mu,mu,'--',label = r"$x^* = \mu$",color="blue")
plt.plot(-mu,-mu,color="blue")
plt.plot(mu,np.zeros(len(mu)),color="red",label=r"$x^* = 0$")
plt.plot(-mu,np.zeros(len(mu)),'--',color="red")
plt.legend()
plt.xlabel(r'$\mu$')
plt.ylabel(r"$x^*$")
plt.title("Trans-critical bifurcation")
plt.savefig("/home/remy13127/Documents/ghpages/content/images/transcritical_birfurcation.png")
plt.close()

