Title: Thermodynamic properties using the Bogoliubov Valatin method
Date: 2019-11-28 11:20
Category: Physics
Tags: Quantum physics, Superconductivity
Slug: homework
Author: Rémy Torro
Summary: Derivation of thermodynamic quantities in the Bogoliubov Valatin formalism.
 
<br>

## Bogoliubov- Valatin (calculated steps of Ch 28 of Ketterson)
As discussed in the previous section, excited states are easily epxressed using the Bogoliubov-Valatin operators. We can also rewrite the reduced Hamiltonian of the system in terms of the Bogoliubov quasiparticle operators. In doing so, we generate two types of terms: those containing products of an equal number of creation $\hat{\gamma}^\dagger_{k\sigma}$ and destruction $\hat{\gamma}_{k\sigma}$ operators and those containing an unequal number. When taking thermally averaged quantum-expectation values of such products, only the first forms yield nonzero averages. 

**1) Write the full Hamiltonian in term of $\gamma$, $\gamma^\dagger$.**

$$ \hat{H}'_R = \hat{H}'_0 + \hat{H}_{IR} \\ = \sum_k \xi_k [2 v_k^2 + (u_k^2 - v_k^2)(\gamma^\dagger_{k\uparrow}\gamma_{k\uparrow}+\gamma^\dagger_{-k\downarrow}\gamma_{-k\downarrow})] + \sum_{k,k'} V_{k k'}[u_k v_k u_{k'}v_{k'}(1 - \gamma^\dagger_{k\uparrow}\gamma_{k\uparrow}-\gamma^\dagger_{-k\downarrow}\gamma_{-k\downarrow})(1 - \gamma^\dagger_{k'\uparrow}\gamma_{k'\uparrow}-\gamma^\dagger_{-k'\downarrow}\gamma_{-k'\downarrow})+ \textrm{terms with unequal numbers of $\gamma^\dagger_{k\sigma}$ and $\gamma_{k\sigma}$}$$

where we had individually 

$$ \hat{H}'_0 = \sum_k \xi_k [2 v_k^2 + (u_k^2 - v_k^2)(\gamma^\dagger_{k\uparrow}\gamma_{k\uparrow}+\gamma^\dagger_{-k\downarrow}\gamma_{-k\downarrow})] + \text{terms with unequal number of $\gamma^\dagger_{k\sigma}$ and $\gamma_{k\sigma}$} $$

and 

$$ \hat{H}_{IR}' = \sum_{k,k'} V_{k k'}[u_k v_k u_{k'}v_{k'}(1 - \gamma^\dagger_{k\uparrow}\gamma_{k\uparrow}-\gamma^\dagger_{-k\downarrow}\gamma_{-k\downarrow})(1 - \gamma^\dagger_{k'\uparrow}\gamma_{k'\uparrow}-\gamma^\dagger_{-k'\downarrow}\gamma_{-k'\downarrow})+ \textrm{terms with unequal numbers of $\gamma^\dagger_{k\sigma}$ and $\gamma_{k\sigma}$}$$



**2) Use Wick theorem to compute thermal averages.**

Firstly, let's compute the thermal average of $\hat{H}_0'$:

$$ \langle \hat{H}_0' \rangle = \sum_k \xi_k [2 v_k^2 + (u_k^2 - v_k^2)(\langle \gamma_{k\uparrow}^\dagger \gamma_{k\uparrow}\rangle + \langle \gamma_{-k\downarrow}^\dagger \gamma_{-k'\downarrow}\rangle)]$$

Since the fermion-quasiparticle excitations do not interact (in our mean-field-like theory), the averages are given by $\langle \gamma^\dagger_{k\sigma}\gamma_{k\sigma} \rangle = f_{k\sigma}$. Let's assume that $2 f_k = f_{k\uparrow}+f_{-k\downarrow}$. As a result:

$$ \langle \hat{H}_0' \rangle = \sum_k \xi_k [2 v_k^2 + (u_k^2 - v_k^2)2 f_k] = 2 \sum_k \xi_k [v_k^2 + (u_k^2 - v_k^2)f_k]$$

