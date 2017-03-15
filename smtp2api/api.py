import logging
from aiosmtpd.handlers import Message

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class ApiMessage(Message):
    def handle_message(self, message):
        """
        Overrides message handler method.

        Pass email message information to API method.

        Parameters
        ----------
        message : email.message.EmailMessage
        """
        from_address = message.get('From')
        to_addresses = message.get('To')
        subject = message.get('Subject')
        text = str(message.get_body(preferencelist=('plain')))
        html = str(message.get_body(preferencelist=('html')))

        log.info('Got a mail from %s', from_address)
        log.info('Email subject is %s', subject)

        self.api_send(self.config, from_address, to_addresses, subject, text, html)
