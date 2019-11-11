Title: Josephson effect through a quantum dot
Date: 2019-12-10 10:20
Category: Physics
Tags: Quantum Statistics
Slug: Superconductivity
Author: Rémy Torro
Status: 
Summary: Computations related to the Josephson effect through a quantum dot.
 
<br>

## Josephson effect through a quantum dot

**1) Show that $H_D$, $H_j$, $H_T$ without spinor notation correspond to the same, in spinor notation.**
 
The total Hamiltonian is written as:

$$ H = H_D + \sum_{j = L, R} H_j + H_T$$

**$H_D$ term:**

$$ H_D = \sum_\sigma \varepsilon d^\dagger_\sigma d_\sigma $$

We want to prove that this is equivalent to $H_D = \varepsilon d^\dagger \sigma_z d$, where:

$$ d = \begin{pmatrix}d_{\uparrow} & d_{\downarrow}^\dagger \end{pmatrix}^T, \qquad \sigma_z = \begin{pmatrix}1 & 0 \\
0 & -1 \end{pmatrix} $$

Let's inject this spinor into the expected spinor form of the Hamiltonian:

$$ H_D = \varepsilon \begin{pmatrix}d_{\uparrow}^\dagger & d_{\downarrow}\end{pmatrix} \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}d_{\uparrow} \\ d_{\downarrow}^\dagger \end{pmatrix} = \varepsilon (d_{\uparrow}^\dagger d_{\uparrow} - d_{\downarrow}d_{\downarrow}^\dagger) = \varepsilon (d_{\uparrow}^\dagger d_{\uparrow} + d_{\downarrow}^\dagger d_{\downarrow} -1) = \sum_\sigma \varepsilon d^\dagger_\sigma d_\sigma - \varepsilon$$

