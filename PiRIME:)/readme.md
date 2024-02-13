## Pi Prime Factory : PiRIME

### Conceptual Representation

Given a range of integers $\([x, y]\)$, the "PIRIME" process can be described through the following steps:

1. **Identify Prime Numbers in Range**: Find all prime numbers, $\(P\)$, within the given range $\([x, y]\)$.

   $\[P = \{p \in \mathbb{N} : x \leq p \leq y, \text{ and } p \text{ is prime}\}\]$

2. **Multiply by π and Round**: For each prime number \(p\) found, calculate \(p \times \pi\). Then, round this product both up and down to obtain two integers,
   $\(R_{\text{down}}\) and \(R_{\text{up}}\)$.

   $\[R_{\text{down}}(p) = \lfloor p \times \pi \rfloor\]$
   $\[R_{\text{up}}(p) = \lceil p \times \pi \rceil\]$

4. **Check for Primality of Rounded Results**: Determine the primality of $\(R_{\text{down}}\) and \(R_{\text{up}}\)$.

   $\[P_{\text{down}} = \{R_{\text{down}}(p) : R_{\text{down}}(p) \text{ is prime}\}\]$
   $\[P_{\text{up}} = \{R_{\text{up}}(p) : R_{\text{up}}(p) \text{ is prime}\}\]$

5. **Output**: The output is a set of tuples where each tuple contains the original prime $\(p\)$, and its corresponding $\(R_{\text{down}}\)$ or $\(R_{\text{up}}\)$ if they are prime.

   $\[O = \{(p, R_{\text{down}}) : R_{\text{down}} \in P_{\text{down}}\} \cup \{(p, R_{\text{up}}) : R_{\text{up}} \in P_{\text{up}}\}\]$
