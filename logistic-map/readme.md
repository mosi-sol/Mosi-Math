The core mathematical formula logistic map, on this code is:

$\[x_{n+1} = r \cdot x_n \cdot (1 - x_n)\]$

Where:
- $\(x_{n+1}\)$ is the value of $\(x\)$ at the next iteration,
- $\(r\)$ is a parameter that influences the behavior of the system,
- $\(x_n\)$ is the current value of $\(x\)$.

This formula is used iteratively to simulate the dynamics of the logistic map, a classic example of how simple nonlinear 
systems can exhibit complex behavior, including chaos, under certain conditions.

#

Example setup:
- `r:3.141592` , `x:0.5` , `iterations:100`
- `r:2.718` , `x:0.5` , `iterations:100`
- `r:0.5` , `x:0.5` , `iterations:100`

Groeth model example (impossible mission):
- r: 1.589048505890485
- x: 0.00005890485
- iterations: 30