where we used the property $\{d_\sigma, d^\dagger_{\sigma'}\} = \delta_{\sigma \sigma'}$. Eventually, we can drop out the constant $\varepsilon$ term that can be thought of as a potential's zero energy that is totally adjustable, as only its derivative has physical significance ([@coleman_2015]). 

**$H_j$ term:**

The lead Hamiltonian is expressed as:

$$ H_j = \sum_{k,\sigma} \xi_k \psi_{jk\sigma}^\dagger \psi_{jk\sigma} + \Delta \sum_k (\psi_{jk\uparrow}^\dagger \psi_{jk\downarrow}^\dagger + \psi_{jk\downarrow}\psi_{jk\uparrow})$$

We want to check that this expression can be written in spinor notation as:

$$ H_j = \sum_k \psi_{jk}^\dagger (\xi_k \sigma_z + \Delta \sigma_x)\psi_{jk}$$

where 
$$\psi_{jk} = \begin{pmatrix}
\psi_{jk\uparrow} & \psi_{jk\downarrow}^\dagger\end{pmatrix}^T, \qquad \sigma_x = \begin{pmatrix}0 & 1 \\
1 & 0\end{pmatrix}$$

We can substitute the full expression for the spinor in the expression for the Hamiltonian in spinor notations: 

$$ H_j = \sum_k \begin{pmatrix}\psi_{jk\uparrow}^\dagger & \psi_{jk\downarrow}\end{pmatrix}\begin{pmatrix}\xi_k & \Delta \\
\Delta & -\xi_k \end{pmatrix}\begin{pmatrix}\psi_{jk\uparrow}\\\psi_{jk\downarrow}^\dagger\end{pmatrix} 
= \sum_k \xi_k \psi_{jk\uparrow}^\dagger \psi_{jk\uparrow} + \Delta \psi_{jk\downarrow}\psi_{jk\uparrow} + \Delta \psi_{jk\uparrow}^\dagger \psi_{jk\downarrow}^\dagger - \xi_k \psi_{jk\downarrow}\psi_{jk\downarrow}^\dagger 
= \sum_k \xi_k \left[ \psi_{jk\uparrow}^\dagger \psi_{jk\uparrow} - \psi_{jk\downarrow}\psi_{jk\downarrow}^\dagger \right] + \Delta \left[\psi_{jk\downarrow}\psi_{jk\uparrow} + \psi_{jk\uparrow}^\dagger \psi_{jk\downarrow}^\dagger \right]$$

Since $ \{\psi_{k\sigma} , \psi_{k'\sigma'}^\dagger \} = \delta_{\sigma\sigma'}\delta(k-k')$, we can write:

$$ H_j = \sum_k \xi_k \left[\psi_{jk\uparrow}^\dagger \psi_{jk\uparrow} +  \psi_{jk\downarrow}^\dagger\psi_{jk\downarrow} - 1 \right] + \Delta \left[\psi_{jk\downarrow}\psi_{jk\uparrow} + \psi_{jk\uparrow}^\dagger \psi_{jk\downarrow}^\dagger \right] = \sum_{k,\sigma} \xi_k \psi_{jk\sigma}^\dagger \psi_{jk\sigma} + \sum_k \Delta \left[\psi_{jk\downarrow}\psi_{jk\uparrow} + \psi_{jk\uparrow}^\dagger \psi_{jk\downarrow}^\dagger \right] - \sum_k \xi_k$$

Eventually, as above, we can drop the constant $\sum_k \xi_k$ term, that will not affect the Hamiltonian, in order to recover the original expression for $H_j$. 

**$H_T$ term:**

The tunnelling Hamiltonian can be expressed as:

$$ H_T = \sum_{jk\sigma} \left( T_{jk} d_\sigma^\dagger \psi_{jk\sigma}+T_{jk}^* \psi_{jk\sigma}^\dagger d_\sigma\right)$$

Assuming that $T_{jk}$ depends weakly on $k$, we want to express $H_T$ in Nambu spinor notation as:

$$ H_T = \sum_{jk} \left(\psi_{jk}^\dagger T_j d + d^\dagger T_j^\dagger \psi_{jk} \right)$$

where $T_j$ is a $2\times 2$ matrix defined as follows: 

$$T_j =\left\{
                \begin{array}{ll}
                  t_L \sigma_z e^{i \sigma_z \phi/4} \quad j = L \\
                  t_R \sigma_z e^{-i \sigma_z \phi / 4} \quad j = R \\
                \end{array}
              \right. 
$$

$t_{L / R}$ is assumed to be a real coefficient, $\phi$ is the phase difference between the superconductors. Let's replace the $L$ and $R$ indices with a $\pm$, where the upper sign corresponds to $j=L$ and the lower sign to $j=R$. We can immediately rework $T_j$ using the expression for the exponential of a Pauli matrix: $\exp(i \phi \sigma_i) = \mathbb{I}\cos{\phi}+i \sigma_i \sin{\phi}$. 

$$ T_\pm = t_\pm \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}\left[\mathbb{I}\cos{\pm \frac{\phi}{4}}+i\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}\sin{\pm \frac{\phi}{4}} \right] = t_\pm \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix} \begin{pmatrix}\cos{\frac{\phi}{4}}\pm i\sin{\frac{\phi}{4}} & 0 \\
0 & \cos{\frac{\phi}{4}}\mp i \sin{\frac{\phi}{4}}\end{pmatrix} = t_\pm \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix} \begin{pmatrix} e^{\pm i \frac{\phi}{4}} & 0 \\
0 & e^{\mp i \frac{\phi}{4}}\end{pmatrix}$$

Eventually, we have the following expression for $T_j = T_\pm$:

$$ T_j = t_j \begin{pmatrix} e^{\pm i \frac{\phi}{4}} & 0 \\
0 & -e^{\mp i \frac{\phi}{4}}\end{pmatrix}$$

We can plug this expression into the Hamiltonian in spinor notation above:

