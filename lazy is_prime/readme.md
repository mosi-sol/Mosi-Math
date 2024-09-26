# is prime (lazy solution)

If a number not divided by `2` and `3`, then `((n^2) - 1) % 24 == 0` then that number is prime.

This solution is fastest way to return the Boolean of `is_prime` on programming. In the math problems can to use this solution for find better and fastest than other algorithm.

The longest solution used on programming is `a^(p-1) ≡ 1 (mod p)`. I hate that, I love lazy-solution just for my computer hardware "resources management" :)

### Why `24`? 
`1*2*3*4` lol. actualy each prime greater of 3 is before or after "6 family" :)

> Made by Mosi, year 2000, Shiraz

---

This code have 1 problem: if number is a factor of a prime like `7^2` or `7*11` the code made wrong answer.\
To fix this problem can to check root of input (root or 2root or...)!
