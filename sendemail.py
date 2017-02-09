import smtplib
from_addr = 'rfredrickez@gmail.com'
to_addr = 'triple_robinson@hotmail.com'
subject = 'Lab1'
to_name = 'Roshane'
from_name = 'Roberto'
msg ='Testing for lab1'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)
# Credentials (if needed)
username = 'rfredrickez@gmail.com'
password = ''
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 