Title: Statistical Physics - Problem set
Date: 2019-12-10 10:20
Category: Physics
Tags: Statistics
Slug: Problems
Author: Rémy Torro
Status: draft
Summary: A collection of statistics and statistical physics problems.
<br>

## Statistics

**Problem**: what are the chances that at least two people in your class have the same birthday?

The easiest way to solve this problem is to look at the probability that "not two people in the class have the same birthday". On average, a year contains $365$ days, so the probability to have a birthday on a given day is $\frac{1}{365}$. The number of students in the class is set to $30$. If a student has his birthday on a particular day, the probability for another student not to have the same birthday as the first one is $\frac{364}{365}$. For the next student, the probability that his birthday is different from the other two is $\frac{363}{365}$, and so on...

$$ p(\overline{B}) = \underbrace{\frac{365}{365}\times \frac{364}{365}\times ... \times \frac{336}{365}}_{30 \ \textrm{elements}}$$ 

$$ p(\overline{B}) = \frac{1}{(365)^{30}} \times 365 \times 364 \times ... \times 336  = \frac{365!}{365^{30}(365 - 30)!} $$

Numerically one obtains $p(\overline{B}) = 0.294$. As a result the probability that at least two people in my class have the same birthday is $p(B) = 1 - p(\overline{B}) = 1 - 0.294 = 70.6 \%$.

<hr>

**Problem**: a particle is moving in a one-dimensional line along discrete locations. What is the probability that the particle returns to the origin after $N$ steps? How does the probability behave for large $N$? If $p = 1/2$? 

Let's define $p$ as the probability of moving to the right and $q$ the probability of moving to the left. The condition $p+q = 1$ is necessary. Let's denote $n_r$ the number of steps taken to the right and $n_l$ the number of steps taken to the left. We have $n_r + n_l = N$ and $n_r - n_l = x$, where $N$ is the total number of steps and $x$ some discrete position on the line. 

The number of steps $N$ has to be even in order to allow the particle to return to $0$. Let's assume that the number of time steps is even, i.e. $t = 2m$. Since we are interested in going back to $x=0$ after $t=N$ steps, we have $n_l = n_r$. But $n_r = \frac{N+x}{2} = \frac{N}{2} = n_l$. The binomial probability of moving by $\frac{N}{2}$ steps to the left in $t=N$ s is:

$$ p(x=0,t=N)=\begin{pmatrix}N \\ \frac{N}{2} \end{pmatrix}p^{\frac{N}{2}} q^{N - \frac{N}{2}} $$

For large $N=2m$ we can use Stirling's approximation: $m! \sim m^{m+1/2}e^{-m}\sqrt{2\pi}$. 