Now we have to deal with the thermal average of $\hat{H}_{IR}'$. The parentheses in equation ... can be developped as: $I = 1 - \gamma_{k'\uparrow}^\dagger \gamma_{k'\uparrow} - \gamma_{-k'\downarrow}^\dagger \gamma_{-k'\downarrow} - \gamma_{k\uparrow}^\dagger \gamma_{k\uparrow} + \gamma_{k\uparrow}^\dagger\gamma_{k\uparrow}\gamma_{k'\uparrow}^\dagger\gamma_{k'\uparrow} + \gamma_{k\uparrow}^\dagger\gamma_{k\uparrow}\gamma_{-k'\downarrow}^\dagger\gamma_{-k'\downarrow} - \gamma_{-k\downarrow}^\dagger\gamma_{-k\downarrow}+\gamma_{-k\downarrow}^\dagger\gamma_{-k\downarrow}\gamma_{k'\uparrow}^\dagger\gamma_{k'\uparrow}+\gamma_{-k\downarrow}^\dagger\gamma_{-k\downarrow}\gamma_{-k'\downarrow}^\dagger\gamma_{-k'\downarrow}$

The thermal average of couples of fermionic operators is computed using $\langle \gamma^\dagger_{k\sigma}\gamma_{k\sigma} \rangle = f_{k\sigma}$. For quartets of fermionic operators, we can apply Wick's theorem. Let's compute the average for the first of these quartets:

$$\langle \gamma_{k\uparrow}^\dagger \gamma_{k\uparrow}\gamma_{k'\uparrow}^\dagger\gamma_{k'\uparrow} \rangle = \langle  \gamma_{k\uparrow}^\dagger \gamma_{k\uparrow} \rangle\langle \gamma_{k'\uparrow}^\dagger \gamma_{k'\uparrow} \rangle 
- \langle \gamma_{k\uparrow}^\dagger\gamma_{k'\uparrow}^\dagger \rangle \langle \gamma_{k\uparrow}\gamma_{k'\uparrow}\rangle 
+ \langle \gamma_{k\uparrow}^\dagger \gamma_{k'\uparrow}\rangle \langle \gamma_{k\uparrow}\gamma_{k'\uparrow}^\dagger \rangle
\\ = f_{k\uparrow}f_{k'\uparrow} - 0 + 0 $$

We can proceed in the same fashion for each term and get:

$$\langle I \rangle = 1 -f_{k'\uparrow} -f_{-k'\downarrow} - f_{k\uparrow} - f_{k\downarrow} + f_{k\uparrow}f_{k'\uparrow} + f_{k\uparrow}f_{-k'\downarrow}+f_{-k\downarrow}f_{k'\uparrow}+f_{-k\downarrow}f_{-k'\downarrow}$$

Assuming that $f_k f_{k'} = \frac{1}{4}(f_{k\uparrow}+f_{-k\downarrow})(f_{k'\uparrow}f_{-k'\downarrow})$, we recognize that we have $\langle I \rangle = 1 - 2f_{k'}-2f_k + 4f_kf_{k'}$.

Eventually:

$$\langle \hat{H}_{IR}' \rangle = \sum_{k,k'} V_{kk'} u_k v_k u_{k'}v_{k'}(1-2f_k)(1-2f_{k'})$$

Gathering all the terms, we can write:

$$\langle \hat{H}_R' \rangle = 2\sum_k \xi_k[v_k^2 + (u_k^2 - v_k^2)f_k] + \sum_{k,k'} V_{kk'}u_k v_k u_{k'}v_{k'}(1-2f_k)(1-2f_{k'})$$


**3) Use microcanonical argument to find the entropy.**


There can be no more than one particle in each quantum state. The number of possible ways of distributing $N_j$ identical particles among $G_j$ states with no more than one particle in each is the number of ways of selecting $N_j$ of the $G_j$ states:

$$ \Delta \Gamma_j = \frac{G_j !}{N_j!(G_j - N_j)!}$$

If we take the logarithm of this quantity and apply Stirling's approximation, we can write the following ``microcanonical'' entropy:

$$S = \ln \prod_j \Delta \Gamma_j \\ = \sum_j \ln \frac{G_j !}{N_j!(G_j - N_j)!} = \sum_j \left\{G_j \ln G_j - N_j \ln N_j -(G_j - N_j)\ln(G_j - N_j)-G_j + N_j + (G_j - N_j)  \right\} \\ = \sum_j \left\{G_j \ln G_j - N_j \ln N_j -(G_j - N_j)\ln(G_j - N_j) \right\}$$

