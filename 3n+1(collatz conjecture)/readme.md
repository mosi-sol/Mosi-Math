The possible reverse of a number in odd or even with collatz conjecture.

This code reverse the opperations of collatz to find the root of numbers in several odd and even possibilities.

> made by mosi , 2000, shiraz university

- i changed my base "c" code to this python code

I has observe so many twin numbers made a pattern, like `61`:
```
1952 (even) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
325 (odd) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
324 (even) | 162 (even) | 81 (odd) | 244 (even) | 122 (even) | 61 (start)
```
The number `61` have 3 branches in 5 time reverses.\
On this observation you can watching `324` and `325` are twins in the root of `61`

When i try to 10 branches i looking interesting information:
```
62464 (even) | 31232 (even) | 15616 (even) | 7808 (even) | 3904 (even) | 1952 (even) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
10410 (even) | 5205 (odd) | 15616 (even) | 7808 (even) | 3904 (even) | 1952 (even) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
10408 (even) | 5204 (even) | 2602 (even) | 1301 (odd) | 3904 (even) | 1952 (even) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
1734 (even) | 867 (odd) | 2602 (even) | 1301 (odd) | 3904 (even) | 1952 (even) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
10400 (even) | 5200 (even) | 2600 (even) | 1300 (even) | 650 (even) | 325 (odd) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
1733 (odd) | 5200 (even) | 2600 (even) | 1300 (even) | 650 (even) | 325 (odd) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
1732 (even) | 866 (even) | 433 (odd) | 1300 (even) | 650 (even) | 325 (odd) | 976 (even) | 488 (even) | 244 (even) | 122 (even) | 61 (start)
10368 (even) | 5184 (even) | 2592 (even) | 1296 (even) | 648 (even) | 324 (even) | 162 (even) | 81 (odd) | 244 (even) | 122 (even) | 61 (start)
```
Actually after long observation i found the pattern.\
All numbers make same branches in different possibilities.

A wonderfull relation between 3 and 10 or 33 and 100 or similar numbers exist!!!