$$ H_T = \sum_{j,k} t_j \left[\begin{pmatrix}\psi_{jk\uparrow}^\dagger & \psi_{jk\downarrow}\end{pmatrix}\begin{pmatrix}e^{\pm i \frac{\phi}{4}} & 0 \\
0 & -e^{\mp i \frac{\phi}{4}}\end{pmatrix} \begin{pmatrix}d_\uparrow \\ d_{\downarrow}^\dagger \end{pmatrix} + \begin{pmatrix}d_\uparrow^\dagger & d_\downarrow \end{pmatrix}\begin{pmatrix}e^{\mp i \frac{\phi}{4}} & 0 \\
0 & -e^{\pm i \frac{\phi}{4}}\end{pmatrix}\begin{pmatrix}\psi_{jk\uparrow}\\ \psi_{jk\downarrow}^\dagger \end{pmatrix} \right] = \sum_{j,k} \left[t_j e^{\pm i\frac{\phi}{4}}\left(\psi_{jk\uparrow}^\dagger d_\uparrow - d_\downarrow \psi_{jk\downarrow}^\dagger \right) + t_j e^{\mp i \frac{\phi}{4}} \left(-\psi_{jk\downarrow}d_\downarrow^\dagger + d_\uparrow^\dagger \psi_{jk\uparrow}  \right)\right]$$

Assuming that $d_\alpha \sim \psi_{\alpha}^\dagger$, we can write: $\{d_\downarrow,\psi_{jk\downarrow}^\dagger\} = 0$, which leads to $d_\downarrow \psi_{jk\downarrow}^\dagger = - \psi_{jk\downarrow}^\dagger d_\downarrow$. Furthermore, we will call $T_{jk}^* = t_j e^{\pm i \frac{\phi}{4}}$, such that $T_{jk} = t_j e^{\mp i \frac{\phi}{4}}$. 

Eventually, we can write:

$$ H_T = \sum_{jk\sigma} \left[T_{jk}^* \left(\psi_{jk\sigma}^\dagger d_\sigma \right) + T_{jk} \left(d_\sigma^\dagger \psi_{jk\sigma} \right)\right]$$

We recover the original expression for the tunnelling Hamiltonian. 

**2) Integrating out the lead degrees of freedom, derive (using Gaussian integration), the effective action of the dot.**

We are now interested in representing the partition function $Z =\textrm{Tr} \  e^{-\beta H}$ with Grassmann variables. We expect:

$$ Z = \int \mathcal{D}(\bar{\psi}\psi)\mathcal{D}(\bar{d}d)e^{-S}$$

where $S$ is the Euclidean action and can be expanded as:

$$S = S_D + S_j + S_T = \int_0^\beta d\tau \bar{d}(\partial_\tau +\varepsilon \sigma_z) d + \int_0^\beta d\tau \left[ \sum_{jk} \bar{\psi}_{jk}(\partial_\tau + \xi_k \sigma_z +\Delta \sigma_x)\psi_{jk} \right] + \int_0^\beta d\tau \left[ \sum_{jk} \bar{\psi}_{jk} T_j d + \bar{d} T_j^\dagger \psi_{jk}\right]$$

The action has the following structure:

$$ S = \int d\tau \sum_{jk} \bar{\psi}_{jk}(\tau) M_k \psi_{jk}(\tau) + \bar{d}(\tau) N d(\tau) + \sum_{jk} \left(\bar{\psi}_{jk}(\tau) T_{jk} d(\tau) + \bar{d}(\tau) T_{jk}^\dagger \psi_{jk}(\tau) \right)$$

where $M_k = (\partial_\tau + \xi_k \sigma_z + \Delta \sigma_x)$ and $N = (\partial_\tau + \varepsilon \sigma_z)$. This is a fermionic Gaussian integral for the partition function $Z$. We want to find the $\psi$ and $\bar{\psi}$ which minimize the action $S$, in order to shift the Grassman variables $\psi(\tau) \rightarrow \psi(\tau) + \psi^c(\tau)$ and $\bar{\psi}(\tau) \rightarrow \bar{\psi}(\tau) + \bar{\psi}^c(\tau)$. 

$$ \left. \frac{\partial S}{\partial \bar{\psi}_{jk}(\tau)}\right\vert_{\psi_{jk} = \psi_{jk}^c} = M_k(\tau) \psi_{jk}^c(\tau)+T_{jk}d(\tau) = 0 $$

$$ \left. \frac{\partial S}{\partial \psi_{jk}(\tau)}\right\vert_{\bar{\psi}_{jk} = \bar{\psi}_{jk}^c} = \bar{\psi}^c_{jk}(\tau) M_k + \bar{d}(\tau) T_{jk}^\dagger = 0 $$

