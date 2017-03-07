from aiosmtpd.handlers import Message


class ApiMessage(Message):
    def __init__(self, config, message_class=None):
        super(ApiMessage, self).__init__(message_class=message_class)
        self.config = config

    def handle_message(self, message):
        # print(message.items())
        # body =
        # print(body)
        # maintype, subtype = part.get_content_type().split('/')
        # type = 'html' if subtype == 'html' else 'text'

        from_address = message.get('From')
        to_addresses = message.get('To')
        subject = message.get('Subject')
        text = str(message.get_body(preferencelist=('plain')))
        html = str(message.get_body(preferencelist=('html')))

        self.api_send(self.config, from_address, to_addresses, subject, text, html)
