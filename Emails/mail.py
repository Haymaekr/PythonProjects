import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('html_temp.html').read_text())
email = EmailMessage()

email["from"] = 'Moi'
email['to'] = 'dummy.emailed@gmail.com'
email['subject'] = 'This is a Recording'

email.set_content(html.substitute({'name' : "TinTin"}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummy.emailed@gmail.com','Passdoor1')
	smtp.send_message(email)
print("Done!")