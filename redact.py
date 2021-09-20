# Class: CPSC 449
# Project: # 1
# Members: Tilak Ghorashainee, Juan Cocina, ..

# Project Description can be found at the repo...
import sys
import ssl
import http.client
import json
import urllib

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

    # attempting to use json
    incoming = res.read()
    data = json.loads(incoming.decode())
    message = data['message']
    print("Raw data: ", data)
    print("'Message' parameter: ", message)
    parsed_message = urllib.parse.quote(message)
    print("Parsed: ", parsed_message)

    # attempting to connect to purgomalum.com
    h2 = http.client.HTTPSConnection("purgomalum.com")
    h2.request("GET", "/")

else:
    # exit program
    print("Check URL")
    exit(1)