$M_k$ is an operator whose inverse in the Green's function of the lead:

$$ M_k(\tau) G_k (\tau,\tau') = \delta(\tau - \tau')$$

The maximum is reached when 

$$ \psi_{jk}^c(\tau) = - \int d\tau' G_k (\tau - \tau') T_{jk} d(\tau') $$

$$ \bar{\psi}_{jk}^c (\tau) = - \int d\tau' \bar{d}(\tau') T_{jk}^\dagger G_k^*(\tau, \tau')$$

We can operate the translation in the quadratic terms:

$$ \int d\tau \sum_{jk} (\bar{\psi}_{jk}+\bar{\psi}_{jk}^c) M_k (\psi_{jk}+\psi_{jk}^c) = \int d\tau \sum_{jk} \left[ \bar{\psi}_{jk} M_k \psi_{jk} + \bar{\psi}_{jk} M_k \psi_{jk}^c + \bar{\psi}_{jk}^c M_k \psi_{jk} + \bar{\psi}_{jk}^c M_k \psi_{jk}^c \right]= \int d\tau \sum_{jk} \left[\bar{\psi}_{jk} M_k \psi_{jk} - \int d\tau' \bar{\psi}_{jk}(\tau) \underbrace{M_k(\tau) G_k(\tau-\tau')}_{\delta(\tau - \tau')} T_{j,k} d(\tau') - \int d\tau' \bar{d}(\tau') T_{jk}^\dagger \underbrace{G_k^*(\tau-\tau') M_k(\tau)}_{\delta(\tau - \tau')}\psi_{jk}(\tau) + \int d\tau' \int d\tau'' \bar{d}(\tau') T_{jk}^\dagger G^*_k(\tau - \tau') \underbrace{M_k(\tau) G_k(\tau-\tau'')}_{\delta(\tau'' - \tau)}T_{jk}d(\tau'')  \right] = \int d\tau \sum_{jk} \left[\bar{\psi}_{jk} M_k \psi_{jk} - \bar{\psi}_{jk}(\tau) T_{jk} d(\tau) - \bar{d}(\tau) T_{jk}^\dagger \psi_{jk}(\tau) + \int d\tau' \bar{d}(\tau') T_{jk}^\dagger G^*_k(\tau - \tau') T_{jk} d(\tau) \right]$$

We can do the same translation in the tunnelling term:

$$\begin{align}\int d\tau \sum_{jk} \left[(\bar{\psi}_{jk}(\tau) + \bar{\psi}_{jk}^c)T_{jk}d(\tau) + d^\dagger(\tau)(\psi_{jk}(\tau) + \psi_{jk}^c(\tau)) \right] \\ = \int d\tau \sum_{jk} \left[\bar{\psi}_{jk}(\tau)T_{jk}d(\tau) + \bar{\psi}_{jk}^c(\tau) T_{jk} d(\tau) + d^\dagger(\tau)T_{jk}^\dagger \psi_{jk}(\tau) + d^\dagger(\tau)T_{jk}^\dagger \psi_{jk}^c(\tau)  \right] \\ = \int d\tau \sum_{jk} \left[\bar{\psi}_{jk}(\tau)T_{jk}d(\tau) - \int d\tau' \bar{d}(\tau')T_{jk}^\dagger G_k^*(\tau-\tau')T_{jk}d(\tau) + \bar{d}(\tau)T_{jk}^\dagger \psi_{jk}(\tau) - \int d\tau' \bar{d}(\tau) T_{jk}^\dagger G_k(\tau - \tau')T_{jk}d(\tau')  \right]\end{align}$$

