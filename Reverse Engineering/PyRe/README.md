# PyRe
## Reverse Engineering

> Can you reverse this easy encoding?
>
> n§©ËàßÙ\x93§Ö\x94b\x90\x93\x98ÈÍÝÝ\x99\x9eÍ\x93\x98\x94\x91ÅÉ\x98gi\x99\x9dnnihhg\x9b\x99lkhljjolmmk\x97\x9a¶

### Files
- encoder.py

### Analysis
Analyse encoder.py, it is slightly obfuscated<br />
The code uses the ASCII number of the previous character in the input to encode the next character

### Solution
1. Run solve.py -> decode() with the encoded string
