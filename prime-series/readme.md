## The proof of Behiverial morality of small numbers:

Relation of "**Faulhaber's Fabulous Formula** (and **Bernoulli Numbers**)" to the prime numbers

#### Faulhaber's Formula

Faulhaber's formula for the sum of the kkth powers of the first nn natural numbers can be expressed using Bernoulli numbers (BmBm​) as follows:

$\[Sk(n)=1k+1∑m=0k(k+1m)Bmnk+1−m]]\$ 

`Sk(n)` represents the sum `1k+2k+⋯+nk`, and `(k+1m)` are the binomial coefficients.

#### Bernoulli Numbers and the Riemann Zeta Function

Bernoulli numbers are deeply connected to the Riemann zeta function, `ζ(s)`, for negative integer arguments. 
The Riemann zeta function is defined for `s>1` as:

$\[ζ(s)=∑n=1∞1ns]\$

For negative integers (`s=−n`), where nn is a positive integer, we have:

$\[ζ(−n)=−Bn+1n+1]\$

The zeta function plays a crucial role in the distribution of prime numbers, particularly through its non-trivial 
zeros according to the Riemann Hypothesis.

#### Bernoulli Numbers and Regular Primes

A prime pp is regular if it does not divide the numerator of any of the Bernoulli numbers `B2,B4,…,Bp−3`​. 
This can be algebraically represented by checking for each Bernoulli number `Bk​` (where `k` is even and `2≤k≤p−3`):

$\[p∤numerator(Bk)]\$

If this holds for all `Bk​` in the range, then pp is a regular prime.

#### Euler-Maclaurin Formula

The Euler-Maclaurin formula, which connects sums, integrals, and Bernoulli numbers, is another area where these concepts interplay, though it's more complex and involves calculus. It's used indirectly to study the distribution of prime numbers, especially in analytic number theory.

These equations and relationships showcase the intricate connections between sums of powers (Faulhaber's formula), Bernoulli numbers, and prime numbers, highlighting the deep interplay of these concepts in number theory and beyond.

#

On this python code i convert this relationship to code. 
- When you have want to choose change the range, looking your compute power.
- Can to save result as the text file `.txt`

Prime validation proof:
> Bernoulli numbers are related to prime numbers, notably through their role in the Euler-Maclaurin formula, the Riemann zeta function, and the criteria for regular primes.

