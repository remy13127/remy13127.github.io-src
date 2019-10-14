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
