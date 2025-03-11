# EX01 Developing a Simple Webserver
## Date:11/03/2025

NAME : VIJAYAKUMAR S

REG NO: 212224040359

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>

<html lang="en">

  <head>
  
    <meta charset="UTF-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Simple Website</title>
    
    
    
    <style>
    
        body {
        
            font-family: Arial, sans-serif;
            
            text-align: center;
            
            margin: 0;
            
            padding: 0;
        }
        
        
        header, footer {
        
            
            background: #333;
            
            color: white;
            
            
            padding: 10px;
        }
        
        
        .content {
        
            padding: 20px;
        }
        
    </st
    yle>
</head>

<body>
  
  <header>
  
    <h1>My Simple Website</h1>
    
    
    
    </header>
    
    <div class="content">
    
        <p>Welcome to my website. This is a simple layout.</p>
    </div>
    
    <footer>
    
        <p>&copy; 2025 My Website</p>
    </footer>

</body>

</html>
"""

class myhandler(BaseHTTPRequestHandler):

    def do_GET(self):
    
        print("request received")
        
        self.send_response(200)
        
        self.send_header('content-type', 'text/html; charset=utf-8')
        
        self.end_headers()
        
        
        self.wfile.write(content.encode())
server_a
ddress = ('',80)

httpd = HTTPServer(server_address,myhandler)

print("my webserver is running...")


httpd.serve_forever()

## OUTPUT:

![Screenshot 2025-03-11 120306](https://github.com/user-attachments/assets/2a2749f6-8790-4d42-87ec-92331da409a4)


![Screenshot 2025-03-11 115921](https://github.com/user-attachments/assets/2919b61a-7950-4510-82ef-e0916c2f60ff)



## RESULT:
The program for implementing simple webserver is executed successfully.