$$\begin{align}S = \int d\tau \left\{\sum_{jk} \left[\bar{\psi}_{jk} M_k \psi_{jk} - \bar{\psi}_{jk}(\tau) T_{jk} d(\tau) - \bar{d}(\tau) T_{jk}^\dagger \psi_{jk}(\tau) \\ + \int d\tau' \bar{d}(\tau') T_{jk}^\dagger G^*_k(\tau - \tau') T_{jk} d(\tau) + \bar{\psi}_{jk}(\tau)T_{jk}d(\tau) \\ - \int d\tau' \bar{d}(\tau')T_{jk}^\dagger G_k^*(\tau-\tau')T_{jk}d(\tau) + \bar{d}(\tau)T_{jk}^\dagger \psi_{jk}(\tau) \\ - \int d\tau' \bar{d}(\tau) T_{jk}^\dagger G_k(\tau - \tau')T_{jk}d(\tau')  \right] + \bar{d}(\tau) N d(\tau)   \right\}\end{align} $$

$$ S = \int d\tau \left\{\sum_{jk} \left[\bar{\psi}_{jk} M_k \psi_{jk} - \int d\tau' \bar{d}(\tau) T_{jk}^\dagger G_k(\tau - \tau')T_{jk}d(\tau')  \right] + \bar{d}(\tau) N d(\tau)   \right\}$$

Now that the crossed terms $(\psi_{jk},d)$ have been cancelled, we would like to perform the integration of $Z$ on the superconducting degrees of freedon $(\bar{\psi},\psi)$. 

$$Z_S = \int \mathcal{D}(\bar{\psi}\psi)\mathcal{D}(\bar{d}d)e^{-\int d\tau \sum_{jk} \bar{\psi}_{jk}M_k\psi_{jk}}$$

$M_k$ is some Hermitian differential operator with orthonormal eigenstates $\chi_{kn}$ and eigenvalues $\lambda_{kn}$:

$$ M_k \chi_{kn} = \lambda_{kn}\chi_{kn}$$

We can expand $\psi$ and $\bar{\psi}$ in terms of these eigenstates:

$$ \psi(\tau) = \sum_n c_n \chi_{n}(\tau) \qquad \bar{\psi}(\tau) = \sum_n \bar{c}_n \chi^\dagger_n(\tau)$$

$$
Z_S = \int \prod_{j,k}\prod_n d\bar{c}_n dc_n e^{-\sum_{m,n} \lambda_n \bar{c}_m c_n \int d\tau \chi_m^\dagger(\tau)\chi_n(\tau)}
\\ = \int \prod_{j,k,n} d\bar{c}_n dc_n e^{-\sum_n \lambda_n \bar{c}_n c_n}
\\ = \int \prod_{j,k,n} d\bar{c}_n dc_n \prod_n (1 - \lambda_n \bar{c}_n c_n)
\\ = \prod_{j,k,n} \lambda_n = \det M $$

We are left with:

$$Z = Z_S \int \mathcal{D}(\bar{d}d)e^{-\int d\tau \bar{d}(\tau)N d(\tau) + \int d\tau \int d\tau' \bar{d}(\tau)\sum_{jk}T_{jk}^\dagger G_k(\tau - \tau') T_{jk} d(\tau')}$$

We can introduce $\sum (\tau - \tau') = \sum_{jk} T_{jk}^\dagger G_k(\tau - \tau') T_{jk}$, the self energy due to the leads. 

$$Z = Z_S \int \mathcal{D}(\bar{d}d)e^{-\int d\tau \bar{d}(\tau)(\partial_\tau - \varepsilon \sigma_z) d(\tau) + \int d\tau \int d\tau' \bar{d}(\tau)\sum(\tau - \tau') d(\tau')}$$

**3) Using Matsubara representation, derive the self energy of the dot**

The Green's function of the leads satisfies the differential equation:

$$M_k G_k(\tau,\tau') = \delta(\tau-\tau')$$

$$(\partial_\tau + \xi_k \sigma_z + \Delta \sigma_x) G_k(\tau,\tau') = \delta(\tau - \tau')$$

it is noted as 

$$ G_L(\tau) = (\partial_\tau + \xi_k \sigma_z + \Delta \sigma_x)^{-1} \delta(\tau)$$

We now have a quadratic effective action in terms of the dot degrees of freedom. We will use the Matsubara representation (Fourier series for the dot fields, with antiperiodic boundary conditions). 

$$ \delta(\tau) = \frac{1}{\beta} \sum_{\omega_n} e^{-i\omega_n \tau} \qquad \omega_n = \frac{2\pi}{\beta}\left(n+\frac{1}{2}\right) $$

The Matsubara representation of the Green's function is then obtained as:

$$ G(\tau) = \frac{1}{\beta} \sum_{\omega_n} e^{-i\omega_n \tau} G_{\omega_n}$$

$$ G_{\omega_n} = \sum_k \left(-i\omega_n + \xi_k \sigma_z + \Delta \sigma_x  \right)^{-1} \\ = \sum_k \underbrace{\begin{pmatrix}-i\omega_n + \xi_k & \Delta \\ \Delta & -i\omega_n -\xi_k \end{pmatrix}}_{M}^{-1}$$

We can compute the inverse of this matrix, assuming that it is invertible *i.e.* $\det{M}\neq 0$. 

$$ M^{-1} = \frac{1}{\det{M}} C^T$$

where $C^T$ is the transpose of the cofactor matrix of $M$. 

$$\det{M} = (-i\omega_n + \xi_k)(-i\omega_n - \xi_k)-\Delta^2 = -(\omega_n^2 + \xi_k^2 + \Delta^2)$$

$$ M^{-1} = \frac{-1}{\omega_n^2 + \xi_k^2 + \Delta^2} \begin{pmatrix}-i\omega_n - \xi_k & -\Delta \\ -\Delta & -i\omega_n + \xi_k \end{pmatrix} = \frac{1}{\omega_n^2 + \xi_k^2 + \Delta^2} \begin{pmatrix}i\omega_n + \xi_k & \Delta \\ \Delta & i\omega_n - \xi_k \end{pmatrix} \\ = \frac{i\omega_n \sigma_0 + \xi_k \sigma_z + \Delta \sigma_x}{\omega_n^2 + \xi_k^2 + \Delta^2}$$

In the continuum limit, $\sum_k \rightarrow \int d\xi \nu(\xi) \sim \int d\xi \nu(0)$. We can perform the integration separately for each term in the numerator, using the property $\int d\xi (\xi^2 + b^2)^{-1} = \pi/b$. 

$$ i \omega_n \sigma_0 \int d\xi \nu(0) \frac{1}{(\omega_n^2 + \Delta^2)+\xi^2} = i\omega_n \sigma_0 \nu(0) \frac{\pi}{\sqrt{\omega_n^2 + \Delta^2}} $$

$$ \sigma_z \int_{-\infty}^{\infty} d\xi \nu(0) \underbrace{\frac{\xi}{(\omega_n^2 + \Delta^2)+\xi^2}}_{\textrm{odd function}} = 0$$

$$ \Delta \sigma_x \int d\xi \nu(0) \frac{1}{(\omega_n^2 + \Delta^2)+\xi^2} = \Delta \sigma_x \nu(0) \frac{\pi}{\sqrt{\omega_n^2 + \Delta^2}} $$

So we can write:

$$ G_{\omega_n} = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}}(i\omega_n \sigma_0 + \Delta \sigma_x)$$

We can now derive the self-energy, using $G_{\omega_n}$ and the previously defined $T_j$ matrix:

$$ \sum(\omega_n) = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}}\sum_{j=L,R} T_j^\dagger G_{\omega_n} T_j
\\ = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}} \sum_{j=L,R} t_j^2 \begin{pmatrix}e^{\mp i \phi/4} & 0 \\ 0 & -e^{\pm i \phi/4} \end{pmatrix}\begin{pmatrix}i\omega_n & \Delta \\ \Delta & i\omega_n \end{pmatrix}\begin{pmatrix}e^{\pm i \phi/4} & 0 \\ 0 & -e^{\mp i \phi/4}\end{pmatrix} \\ = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}} \sum_{j=L,R} t_j^2 \begin{pmatrix}i\omega_n & -\Delta e^{\mp i \phi/2} \\ -\Delta e^{\pm i \phi/2} & i\omega_n \end{pmatrix} \\ = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}} \left\{ t_L^2 \underbrace{\begin{pmatrix}i\omega_n & -\Delta[\cos(\phi/2) - i \sin(\phi/2)] \\ -\Delta[\cos(\phi/2)+i\sin(\phi/2)] & i\omega_n \end{pmatrix}}_{i\omega_n \sigma_0 - \Delta \cos(\phi/2)\sigma_x - \Delta \sin(\phi/2)\sigma_y} + t_R^2 \underbrace{\begin{pmatrix}i\omega_n & -\Delta[\cos(\phi/2) + i \sin(\phi/2)] \\ -\Delta[\cos(\phi/2)-i\sin(\phi/2)] & i\omega_n \end{pmatrix}}_{i\omega_n \sigma_0 -\Delta \cos(\phi/2)\sigma_x + \Delta \sin(\phi/2) \sigma_y}\right\} \\ = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}} \left\{(t_L^2 + t_R^2)[i\omega_n\sigma_0 - \Delta \cos(\phi/2)\sigma_x] - \Delta\sin(\phi/2) \sigma_y (t_L^2 - t_R^2)\right\} \\ = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}}  (t_L^2 + t_R^2)\left[i\omega_n\sigma_0 - \Delta \cos(\phi/2)\sigma_x - \frac{t_L^2 - t_R^2}{t_L^2 + t_R^2} \Delta\sin(\phi/2) \sigma_y \right] \\ = \frac{\pi \nu(0)}{\sqrt{\omega_n^2 + \Delta^2}}  (t_L^2 + t_R^2)\left[i\omega_n\sigma_0 - \Delta \cos(\phi/2)\sigma_x - \gamma \Delta\sin(\phi/2) \sigma_y \right] $$

