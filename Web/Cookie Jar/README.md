# Cookie Jar
## Web

> Yum!
>
> http://mctf-cookie-jar.herokuapp.com/

### Files
- N/A

### Analysis
Website is a simple username input page<br />
The challenge name suggests that the challenge is related to the cookies<br />
The Flag tab is inaccessible

### Solution
1. Enter a random username
2. Read the cookies
   There is a cookie name "Auth" with a value "No"
3. Edit the cookie
   Open the Developer Console/Inspect Element<br />
   Navigate to the Storage tab and change the value of "Auth" to "Yes"
4. Access the flag
   Click the Flag tab to get the flag
