Title: Rayleigh-Benard convection
Date: 2019-12-10 10:20
Category: Physics
Tags: Dynamical systems, instabilities
Slug: convection
Author: Rémy Torro
Status: draft
Summary: A study of the Rayleigh-Benard convection phenomenon.

<br>

The Rayleigh-Bénard convection is a convection phenomenon occuring when a fluid between two horizontal plates is heated from below. The fluid organizes itself into a regular pattern known as Bénard cells, showcasing the self-organizing of a nonlinear system. 

## Dynamical equations

Fourier's equation:

$$ \frac{D T}{D t} = K \Delta T $$

$$ \rho \frac{D \vec{v}}{D t} = - \nabla p + \rho \vec{g}+ \mu \Delta \vec{v}$$

$$ \frac{D \rho}{D t} + \rho \nabla \vec{v} = 0$$

$$ \rho(T) = \rho_0 [1 - \alpha (T - T_0)]$$

where $\alpha = \frac{\partial \rho}{\partial T}|_p$, $\frac{\partial \rho}{\partial p}|_T$ is neglected. We end up with six scalar equations for six variables ($v_x,v_y,v_z,\rho,p,T$). 

$$ \frac{D \vec{v}}{D t} = -\frac{\nabla p}{\rho_0}+ \frac{\rho}{\rho_0} \vec{g} + \nu \Delta \vec{v} $$

$$ \nabla \vec{v} = 0 $$

$$ \rho(T) = \rho_0 [1 - \alpha(T - T_0)]$$

$$ \frac{D T}{D t} = \kappa \Delta T$$

# Stationary states

$D(.)/Dt = 0$, which implies that $\vec{v} = \vec{0}$. $\Delta T = 0$, $\nabla p = \rho \vec{g}$, so $\frac{\nabla p}{\rho} = \vec{g}$. 