where $\gamma = (t_L^2 - t_R^2)/(t_L^2 + t_R^2)$. As a result, the self energy of the dot can be expressed as:

$$ \Sigma_{\omega_n} = \frac{\pi \nu(0) (t_L^2 + t_R^2)}{\sqrt{\omega_n^2 + \Delta^2}} \left[i\omega_n\sigma_0 - \Delta \cos(\phi/2)\sigma_x - \gamma \Delta\sin(\phi/2) \sigma_y \right] $$

$$ \Sigma_{\omega_n} = \frac{\Gamma / 2}{\sqrt{\Delta^2 - (i\omega_n)^2}} \left[i\omega_n\sigma_0 - \Delta \cos(\phi/2)\sigma_x - \gamma \Delta\sin(\phi/2) \sigma_y \right] $$

where we introduced $\Gamma = 2\pi \nu(0) (t_L^2 + t_R^2)$. 

**4) Compute the fermionic determinant for a given Matsubara frequency**

Now we integrate out the dot degrees of freedom:

$$Z = \int \mathcal{D}(\bar{d}d)e^{-S_{\textrm{eff}}} \\ = \int \mathcal{D}(\bar{d}d) e^{-\int_0^\beta d\tau \bar{d}(\tau)(\partial_\tau + \varepsilon \sigma_z)d(\tau)} e^{-\int_0^\beta d\tau \int_0^\beta d\tau' \bar{d}(\tau) \Sigma (\tau - \tau') d(\tau')} \\ = \int \mathcal{D}(\bar{d}d)e^{-\sum_{\omega_n} \bar{d}_{\omega_n} M_{\omega_n} d_{\omega_n}} \\ = \prod_{\omega_n} \det M_{\omega_n} $$

with $M_{\omega_n} = -i\omega_n +\varepsilon \sigma_z - \Sigma_{\omega_n}$. Since

$$ J = -\frac{2}{\beta} \frac{\partial}{\partial \phi} \ln Z \\ = -\frac{2}{\beta} \frac{\partial}{\partial \phi} \sum_{\omega_n} \ln \det M_{\omega_n}$$

We will start by expressing $M_{\omega_n}$ in matrix notation:

$$M_{\omega_n} = \begin{pmatrix}-i\omega_n + \varepsilon & 0 \\ 0  & -i\omega_n -\varepsilon \end{pmatrix} - \frac{\Gamma / 2}{\sqrt{\Delta^2 -(i\omega)^2}}\begin{pmatrix}i\omega_n & -\Delta \cos{\phi/2} + i \gamma \Delta \sin{\phi/2} \\ -\Delta \cos{\phi/2} - i \gamma \Delta \sin{\phi/2} & i\omega_n \end{pmatrix} = \begin{pmatrix}\frac{(-i\omega_n + \varepsilon)\sqrt{\Delta^2 -(i\omega_n)^2} - \Gamma/2 i \omega_n}{\sqrt{\Delta^2 -(i\omega_n)^2}} & \frac{-\Gamma / 2 (-\Delta \cos{\phi/2} + i \gamma \Delta \sin{\phi/2})}{\sqrt{\Delta^2 -(i\omega_n)^2}} \\ \frac{-\Gamma / 2 (-\Delta \cos{\phi/2} - i \gamma \Delta \sin{\phi/2})}{\sqrt{\Delta^2 -(i\omega_n)^2}} & \frac{(-i\omega_n - \varepsilon)\sqrt{\Delta^2 -(i\omega_n)^2} - \Gamma / 2 i\omega_n}{\sqrt{\Delta^2 -(i\omega_n)^2}} \end{pmatrix} $$

$$\det M_{\omega_n} = \underbrace{(-i\omega_n + \varepsilon)(-i\omega_n - \varepsilon)}_{(a+b)(a-b) = a^2 - b^2} - \frac{\Gamma / 2 i \omega_n \left[(-i\omega_n + \varepsilon) + (-i\omega_n - \varepsilon)\right]}{\sqrt{\Delta^2 -(i\omega_n)^2}} + \frac{(\Gamma / 2)^2 (i\omega)^2}{\Delta^2 -(i\omega)^2} - \frac{(\Gamma / 2)^2}{\Delta^2 -(i\omega_n)^2}\underbrace{(-\Delta \cos{\phi/2}+i\gamma\Delta\sin{\phi/2})(-\Delta \cos{\phi/2}-i\gamma \Delta \sin{\phi/2})}_{zz^* = |z|^2} \\ = (i\omega_n)^2 - \varepsilon^2 + \frac{(i\omega_n)^2 \Gamma}{\sqrt{\Delta^2 -(i\omega_n)^2}}+ \frac{(\Gamma / 2)^2 (i\omega)^2}{\Delta^2 -(i\omega)^2}- \frac{(\Gamma / 2)^2}{\Delta^2 -(i\omega_n)^2}\left[\Delta^2 \cos^2{\phi/2} + \gamma^2 \Delta^2 \sin^2{\phi/2} \right] \\ = - \varepsilon^2 + (i\omega_n)^2 \underbrace{\left[1 + \frac{\Gamma}{\sqrt{\Delta^2 -(i\omega_n)^2}}+ \frac{(\Gamma / 2)^2 }{\Delta^2 -(i\omega)^2}\right]}_{= \left[1 + (\Gamma/2)/(\sqrt{\Delta^2+(i\omega_n)^2})\right]^2} - \frac{(\Gamma / 2)^2}{\Delta^2 -(i\omega_n)^2}\left[\Delta^2 \cos^2{\phi/2} + \gamma^2 \Delta^2 \sin^2{\phi/2} \right] $$

$$ \det M_{\omega_n} = (i\omega_n)^2 \left[1 + \frac{\Gamma/2}{\sqrt{\Delta^2+(i\omega_n)^2}}\right]^2 - \varepsilon^2 -  \frac{(\Gamma / 2)^2 \Delta^2}{\Delta^2 -(i\omega_n)^2}\left[\cos^2{\phi/2} + \gamma^2 \sin^2{\phi/2} \right]$$

Eventually, the Josephson current can be written as:

$$ J = -\frac{2}{\beta} \frac{\partial }{\partial \phi} \sum_{\omega_n} \ln \left\{(i\omega_n)^2 \left[1 + \frac{\Gamma/2}{\sqrt{\Delta^2+(i\omega_n)^2}}\right]^2 - \varepsilon^2 -  \frac{(\Gamma / 2)^2 \Delta^2}{\Delta^2 -(i\omega_n)^2}\left[\cos^2{\phi/2} + \gamma^2 \sin^2{\phi/2} \right]\right\}$$
**5) Derive the equation for the Andreev levels, and find the approximate solution for $Z$**

*a) in the tunnel regime $\Gamma, \varepsilon << \Delta$ (quartic equation) (throwing away the solution which is not consisent with this assumption ($Z << \Delta$)*

*b) in the high transparency regime $\Gamma >> \Delta$*


