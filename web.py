from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
<style>
    table { width: 50%; margin: 20px auto; border-collapse: collapse; }
    th, td { padding: 10px; text-align: center; border: 1px solid black; }
    h1 { text-align: center; color: #0066cc; }
    .tagline { text-align: center; font-size: 20px; color: #ff5733; }
</style>
</head>
<body>
<h1>Welcome to RCB</h1>
<p class="tagline">Play Bold</p>
<h2>RCB Players (Captain: Virat Kohli)</h2>
<table>
<tr>
<th>#</th>
<th>Player Name</th>
<th>Jersey Number</th>
</tr>
<tr><td>1</td><td>Virat Kohli (Captain)</td><td>18</td></tr>
<tr><td>2</td><td>Glenn Maxwell</td><td>32</td></tr>
<tr><td>3</td><td>Faf du Plessis</td><td>13</td></tr>
<tr><td>4</td><td>Dinesh Karthik (DK)</td><td>19</td></tr>
<tr><td>5</td><td>Mohammed Siraj</td><td>73</td></tr>
<tr><td>6</td><td>Shane Watson</td><td>33</td></tr>
<tr><td>7</td><td>Chris Gayle</td><td>333</td></tr>
<tr><td>8</td><td>Dale Steyn</td><td>2</td></tr>
<tr><td>9</td><td>David Willey</td><td>22</td></tr>
<tr><td>10</td><td>Rajat Patidar</td><td>87</td></tr>
<tr><td>11</td><td>Josh Hazlewood</td><td>15</td></tr>
<tr><td>12</td><td>Anuj Rawat</td><td>14</td></tr>
<tr><td>13</td><td>Devdutt Padikkal</td><td>37</td></tr>
<tr><td>14</td><td>K L Rahul</td><td>1</td></tr>
<tr><td>15</td><td>Yuzvendra Chahal</td><td>3</td></tr>
</table>
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

server_address = ('', 80)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()