from email.message import EmailMessage
from smtp_controller import SMTPController
from api_mailgun import MailgunMessage


async def server(loop, config):
    cont = SMTPController(MailgunMessage(config=config, message_class=EmailMessage), hostname=config.get('SMTP', 'host'), port=int(config.get('SMTP', 'port')))
    cont.start()
