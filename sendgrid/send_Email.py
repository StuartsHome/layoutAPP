import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Have to set the environment variable for it to work
#

message = Mail(
    from_email = '?',
    to_emails = '?',
    subject = 'SendGRID email from Python',
    html_content = '<strong> and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print(e.message)

