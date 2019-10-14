Title: Stochastic differential equations
Date: 2019-12-10 10:20
Category: Physics
Tags: Stochastic, Differential equations
Slug: stochastic-differential-equations
Author: Rémy Torro
Summary: Properties of stochastic differential equations.

> How can we define stochastic differential equations? 

We are interested in solving the following stochastic differential equation: 

$$ dx = a(x,t) dt + b(x,t) dW$$

Firstly, we must introduce rules for changing variables in a S.D.E. Assume $y = g(x)$:

$$dy = y(t+dt) - y(t) = g(x(t+dt))-g(t) = g(x+dx)-g(x) = g(x) + g'(x)dx + \frac{1}{2}g''(x) (dx)^2 - g(x) = g'(x)[a(x,t) dt + b(x,t) dW] + \frac{1}{2}g''(x) [a^2(x,t)(dt)^2 + b^2(x,t)(dW)^2 + 2 a(x,t) b(x,t) dt dW] = [g'(x) a(x,t) + \underbrace{\frac{1}{2}g''(x)b^2(x,t)}_{\textrm{additional term}}]dt + g'(x)b(x,t)dW
$$

The Ornstein–Uhlenbeck process is an exactly soluble S.D.E, the equivalent to the original [Langevin](https://remy13127.github.io/brownian-motion.html) equation. 

$$ dx = - \gamma x dt + c dW$$

This S.D.E. can be solved by variation of parameters. Let's set $y = x e^{\gamma t}$:

$$dy = (x+dx)e^{\gamma(t+dt)} - xe^{\gamma t} = (x+dx)e^{\gamma t}(1+\gamma dt) - xe^{\gamma t} = (xe^{\gamma t}+e^{\gamma t}dx)(1+\gamma dt) - xe^{\gamma t} = \gamma x e^{\gamma t} dt + e^{\gamma t} dx + \underbrace{dx dt \gamma e^{\gamma t}}_{0} = \gamma x e^{\gamma t} + [-\gamma x dt + c dW]e^{\gamma t} = c e^{\gamma t} dW $$

$$ y(t) = y(0) + c\int_0^t e^{\gamma t'} dW(t') = y(0) + \lim_{N \rightarrow \infty} \sum_{n=0}^{N-1} c e^{\gamma n \Delta t}\Delta W_n$$

$$x(t) = x(0) e^{-\gamma t} + c\int_0^t e^{\gamma(t' -t)} dW(t) $$

<center>![Ornstein-Uhlenbeck process](images/ornsteinprocess.png)</center>


<center>![Ornstein-Uhlenbeck distribution at given times](images/ornsteindistrib.png)</center>
