import numpy as np
import matplotlib.pyplot as plt

sigma = 1. #standard deviation
mu = 10. #mean
tau = .05 #time constant

dt = .001 #time step
T = 1. #total time
n = int(T/dt) #number of time steps
t = np.linspace(0.,T,n) #vector of times

sigma_bis = sigma*np.sqrt(2. / tau)
sqrtdt = np.sqrt(dt)

x = np.zeros(n)

#Euler-Maruyama method

for i in range(n-1):
	x[i+1] = x[i] + dt*(-(x[i]-mu)/tau)+ sigma_bis*sqrtdt*np.random.randn()

fig, ax = plt.subplots(1,1,figsize=(8,4))
ax.plot(t,x,lw=2)

plt.savefig("/home/remy13127/Documents/ghpages/content/images/ornsteinprocess.png")
plt.close()

ntrials = 100000
X = np.zeros(ntrials)

# We create bins for the histograms.
bins = np.linspace(-2., 14., 100)
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
for i in range(n):
   	# We update the process independently for
	# all trials
	X += dt * (-(X - mu) / tau) + sigma_bis * sqrtdt * np.random.randn(ntrials)
	# We display the histogram for a few points in
	# time
	if i in (5, 50, 900):
		hist, _ = np.histogram(X, bins=bins)
		ax.plot((bins[1:] + bins[:-1]) / 2, hist, {5: '-', 50: '.', 900: '-.', }[i],label=f't={i * dt:.2f}')
	ax.legend()

plt.savefig("/home/remy13127/Documents/ghpages/content/images/ornsteindistrib.png")
plt.close()
