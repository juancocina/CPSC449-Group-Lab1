# Class: CPSC 449
# Project: # 1
# Members: Tilak Ghorashainee, Juan Cocina, Alberto Perez ..

# Project Description can be found at the repo...
import sys
import ssl
import http.client
import json
import urllib
import urllib.request

import http.server
import socketserver

PORT = 8080

def servercall(p):
    pay=p
    
    class ExHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
    
            payload = '<h1>'+pay+'</h1>'
            self.wfile.write(payload.encode('utf-8'))
            
    with socketserver.TCPServer(("", PORT), ExHTTPRequestHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

# Display script use
print('Usage: redact URL')
print('Please include a FOAAS url')
print('Example: "/because/ProfAvery" ')

# Take the url from argv using sys.argv
f = sys.argv[1]

# Use http.client.HTTPSConnection with the Accept: application/json request header
h1 = http.client.HTTPSConnection("foaas.com")
headers = {"Accept": "application/json"}
h1.request("GET", f, "", headers)

# checking response from foaas
res = h1.getresponse()
if res.status == 200:
    print("Successfully connected")

    # converting incoming message to json and parsing
    incoming = res.read()
    data = json.loads(incoming.decode())
    message = data['message']
    subtitle = data['subtitle']
    print("Raw data: ", data)
    print("'Message' parameter: ", message)
    parsed_message = urllib.parse.quote(message)
    print("Parsed: ", parsed_message)
    print('')

    # connecting to purgomalum.com, retreiving message, converting to json, printing
    url = "https://www.purgomalum.com/service/json?text=" + parsed_message
    h2 = urllib.request.urlopen(url)
    censored = h2.read()
    censored_data = json.loads(censored.decode())
    # prints the final censored message
    final_message = censored_data['result']
    print(json.dumps(final_message, indent = 4))
    print(json.dumps(subtitle, indent = 4))
    
    mes=json.dumps(final_message, indent = 4)
    
    servercall(p=mes)

else:
    # exit program
    print("Check URL")
    exit(1)
