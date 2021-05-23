# Heading
## Web

> The admin thinks he improved the authentication system
> Prove him wrong!
>
> http://mctf-heading.herokuapp.com/

### Files
- N/A

### Analysis
The website asks for a username and has a Flag tab
The website does not authenticate based on the Auth cookie this time
The challenge name suggests that the challenge is related to HTTP reques/response headers

### Solution
1. Open Burp Suite
   Use the proxy feature and navigate to the webpage
2. Testing
   Enter a random username and view the response header<br />
   There is a header named "Priv" with the value "user"
3. Accessing the flag
   With the knowledge that the authentication is done through the headers, edit the headers to access the flag
   Navigate to /flag or click the Flag tab<br />
   Edit the request headers and add "Priv: root"
   Complete the request
   
