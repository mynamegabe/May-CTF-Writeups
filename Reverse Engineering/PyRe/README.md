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

encoder.py
```python
def lMaO(fHpr):
    kJqB = ""
    lKyM = " "
    for sDhe in fHpr:
        kJqB += chr(ord(sDhe)+ord(lKyM))
        lKyM = sDhe
    return kJqB
```

### Solution
1. Write a script like solve.py -> decode() with the encoded string
   ```python
   def encode(fHpr):
      encoded = ""
      prevchar = " "
      for sDhe in fHpr:
          encoded += chr(ord(sDhe)+ord(prevchar))
          print(ord(sDhe)+ord(prevchar))
          prevchar = sDhe
      return encoded

   def decode(str1):
      decoded = ""
      prevchar = " "
      for char in str1:
          print(decoded)
          decoded += chr(ord(char)-ord(prevchar))
          prevchar = chr(ord(char)-ord(prevchar))
      return decoded

   decode("n§©ËàßÙ\x93§Ö\x94b\x90\x93\x98ÈÍÝÝ\x99\x9eÍ\x93\x98\x94\x91ÅÉ\x98gi\x99\x9dnnihhg\x9b\x99lkhljjolmmk\x97\x9a¶")
   ```
