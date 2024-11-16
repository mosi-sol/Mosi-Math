## Divisibility Rules for Binary Numbers

Understanding the divisibility of binary numbers involves applying specific rules based on the properties of binary representation. Below are the rules for determining if a binary number is divisible by integers from 0 to 10.

### **Divisibility by 0**
- **Rule**: No number can be divisible by zero, except for zero itself.

### **Divisibility by 1**
- **Rule**: Every number is divisible by 1.

### **Divisibility by 2**
- **Rule**: A binary number is divisible by 2 if it ends in **0**.
- **Example**: $$11010_2$$ (binary) is divisible by 2, while $$11011_2$$ is not.

### **Divisibility by 3**
- **Rule**: Calculate the alternating sum of the bits. If the result is divisible by 3, then the binary number is also divisible by 3.
- **Formula**: 
  $$S = b_1 - b_2 + b_3 - b_4 + \ldots$$
  where $$b_i$$ are the bits of the binary number.
- **Example**: For $$110011_2$$, $$S = 1 - 1 + 0 - 0 + 1 - 1 = 0$$, which is divisible by 3.

### **Divisibility by 4**
- **Rule**: A binary number is divisible by 4 if its last two bits are **00**.
- **Example**: $$10100_2$$ is divisible by 4, while $$10101_2$$ is not.

### **Divisibility by 5**
- **Rule**: Convert the binary number to base 4 and calculate the alternating sum of the digits. If this sum is divisible by 5, then the binary number is also divisible by 5.
- **Example**: For $$11100_2$$:
    - Convert to base 4: Pairs are $$11$$ (3), $$00$$ (0), yielding $$30_4$$.
    - Calculate alternating sum: $$3 - 0 = 3$$, not divisible by 5.

### **Divisibility by 6**
- **Rule**: A binary number must be divisible by both 2 and 3.
- **Example**: Check if it ends in **0** (for divisibility by 2) and apply the alternating sum rule (for divisibility by 3).

### **Divisibility by 7**
- **Rule**: Use a modified alternating sum based on powers of two modulo seven. Multiply each bit from right to left with powers of two that cycle through [1,2,4].
- Example:
    - For $$1101010_2$$:
        - Calculation: 
        $$S = (0 \cdot 1) + (1 \cdot 2) + (0 \cdot 4) + (1 \cdot 1) + (0 \cdot 2) + (1 \cdot 4) + (1 \cdot 1)$$
        - Resulting sum must be checked against modulo seven.

### **Divisibility by 8**
- **Rule**: A binary number is divisible by 8 if its last three bits are **000**.
- **Example**: $$100000_2$$ is divisible by 8, while $$100001_2$$ is not.

### **Divisibility by 9**
- **Rule**: Convert the binary number to base 8 and calculate the alternating sum of the digits. If this sum equals zero, then it’s divisible by 9.
- **Example**: For $$11001001_2$$:
    - Convert to base 8 in triplets: $$011,001,001$$ yields $$1,1,1 = (111)_8$$.
    - Calculate alternating sum: $$1 - 1 + 1 = 1$$, not divisible by 9.

### **Divisibility by 10**
- **Rule**: A binary number must be divisible by both 2 and 5.
- Example: Check for an ending bit of zero and apply the base conversion for divisibility by five.

### Examples
- **Divisibility by 0**: Not applicable (only zero is divisible by zero).
- **Divisibility by 1**: Any binary number (e.g., $$101_2$$).
- **Divisibility by 2**: $$110_2$$ (ends in 0).
- **Divisibility by 3**: $$110011_2$$ (alternating sum equals 0).
- **Divisibility by 4**: $$100_2$$ (last two bits are 00).
- **Divisibility by 5**: $$11001_2$$ (base 4 conversion yields alternating sum of 0).
- **Divisibility by 6**: $$110_2$$ (divisible by both 2 and 3).
- **Divisibility by 7**: $$1110110_2$$ (calculated sum modulo 7 equals 0).
- **Divisibility by 8**: $$1000_2$$ (last three bits are 000).
- **Divisibility by 9**: $$110001001_2$$ (base 8 conversion yields alternating sum of 0).
- **Divisibility by 10**: $$1010_2$$ (divisible by both 2 and 5).

These rules provide a systematic approach to determining divisibility for binary numbers across various bases.

#

### Alternative
Alternative formulas for divisibility from 1 to 10 in binary:

1. **Divisibility by 1**: $$\( \text{Any integer} \)$$

2. **Divisibility by 2**: $$\( b_0 = 0 \)$$

3. **Divisibility by 3**: $$\( |(\text{count of 1s in odd positions}) - (\text{count of 1s in even positions})| \mod 3 = 0 \)$$

4. **Divisibility by 4**: $$\( b_1 b_0 = 00 \)$$

5. **Divisibility by 5**: $$\( \text{Decimal equivalent} \mod 5 = 0 \)$$

6. **Divisibility by 6**: $$\( b_0 = 0 \) and \( |(\text{count of 1s in odd positions}) - (\text{count of 1s in even positions})| \mod 3 = 0 \)$$

7. **Divisibility by 7**: $$\( \text{Decimal equivalent} \mod 7 = 0 \)$$

8. **Divisibility by 8**: $$\( b_2 b_1 b_0 = 000 \)$$

9. **Divisibility by 9**: $$\( \text{Decimal equivalent} \mod 9 = 0 \)$$

10. **Divisibility by 10**: $$\( b_0 = 0 \) and \( \text{Decimal equivalent} \mod 5 = 0 \)$$

These formulas alternative solution of the divisibility rules for numbers 1 through 10 in binary.
