from aiosmtpd.handlers import Message


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

        self.api_send(self.config, from_address, to_addresses, subject, text, html)