Using the mean occupation numbers of the quantum states $n_j = N_j / G_j$, we can rewrite the above expression as:

$$S = \sum_j \left\{G_j \ln G_j - G_j n_j \ln(G_j n_j) -(G_j - G_j n_j)\ln(G_j - G_j n_j) \right\} \\ = \sum_j G_j \left\{\ln G_j - n_j \ln(G_j n_j) -(1 - n_j)\ln[G_j(1-n_j)] \right\} \\ = \sum_j G_j \left\{\ln G_j - n_j \ln G_j - n_j \ln n_j -(1 - n_j)\ln G_j - (1 -n_j)\ln(1 - n_j) \right\} \\ = -\sum_j G_j \left\{n_j \ln n_j + (1 -n_j)\ln(1 - n_j) \right\} $$

The distribution $n_j$ that maximises this entropy is the usual equilibrium Fermi-Dirac distribution $n_j = f_j$. For electrons, we can set the degeneracy $G_j = 2$. If we introduce $k_B$ to get the right units;

$$S = -2 k_B \sum_k \left\{f_k \ln f_k + (1 -f_k)\ln(1 - f_k) \right\} $$


The Helmholtz free energy in the pairing approximation is given by

$$ F = \langle H_R \rangle - TS $$

where the entropy for fermions is given by the usual expression from statistical mechanis 

$$ S = -k_B \sum_{k,\sigma} [f_k \ln f_k + (1-f_k)\ln(1-f_k)] \\ = -2k_B \sum_k [f_k \ln f_k + (1-f_k)\ln(1-f_k)]$$


**4) Find the gap self-consistent equation. For gap 28.12, solve with Cooper.**

We can introduce $u_k = \cos \theta_k$ and $v_k = \sin \theta_k$ and minimize $F$ with respect to $\theta_k$ ($\partial F / \partial \theta_k = 0$. Since the $-TS$ term in $F$ does not depend on $\theta_k$ we can directly perform:

$$\frac{\partial \langle H_R' \rangle }{\partial \theta_k} = 2\xi_k [2\cos \theta_k \sin \theta_k - 4 \cos \theta_k \sin \theta_k f_k] + 2 \underbrace{\sum_{k'} V_{kk'}(1-2 f_{k'})\cos \theta_{k'}\sin \theta_{k'}}_{-\Delta_k}(\cos^2 \theta_k - \sin^2 \theta_k)(1-2 f_k)  \\ = 4 \xi_k u_k v_k (1-2f_k) - 2 \Delta_k (u_k^2 - v_k^2)(1-2f_k) = 0$$

