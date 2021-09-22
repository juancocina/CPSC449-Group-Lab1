# CPSC449-Group-Lab1
Professor Kenytt Avery

Group Members:
- Juan Cocina
- Alberto Perez
- Tilak Ghorashainee

# Project Objective:
In this project you will familiarize yourself with Python and the HTTP protocol by implementing an HTTP client and server.

Running redact.py in your terminal will give you both a terminal response
and a response at localhost:8080.

Entering 'python3 redact.py' will return usage and a message to include a url path.
Entering 'python3 redact.py /because/ProfAvery' (for example) will retrieve a message/response
from foaas.com, which has been passed through PurgoMalum. This redacts any profanity from the message.

After, a server will start. You can access the webpage at localhost:8080, which does not yet have a message.
To receive a message similar to the terminal, you must include a path such as '/because/ProfAvery' 
at the end of the localhost url.
For example, 'http://localhost:8080/because/ProfAvery'

This will display a censored message, a subtitle, and a link to foaas.com

Full project information can by found here
https://docs.google.com/document/d/1Jsjhd28TX1GY1sWxFZhYHaCJ9yAb8Klyiu_iK5sP64k/edit#
