Title: Ornstein–Uhlenbeck process
Date: 2019-12-10 10:20
Category: Physics
Tags: Stochastic, Differential equations
Slug: ornstein-uhlenbeck
Author: Rémy Torro
Summary: Properties of Ornstein-Uhlenbeck processes.

<br>

> How can we define stochastic differential equations? 

We are interested in solving stochastic differential equations of this kind: 

$$ dx = a(x,t) dt + b(x,t) dW$$

## Itô's lemma
Itô's lemma is an identity used to find the differential of a time-dependent function of a stochastic process. It is the stochastic calculus counterpart of the chain rule. One can Taylor-expand a function up to its second derivatives and keep only terms up to first order in time ($dt$) and second order in the Wiener process increment $dW$. Let's consider $y = g(x)$. 

$$dy = y(t+dt) - y(t) = g(x(t+dt))-g(t) = g(x+dx)-g(x) = g(x) + g'(x)dx + \frac{1}{2}g''(x) (dx)^2 - g(x) = g'(x)[a(x,t) dt + b(x,t) dW] + \frac{1}{2}g''(x) [a^2(x,t)(dt)^2 + b^2(x,t)\underbrace{(dW)^2}_{dt} + 2 a(x,t) b(x,t) dt dW] = [g'(x) a(x,t) + \underbrace{\frac{1}{2}g''(x)b^2(x,t)}_{\textrm{additional term}}]dt + g'(x)b(x,t)dW
$$

In the limit $dt \rightarrow 0$, the terms $dt^2$ and $dt dW$ go to zero faster than $dW^2$, which is $O(dt)$. We can set $dt^2$ and $dtdW$ to zero and substitute $dW^2$ for $dt$.

$$ dy = \left[g'(x) a(x,t) + \frac{1}{2}g''(x)b^2(x,t)\right]dt + g'(x)b(x,t)dW $$

<hr>

# Problem

For $I(T)=\int_0^T (dW)^2= \lim_{N \rightarrow \infty} \sum_{n=1}^{N-1} (\Delta W_n)^2$, evaluate the mean and variance:

$$\langle I(T) \rangle = \int_0^T \langle (dW)^2 \rangle = \int_0^T dt = T$$

$$V[I(T)] = \lim_{N \rightarrow \infty} V\left[\sum_{n=0}^{N-1} (\Delta W_n)^2 \right] = \lim_{N\rightarrow \infty} \sum_{n=0}^{N-1} V[(\Delta W_n)^2]$$

We can express the variance of $(\Delta W)^2$ as:

$$ V[(\Delta W_n)^2] = \langle (\Delta W_n)^4 \rangle - \langle (\Delta W_n)^2 \rangle^2 = \int_{-\infty}^{\infty} \frac{(\Delta W)^4}{\sqrt{2 \pi \Delta t}} e^{-\frac{(\Delta W)^2}{2\Delta t}} = 3 (\Delta t)^2 - \underbrace{(\Delta t)^2}_{\langle (\Delta W)^2 \rangle = \Delta t} = 3 (\Delta t)^2 - (\Delta t)^2 = 2 (\Delta t)^2$$

<hr>

##Ornstein-Ulhenbeck process

The Ornstein–Uhlenbeck process is an exactly soluble S.D.E, the equivalent to the original [Langevin](https://remy13127.github.io/brownian-motion.html) equation. 

$$ dx = - \gamma x dt + c dW$$

This S.D.E. can be solved by variation of parameters. Let's set $y = x e^{\gamma t}$:

$$dy = (x+dx)e^{\gamma(t+dt)} - xe^{\gamma t} = (x+dx)e^{\gamma t}(1+\gamma dt) - xe^{\gamma t} = (xe^{\gamma t}+e^{\gamma t}dx)(1+\gamma dt) - xe^{\gamma t} = \gamma x e^{\gamma t} dt + e^{\gamma t} dx + \underbrace{dx dt \gamma e^{\gamma t}}_{0} = \gamma x e^{\gamma t} + [-\gamma x dt + c dW]e^{\gamma t} = c e^{\gamma t} dW $$

As a result:

$$ y(t) = y(0) + c\int_0^t e^{\gamma t'} dW(t') $$

But since $x=ye^{-\gamma t}$, we have:

$$x(t) = x(0) e^{-\gamma t} + c\int_0^t e^{\gamma(t' -t)} dW(t) $$

Since $x(t)$ is the sum of Gaussian random variables, it is itself Gaussian and its distribution is completely determined by the mean and variance. 

$$ \langle x(t) \rangle = x(0) e^{-\gamma t}$$
$$ V[x(t)] = \langle x^2(t) \rangle = \lim_{N \rightarrow \infty} \sum_{n=0}^{N-1} V[c e^{-\gamma n \Delta t}\Delta W_n] = \lim_{N\rightarrow \infty} \sum_{n=0}^{N-1} c^2 e^{-2\gamma n\Delta t}\Delta t = \int_0^t c^2 e^{-2\gamma t}dt$$

# Numerical implementation

In the following, we will be interested in S.D.Es of the form:

$$ dx = \underbrace{- \frac{x-\mu}{\tau} dt}_{\textrm{deterministic term}} + \underbrace{\sigma \sqrt{\frac{2}{\tau}} dW}_{\textrm{stochastic term}}$$

where $x(t)$ is the stochastic process, $\mu$ the mean, $\sigma$ the standard deviation and $\tau$ the time constant. $W$ is a Wiener process. Using the Euler-Maruyama method, we can discretize time and add infinitesimal steps to the process at every time step. For the following equation:

$$ dx = a(t,x) dt + b(t,x) dW$$

We can apply the Euler-Maruyama discretization and get:

$$ x_{n+1} = x_n + dx = x_n + a(t,x_n)dt + b(t,x_n) \sqrt{dt}\xi \qquad \xi \approx \mathcal{N}(0,1)$$

	::python
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
		x[i+1] = x[i] + dt*(-(x[i]-mu)/tau)+sigma_bis*sqrtdt*np.random.randn()

	fig, ax = plt.subplots(1,1,figsize=(8,4))
	ax.plot(t,x,lw=2)



<center>![Ornstein-Uhlenbeck process](images/ornsteinprocess.png)</center>


	::python
	ntrials = 100000
	X = np.zeros(ntrials)

	# We create bins for the histograms.
	bins = np.linspace(-2., 14., 100)
	fig, ax = plt.subplots(1, 1, figsize=(8, 4))
	for i in range(n):
		# We update the process independently for
		# all trials
		X += dt * (-(X - mu) / tau) + sigma_bis * sqrtdt * np.random.randn(ntrials)
		# We display the histogram for a few points in time
		if i in (5, 50, 900):
			hist, _ = np.histogram(X, bins=bins)
			ax.plot((bins[1:] + bins[:-1]) / 2, hist, {5: '-', 50: '.', 900: '-.', }[i],label=f't={i * dt:.2f}')
		ax.legend()

<center>![Ornstein-Uhlenbeck distribution at given times](images/ornsteindistrib.png)</center>

The distribution of the process tends to a Gaussian distribution with mean $\mu=10$ and standard deviation $\sigma = 1$.

<hr>

##Stratonovich definition
Itô's integral can be defined as:

$$ \int_0^t f(x(t'),t') dW(t') = \lim_{N\rightarrow \infty}\sum_{n=0}^{N-1} f(x(n\Delta t),n\Delta t)\Delta W_n$$

Using Stratonovich's definition, we will displace the time increments to be in the middle of an interval such that:

$$ \int_0^t f(x(t'),t')dW(t') = \lim_{N \rightarrow \infty} \sum_{n=0}^{N-1} f\left(\frac{x((n+1)\Delta t)+x(n\Delta t)}{2},n\Delta t\right)\Delta W_n $$

$$ x(N\Delta t) = x(0) + \sum_{n=0}^{N-1} a \left(\frac{x((n+1)\Delta t)+x(n\Delta t)}{2},n\Delta t \right)\Delta t+\sum_{n=0}^{N-1} b \left(\frac{x((n+1)\Delta t)+x(n\Delta t)}{2},n\Delta t \right)\Delta W_n$$

We have:

$$\frac{x((n+1)\Delta t)+x(n\Delta t)}{2} = \frac{2x(n\Delta t)+\Delta x_n}{2} = x(n\Delta t) + \frac{\Delta x_n}{2} $$

where $\Delta x_n = x_{n+1} - x_{n}$. 

$$ x(N\Delta t) = x(0) + \sum_{n=0}^{N-1} a \left(x(n\Delta t) + \frac{\Delta x_n}{2},n\Delta t \right)\Delta t+\sum_{n=0}^{N-1} b \left(x(n\Delta t) + \frac{\Delta x_n}{2},n\Delta t \right)\Delta W_n$$

$$a \left(x_n + \frac{\Delta x_n}{2},n\Delta t \right)\Delta t \approx a_n \Delta t + \underbrace{\frac{\partial a_n}{\partial x}\frac{\Delta x_n}{2} \Delta t}_{\Delta x \Delta t = 0}+\underbrace{\frac{1}{2}\frac{\partial^2 a_n}{\partial x^2}\left(\frac{\Delta x_n}{2}\right)^2 \Delta t}_{(\Delta x)^2 \Delta t = 0} + ... \approx a_n \Delta t$$

$$b \left(x_n + \frac{\Delta x_n}{2},n\Delta t \right)\Delta W_n \approx b_n \Delta W_n + \underbrace{\frac{\partial b_n}{\partial x}\frac{\Delta x_n}{2} \Delta W_n}_{\Delta x_n \Delta W_n = a_n \Delta t \Delta W + b_n (\Delta W_n)^2}+\underbrace{\frac{1}{2}\frac{\partial^2 b_n}{\partial x^2}\left(\frac{\Delta x_n}{2}\right)^2 \Delta t}_{(\Delta x)^2 \Delta W_n = 0} + ... \approx b_n \Delta W_n + \frac{1}{2}\frac{\partial b_n}{\partial x} b_n \Delta t$$

As a result:

$$ x(N\Delta t) = x(0) + \sum_{n=0}^{N-1} \left[a(x(n\Delta t),n\Delta t)+\frac{1}{2}\frac{\partial b}{\partial x}b(x(n\Delta t),n\Delta t)\right] \Delta t + b(x(n\Delta t,n\Delta t))\Delta W_n$$
