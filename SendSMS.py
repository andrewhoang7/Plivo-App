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
    client = plivo.RestClient(auth_id='MAMJDMZGIYNMMZNWU0MJ', auth_token='Y2IwNjczNTdiYjU3MTcyNDZjNDAwMjM2ZjhmZjI2')
    message_created = client.messages.create(
        src=('+15613598221'),
        dst=dest_number,
        text=text,
        url='https://api.plivo.com/v1/Account/MAMJDMZGIYNMMZNWU0MJ/Message/'
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

