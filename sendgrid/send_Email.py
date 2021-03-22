import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Have to set the environment variable for it to work
#os.environ['SENDGRID_API_KEY'] = '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'

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

