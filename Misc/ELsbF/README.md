# ELsbF
## Misc

> Binary Binary?

### Files
- lsb

### Analysis
The file provided is a data file, opening the file in Notepad shows that its just Hexadecimal<br />
The challenge name suggests that Least Significant Bits(LSB) is part of the challenge

### Solution
1. Convert the Hex to 8 bit binary
   Using tools such as [CyberChef](https://gchq.github.io/CyberChef/)
2. Extract the least significant bits of the binary
   Write a Python script to split the binary and extract the last digit of each 8 bit binary<br />
   This will generate a hex dump if done correctly
3. Craft the file
   Paste the hex dump into a Hex editor such as HxD
4. Get the flag
   Execute the file with ```bash
   ./lsb
   ``` or ```strings lsb```
