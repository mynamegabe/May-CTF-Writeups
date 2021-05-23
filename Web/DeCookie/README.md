# DeCookie
## Web

> Seems like we need to do this over and over again
>
> http://mctf-decookie.herokuapp.com/

### Files
- N/A

### Analysis
The website asks for an answer without a question
The challenge name suggests the challenge is related to the cookies
The description suggests that an action has to be repeated

### Solution
1. View the cookie
   There is a session cookie that is Base64 encoded.<br />
   > eyJ1c2VybmFtZSI6ICJEUUpHWTJFSFU5NjQwUVU3TDlRVCIsICJhbnN3ZXIiOiAiMjZFUkxQWDRNQ004VkFPN1FXRzAifQ==
2. Decode the cookie
   Use a tool such as [CyberChef](https://gchq.github.io/CyberChef/) to decode the cookie<br />
   > {"username": "DQJGY2EHU9640QU7L9QT", "answer": "26ERLPX4MCM8VAO7QWG0"}
3. Input the answer
   The answer goes through but nothing happens, linking back to the challenge description, but the number of correct answers required is unknown
4. Write a script
   Write a program using Python with the Selenium module to read and decode the cookie and send the answer until a flag is returned.
   https://github.com/Derrick-Png/CTF-Writeups/tree/main/2021/NYP%20May%20CTF/Decookie
   
