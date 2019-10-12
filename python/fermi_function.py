import matplotlib.pyplot as plt
import numpy as np

mu = [2,5]
epsilon = np.linspace(0,10,1000)
kT = 0.0001

for m in mu:
	plt.plot(epsilon,1/(np.exp((epsilon-m)/kT)+1))

plt.fill_between(epsilon,1/(np.exp((epsilon-mu[0])/kT)+1),1/(np.exp((epsilon-mu[1])/kT)+1),hatch='/')
plt.xticks([2,5],[r"$\mu_2$","$\mu_1$"])
plt.xlabel(r"$\epsilon$")
plt.ylabel("$\overline{n}$")
plt.title(r"$\int dE (f_1(E) - f_2(E))$")
plt.savefig("/home/remy13127/Desktop/Website/content/images/fermi_difference.png")
plt.close()

mu2 = [2,2.1]
epsilon = np.linspace(0,10,1000)
kT = 0.5

for m in mu2:
	plt.plot(epsilon,1/(np.exp((epsilon-m)/kT)+1))

plt.xticks([2.05],[r"$\mu_2 \approx \mu_1$"])
plt.xlabel(r"$\epsilon$")
plt.ylabel("$\overline{n}$")
plt.title(r"$k\Theta >> |\mu_1 - \mu_2|$")
plt.savefig("/home/remy13127/Desktop/Website/content/images/fermi_highT.png")
plt.close()

mu = 2.0
epsilon = np.linspace(0,10,1000)
kT = 0.0001

plt.plot(epsilon,1/(np.exp((epsilon-mu)/kT)+1),label='f')
plt.plot(epsilon,(1/(np.exp((epsilon-mu)/kT)+1))**2,'--',label=r'$f^2$')
plt.plot(epsilon,1-1/(np.exp((epsilon-mu)/kT)+1),':',label='(1-f)')

plt.xticks([2.0],[r"$\mu$"])
plt.xlabel(r"$\epsilon$")
plt.ylabel("$\overline{n}$")
plt.legend()
plt.title(r"$k\Theta << |\mu_1 - \mu_2|$")
plt.savefig("/home/remy13127/Desktop/Website/content/images/fermi_lowT.png")
plt.close()

