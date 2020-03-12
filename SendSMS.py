#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#!/usr/bin/env python3
import sys
import os
import plivo
import sys
import cgi, cgitb
"""
Accepts a number from a form.
"""

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<title>Send an SMS!</title>")
print ("</head>")
print ("<body>")
print ("<h2>Message sent</h2>" )
print ("</body>")
print ("</html>")

def sendSMS(dest_number, text):
    dst = dest_number
    client = plivo.RestClient(auth_id='INSERT AUTH ID HERE', auth_token='INSERT AUTHTOKEN HERE')
    message_created = client.messages.create(
        src=('NUMBER YOU BOUGHT ON PLIVO'),
        dst=dest_number,
        text=text,
        url='INSERT API ENDPOINT HERE'
    )

def main():
    # dest_number = sys.argv[1]
    # text = sys.argv[2]
    form =cgi.FieldStorage()
    cgitb.enable()
    dest_number=form.getvalue('number')
    text=form.getvalue('msg')
    sendSMS(dest_number, text)

if __name__=="__main__":
    main()

