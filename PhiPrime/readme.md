## Code logic and math formula:

### 1. Prime Number Definition

A prime number is a natural number greater than 1 that has no positive divisors other than **1** and itself. The mathematical definition is:

$\[ p \in \mathbb{N}, \; p > 1 : \forall d \in \mathbb{N}, (d | p) \Rightarrow (d = 1 \lor d = p) \]$

Where $\(d | p\)$ denotes that $\(d\)$ is a divisor of $\(p\)$, and $\(\mathbb{N}\)$ is the set of natural numbers.

### 2. Finding Prime Numbers

The code uses a simple trial division algorithm to check if a number $\(n\)$ is prime by attempting to divide $\(n\)$ by 
all smaller numbers greater than 1 and up to $\(\sqrt{n}\)$. If none of these divisions result in a whole number, $\(n\)$ is 
prime. The mathematical basis for this is:

$$\[ \text{is\_prime}(n) : \nexists d \in \mathbb{N}, 1 < d < \sqrt{n} + 1 : d | n \]$$

### 3. Distribution and Gap Analysis

- **Distribution**: The code plots the distribution of prime numbers within the specified range, showing how many primes
are found within sub-ranges (**bins**). This is a visual representation and doesn't have a direct mathematical formula, but
it's related to the Prime Number Theorem in a broader sense, which describes the asymptotic distribution of prime numbers.
  
- **Gap Analysis**: This refers to examining the differences in value between consecutive prime numbers.
If $\(p_i\)$ and $\(p_{i+1}\)$ are consecutive primes, the gap $\(g_i\)$ is:

$\[ g_i = p_{i+1} - p_i \]$

The code visualizes these gaps for the primes found in the specified range.

### Prime Number Theorem (PNT)

In relation to the distribution of primes, the Prime Number Theorem provides a deeper insight, 
stating that the number of primes less than a number $\(x\)$ is approximately equal to:

$\[ \pi(x) \sim \frac{x}{\ln(x)} \]$

Where $\(\pi(x)\)$ is the prime-counting function that returns the number of primes less than or equal 
to $\(x\)$, and $\(\ln(x)\)$ is the natural logarithm of $\(x\)$.

#

The core mathematical operation in the provided Python code for finding prime numbers within a specified 
range (from $\(x\)$ to $\(y\))$ is based on the trial division method to test the primality of each number. 
The essential mathematical concept behind this code can be summarized by the following formula for checking if a number $\(n\)$ is prime:

$$\[ \text{is\_prime}(n) = 
\begin{cases} 
\text{false} & \text{if } n \leq 1 \\
\text{false} & \text{if } \exists d \in \mathbb{N}, 2 \leq d \leq \sqrt{n} : d | n \\
\text{true} & \text{otherwise}
\end{cases}
\]$$

Where:
- $\(n\)$ is the number being tested for primality.
- $\(d\)$ represents any natural number divisor of $\(n\)$.
- $\(d | n\)$ denotes that $\(d\)$ divides $\(n\)$ with no remainder.
- $\(\sqrt{n}\)$ is the square root of $\(n\)$, and it's used as the upper limit for checking divisors because if $\(n\)$ has a divisor greater than its square root, it will necessarily have a corresponding divisor smaller than its square root, thus making further checks redundant.

In simpler terms, this formula states that a number $\(n\)$ is considered prime if it is greater than 1 and has no divisors 
other than 1 and itself. The trial division method tests this by checking for divisors from 2 up to the square root 
of $\(n\)$. If any divisor is found within this range, $\(n\)$ is not prime; otherwise, it is prime.

> latex not good work on github, so some math formula not good show (where symbol $ start and finish line)
