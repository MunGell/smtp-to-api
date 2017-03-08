from email.message import EmailMessage
from .smtp_controller import SMTPController
from .api_mailgun import MailgunMessage


async def server(loop, config):
    handler = MailgunMessage(config=config, message_class=EmailMessage)
    cont = SMTPController(handler=handler, hostname=config.get('SMTP', 'host'), port=int(config.get('SMTP', 'port')))
    cont.start()
