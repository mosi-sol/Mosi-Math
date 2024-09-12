### Exploring THRIME Equation: Finding Prime Numbers from Even Numbers in a Logarithmic Sequence
> *Thrime is an observation of an expermential work. This is not Prime factory.*

In mathematics, prime numbers are fascinating due to their irregular distribution and the challenge they present in number theory. In this article, we explore a specific sequence that tests whether sums of certain even numbers with the constant 3 yield prime numbers. This approach uses a logarithmic pattern to select even numbers, excluding those that end in 6, and then checks if the result is prime.

### Equation Overview

The main goal is to examine sums of the form:

$$\
S = 3 + E
\$$

Where:
- $$\( E \)$$ is an even number, but **it should not end in 6**.
- $$\( S \)$$ is the sum of $$\( 3 + E \)$$, and we check if $$\( S \)$$ is a prime number.

This equation is applied in a sequence of even numbers that are progressively selected based on a logarithmic progression. Specifically, for each iteration, we calculate the sum using an even number from a set of valid numbers, but the index of the even number grows logarithmically.

### The Logarithmic Progression

Logarithmic growth is slower than linear growth, making it an interesting choice for this sequence. For each step $$\( i \)$$, we choose the next even number based on a step size that is proportional to the logarithm (base 2) of \( i+2 \). This creates a sequence where larger gaps between even numbers are explored as \( i \) increases.

### Prime Number Check

Once we have the sum $$\( S = 3 + E \)$$, we check whether $$\( S \)$$ is a prime number. Prime numbers are those greater than 1 that have no divisors other than 1 and themselves. We use a basic algorithm to test primality for each value of \( S \).

### Results

After applying this method to a range of even numbers up to 1000, we obtained two sets of results:
1. **Prime numbers**: The sums $$\( 3 + E \)$$ that result in prime numbers.
2. **Non-prime numbers**: The sums $$\( 3 + E \)$$ that do not result in primes.

Here are the prime and non-prime numbers found:

#### Prime Numbers:
```
[7, 11, 17, 23, 31, 37, 41, 43, 53, 61, 67, 71, 73, 83, 97, 101, 103, 107, 113, 127, 131, 137, 151, 157, 163, 167, 181, 191, 193, 197, 211, 223, 227, 233, 241, 251, 257, 263, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 353, 367, 373, 383, 397, 401, 421, 431, 433, 443, 457, 461, 463, 467, 487, 491, 503, 521, 523, 541, 547, 557, 563, 571, 577, 587, 593, 601, 607, 613, 617, 631, 641, 643, 647, 653, 661, 673, 677, 683, 691, 701, 727, 733, 743, 751, 757, 761, 773, 787, 797, 811, 821, 823, 827, 853, 857, 863, 877, 881, 883, 887, 907, 911, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
```

#### Non-Prime Numbers:
```
[15, 21, 27, 33, 35, 45, 51, 55, 57, 63, 65, 75, 77, 81, 85, 87, 93, 95, 105, 111, 115, 117, 121, 123, 125, 133, 135, 141, 143, 145, 147, 153, 155, 161, 165, 171, 175, 177, 183, 185, 187, 195, 201, 203, 205, 207, 213, 215, 217, 221, 225, 231, 235, 237, 243, 245, 247, 253, 255, 261, 265, 267, 273, 275, 285, 287, 291, 295, 297, 301, 303, 305, 315, 321, 323, 325, 327, 333, 341, 343, 345, 351, 355, 357, 361, 363, 365, 371, 375, 377, 381, 385, 387, 391, 393, 395, 403, 405, 407, 411, 413, 415, 417, 423, 425, 427, 435, 437, 441, 445, 447, 451, 453, 455, 465, 471, 473, 475, 477, 481, 483, 485, 493, 495, 497, 501, 505, 507, 511, 513, 515, 517, 525, 527, 531, 533, 535, 537, 543, 545, 551, 553, 555, 561, 565, 567, 573, 575, 581, 583, 585, 591, 595, 597, 603, 605, 611, 615, 621, 623, 625, 627, 633, 635, 637, 645, 651, 655, 663, 665, 667, 671, 675, 681, 685, 687, 693, 695, 697, 703, 705, 707, 711, 713, 715, 717, 721, 723, 725, 731, 735, 737, 741, 745, 747, 753, 755, 763, 765, 767, 771, 775, 777, 781, 783, 785, 791, 793, 795, 801, 803, 805, 807, 813, 815, 817, 825, 831, 833, 835, 837, 841, 843, 845, 847, 851, 855, 861, 865, 867, 871, 873, 875, 885, 891, 893, 895, 897, 901, 903, 905, 913, 915, 917, 921, 923, 925, 927, 931, 933, 935, 943, 945, 951, 955, 957, 961, 963, 965, 973, 975, 981, 985, 987, 993, 995, 1001, 1003]
```

### Observations

1. **Prime Numbers**: We observe a steady stream of primes distributed throughout the sequence. These primes tend to be more frequent in the earlier part of the sequence but still appear at regular intervals even as the logarithmic progression advances.
   
2. **Non-Prime Numbers**: The non-prime sums fill the gaps between the primes. As expected, there are more non-prime sums than prime sums, which reflects the overall distribution of prime numbers in number theory.

### Visualizing the Results
- [code here](https://github.com/mosi-sol/Mosi-Math/blob/main/Thrime!/thrime.py)

We can plot the distribution of prime and non-prime sums to better understand their spread. The scatter plot below shows how the sums evolve and whether they are prime or non-prime:

#### Plot:
- **Green points** represent sums that are prime.
- **Red points** represent sums that are non-prime.

This visual representation highlights the irregular distribution of primes and non-primes in the sequence.

### Conclusion

This exploration of primes using even numbers in a logarithmic sequence provides an interesting insight into how prime numbers are distributed when sums are formed with a fixed constant (3). While primes become less frequent as the numbers grow larger, the logarithmic step ensures that large gaps are explored, leading to the discovery of primes even in higher ranges. This approach could be further expanded to explore similar equations or number patterns.

> This is not Prime Prodecure/Factory, just an observation.
