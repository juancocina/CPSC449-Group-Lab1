# Class: CPSC 449
# Project: # 1
# Members: Tilak Ghorashainee, Juan Cocina, ..

# Project Description can be found at the repo...
import sys
import ssl
import http.client
import json

# Display script use
print('Usage: redact URL')
print('Please include a FOAAS url')
print('Example: "/because/ProfAvery" ')

# Take the url from argv using sys.argv
f = sys.argv[1]

# Use http.client.HTTPSConnection with the Accept: application/json request header
h1 = http.client.HTTPSConnection("foaas.com")
h1.request("GET", "/")

# checking response from foaas
res = h1.getresponse()
print(res.status, res.reason)
