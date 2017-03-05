from aiosmtpd.controller import Controller
from api_mailgun import MailgunMessage


async def server(loop, config):
    cont = Controller(MailgunMessage(config=config), hostname=config.get('SMTP', 'host'), port=int(config.get('SMTP', 'port')))
    cont.start()