where we introduced $\Delta_k = -\sum_{k'} V_{kk'}u_{k'}v_{k'}(1 - 2f_{k'})$. Using the property $u_k^2 + v_k^2 = 1$, we can write $v_k^2 = 1-u_k^2$ and substitute:

$$ 2\xi_k u \sqrt{1 - u^2} = \Delta_k (2 u^2 -1)$$

$$ 4 \xi_k^2 u^2 (1 - u^2) = \Delta_k^2 [4u^4 - 4u^2 +1]$$

$$ u^4 - u^2 + \frac{\Delta_k^2}{4(\xi_k^2 + \Delta_k^2)} = 0$$

We can compute the discriminant $\Delta$:

$$ \Delta = 1 - \frac{\Delta_k^2}{\xi_k^2 + \Delta_k^2} = \frac{\xi_k^2}{\xi_k^2 + \Delta_k^2}$$

This gives us the following solutions for $u^2$:

$$ u^2 = \frac{1}{2}\left(1 \pm \sqrt{\frac{\xi_k^2}{\xi_k^2 + \Delta_k^2}}\right) = \frac{1}{2}\left(1 \pm \frac{\xi_k}{\epsilon}\right)$$

where we introduced $\epsilon = \sqrt{\xi_k^2 + \Delta_k^2}$. If we substitute $u_k^2 = 1 - v_k^2$ we find:

$$ v_k^2 = \frac{1}{2}\left(1 \pm \frac{\xi_k}{\epsilon_k}\right)$$

We can select the upper sign for $u_k$ and the lower sign for $v_k$ in order to satisfy $u_k^2 + v_k^2 = 1$. 

Using $f_{k'} = 1/(e^{\epsilon_{k'}/k_B T}+1)$, we can rewrite $(1-2f_{k'})$ in $\Delta_k$ as:

$$ (1-2 f_{k'}) = 1 - \frac{2}{e^{\epsilon_{k'}/k_BT}+1} = \frac{e^{\epsilon_{k'}/k_B T}+1 - 2}{e^{\epsilon_{k'}/k_B T}+ 1} = \frac{e^{\epsilon_{k'}/k_B T}-1}{e^{\epsilon_{k'}/k_B T}+1} = \tanh \left(\frac{\epsilon_{k'}}{2 k_B T} \right)$$

And as a result:

$$ \Delta_k = \sum_{k'} V_{kk'} u_{k'}v_{k'}\tanh \left(\frac{\epsilon_{k'}}{2 k_B T} \right)$$

Using the expressions for $u_k$ and $v_k$ we may rewrite the gap equation as:

$$ \Delta_k = -\sum_{k'}V_{kk'} \sqrt{\frac{1}{2}\left(1+\frac{\xi_{k'}}{\epsilon_{k'}}\right)\frac{1}{2}\left(1-\frac{\xi_{k'}}{\epsilon_{k'}}\right)}(1 - 2 f_{k'}) \\ = -\sum_{k'}V_{kk'} \sqrt{\frac{1}{4}\left(1-\frac{\xi_{k'}^2}{\xi_{k'}^2 + \Delta_{k'}^2}\right)}(1 - 2 f_{k'}) \\ = -\sum_{k'}V_{kk'} \frac{1}{2}\frac{\Delta_{k'}}{\sqrt{\xi_k^2 + \Delta_k^2}}(1 - 2 f_{k'}) \\ = - \sum_{k'} V_{kk'}\frac{(1 - 2 f_{k'})}{2\epsilon_{k'}}\Delta_{k'} $$

**5) Find the critical temperature.**

If we consider the following gap function in the Cooper model:

$$V_{kk'}=\left\{
                \begin{array}{ll}
                  -V \quad \textrm{for} \ |\xi_k| \ \textrm{and} \ |\xi_{k'}|\leq \hbar \omega_{D} \\
                  0 \quad \textrm{for} \ |\xi_k| \ \textrm{or} \ |\xi_{k'}| > \hbar \omega_D 
                \end{array}
              \right.
$$

We can rewrite the last equation for $\Delta_k$ in integral form as:

$$\Delta \sim \mathcal{N}(0) V \Delta \int_{-\hbar \omega_D}^{\hbar \omega_D} d\xi \frac{1 - 2 f[\epsilon]}{2\epsilon}$$

$$ 1 = \mathcal{N}(0) V \int_{-\hbar \omega_D }^{\hbar \omega_D} d\xi \frac{1 - 2 f[\sqrt{\xi^2 + \Delta^2(T)}]}{2\sqrt{\xi^2 + \Delta^2(T)}}$$

The critical temperature $T_c$ corresponds to $\Delta(T_c) = 0$:

$$ 1 = \mathcal{N}(0) V \int_{-\hbar \omega_D }^{\hbar \omega_D} d\xi \frac{1 - 2 f[\xi,T_c]}{2\xi} = \mathcal{N}(0) V \int_{-\hbar\omega_D}^{\hbar \omega_D} \frac{d\xi}{2\xi} \tanh\left(\frac{\xi}{2k_B T_c}\right) = \mathcal{N}(0) V \int_0^{\hbar \omega_D} \frac{d\xi}{\xi} \tanh\left(\frac{\xi}{2k_B T_c}\right) $$

where I split the integral because the integrand $\tanh(\xi)/\xi$ was even. Since:

$$ \lim_{\xi \rightarrow \infty} \tanh\left(\frac{\xi}{2k_B T}\right) = 1$$ 

and the integral has the asymptotic form $\ln (\hbar \omega_D/k_B T_c) + C$; a numerical computation yields $C = \ln 1.14$.




**6) Compute the Free energy.**

We can express the entropy in a more convenient form as:

$$ - TS = \sum_k \left[\varepsilon_k (1 - 2 f_k) - 2 k_B T \ln \left(2 \cosh \frac{\varepsilon_k}{2 k_B T}\right) \right]$$

**Proof**: let's develop this expression using $\cosh x = \frac{e^x + e^{-x}}{2}$:

$$ - TS = \sum_k \varepsilon_k (1 - 2 f_k) - 2 k_B T \ln [e^{\frac{\varepsilon_k}{2 k_B T}}+e^{-\frac{\varepsilon_k}{2 k_B T}}]$$

The logarithm can be rewritten as: $\ln [e^{-\frac{\varepsilon_k}{2 k_B T}}(1+e^{\frac{\varepsilon_k}{k_B T}})] = -\frac{\varepsilon_k}{2 k_B T} - \ln f_k$. As a result:

$$ -TS = \sum_k \left[\varepsilon_k (1 - 2 f_k) + \varepsilon_k + 2 k_B T \ln f_k \right]$$

We will now try to derive this expression starting from equation ... that we derived in question 3. 

$$ - TS = 2 k_B T \sum_k \left\{f_k \ln f_k + (1 - f_k)\ln(1 - f_k) \right\} \\ = 2k_B T \sum_k \left\{\frac{\varepsilon_k}{k_B T} + \ln f_k - \frac{\varepsilon_k}{k_B T}f_k \right\} \\ = \sum_k \left[2 \varepsilon_k + 2 k_B T \ln f_k - 2 \varepsilon_k f_k \right] \\ = \sum_k \left[\varepsilon_k (1 - 2 f_k) + \varepsilon_k + 2 k_B T \ln f_k \right]$$

Both expressions are thus equivalent. Now, we would like to compute $\langle \hat{H}_{IR} \rangle$. We already computed it in question 1. We want to show that it can be written as:

$$ \langle \hat{H}_{IR} \rangle = - \sum_k \frac{\Delta_k^2}{2\varepsilon_k}(1 - 2 f_k)$$

Starting from equation ... and substituting the expressions for $u_k$ and $v_k$ derived in ... :

$$ \langle \hat{H}_{IR} \rangle = \sum_{k,k'} V_{k,k'} u_k v_k u_{k'}v_{k'}(1 - 2 f_k)(1-2 f_{k'}) \\ = -\sum_k \Delta_k u_k v_k (1-2 f_k) \\ = -\sum_{k} \Delta_k (1 - 2 f_k)\frac{1}{2}\underbrace{\sqrt{1 - \frac{\xi_k^2}{\varepsilon_k^2}}}_{\Delta_k / \varepsilon_k} \\ = -\sum_k \frac{\Delta_k^2}{2\varepsilon_k}(1 - 2 f_k) \\ = -\frac{\Delta^2(T)}{V}$$

where in the last line we introduced a new notation following Ketterson. In the same way, we can compute $\langle \hat{H}_0'\rangle$:

$$ \langle \hat{H}_0' \rangle = 2 \sum_k \xi_k \left[v_k^2 + (u_k^2 - v_k^2)f_k \right] \\ = 2\sum_k \left[\xi_k v_k^2 + \frac{\xi_k^2}{\varepsilon_k}f_k \right] \\ = 2 \sum_k \left[\xi_k v_k^2 + \left(\varepsilon_k - \frac{\Delta_k^2}{\varepsilon_k}\right) f_k\right]$$

Indeed: $\varepsilon_k - \frac{\Delta_k^2}{\varepsilon_k} = \frac{\varepsilon_k^2 - \Delta_k^2}{\varepsilon_k} = \frac{\xi_k^2}{\varepsilon_k}$.The energy $E' = \langle \hat{H}_R' \rangle = \langle \hat{H}_0' \rangle + \langle \hat{H}_{IR}' \rangle$ can be written as:

$$E' = 2 \sum_k \left[\xi_k v_k^2 + f_k \varepsilon_k - \frac{\Delta^2}{2 \varepsilon_k} \right] - \frac{\Delta^2}{V} $$ 
 
Eventually, one can write the free energy as:

$$ F = E' - TS \\ = 2 \sum_k \left[\xi_k v_k^2 + f_k \varepsilon_k - \frac{\Delta^2}{2\varepsilon_k} \right] - \frac{\Delta^2}{V} + \sum_k \left[\varepsilon_k (1 - 2 f_k) - 2 k_B T \ln \left(2 \cosh \frac{\varepsilon_k}{2 k_B T}\right) \right] \\ = \sum_k \left[2\xi_k v_k^2 - \frac{\Delta^2}{\varepsilon_k} + \varepsilon_k - 2 k_B T \ln \left(2 \cosh \frac{\varepsilon_k}{2 k_B T}\right)\right]-\frac{\Delta^2(T)}{V}$$

This is the Free energy of the system.

**7) Find the low temperature behavior of specific heat (! $\varepsilon_k$ in Ketterson is $E_k$ in my notes.**

The specific heat is defined as:

$$ C = T \frac{d S}{d T}$$

Using expression ... for the entropy, and since only $f_k$ depends on $T$, we can perform the derivative:

$$ \frac{dS}{dT} = -2 k_B \sum_k \left[\frac{\partial f_k}{\partial T} \ln f_k + \frac{\partial f_k}{\partial T} - \frac{\partial f_k}{\partial T} \ln(1 - f_k) - \frac{\partial f_k}{\partial T} \right] \\ = - 2 k_B \sum_k \left[\ln f_k - \ln(1 - f_k) \right]\frac{\partial f_k}{\partial T}$$

As a result:

$$ C = T \frac{dS}{dT} \\ = -2 k_B T \sum_k \left[\ln f_k - \ln(1-f_k) \right]\frac{\partial f_k}{\partial T}$$

Notice that $\ln f_k - \ln(1-f_k) = -\ln(1+e^{\varepsilon_k/k_B T}) - \ln \left(\frac{e^{\varepsilon_k/k_B T}}{e^{\varepsilon_k/k_B T}+1} \right) = -\frac{\varepsilon_k}{k_B T}$. Thus, we can write:

$$C = 2 k_B T \sum_k \frac{\varepsilon_k}{k_B T} \frac{d}{dT}\left(\frac{1}{e^{\varepsilon_k/k_B T}+1}\right) $$

Now, assuming that $\varepsilon_k = \varepsilon_k(T)$ *via* $\Delta(T)$, we can develop $\partial f_k / \partial T$:

$$ \frac{\partial f_k}{\partial T} = \frac{d}{dT} \left(\frac{1}{e^{\varepsilon_k/k_B T}+1}\right) \\ = \frac{-\frac{d}{dT}[e^{\varepsilon(T)/k_B T}]}{(e^{\varepsilon_k(T)/k_B T}+1)^2} \\ 
= \frac{e^{\varepsilon_k/k_BT}\left(\frac{\varepsilon_k}{k_B T^2} - \frac{1}{k_B T}\frac{\partial \varepsilon_k(T)}{\partial T}\right)}{(e^{\varepsilon_k(T)/k_B T}+1)^2} $$

Since $\varepsilon_k = \sqrt{\Delta_k^2 + \xi_k^2}$, we can easily deduce that $\partial \varepsilon_k / \partial T = \frac{\Delta_k(T)}{\varepsilon_k}\frac{d\Delta}{dT}$. Thus we can write:

$$\frac{\partial f_k}{\partial T} = \frac{e^{\varepsilon_k/k_BT}\left(\frac{\varepsilon_k}{k_B T^2} - \frac{\Delta_k(T)}{k_B T \varepsilon_k}\frac{d\Delta_k}{dT}\right)}{(e^{\varepsilon_k(T)/k_B T}+1)^2} \\ = f_k(1-f_k)\left(\frac{\varepsilon_k}{k_B T^2} - \frac{\Delta_k(T)}{k_B T \varepsilon_k}\frac{d\Delta_k}{dT}\right)$$

$$ C = 2 k_B T \sum_k \frac{\varepsilon_k}{k_B T} f_k(1-f_k)\left(\frac{\varepsilon_k}{k_B T^2} - \frac{\Delta_k(T)}{k_B T \varepsilon_k}\frac{d\Delta_k}{dT}\right) \\ = 2 \sum_k \left(\frac{\varepsilon_k^2}{k_B T^2} - \frac{\Delta_k(T)}{k_B T}\frac{d\Delta_k}{dT}\right)f_k(1-f_k) \\ = \frac{2}{k_B T^2}\sum_k \left(\varepsilon_k^2 - T \Delta_k \frac{d\Delta_k}{dT}\right)f_k(1-f_k) \\ = \frac{2}{k_B T^2} \mathcal{N}(0)\int_0^\infty d\xi f(\varepsilon) [1-f(\varepsilon)]\left(\varepsilon^2 - T \Delta \frac{d\Delta}{dT}\right)$$

