from aiosmtpd.handlers import Message


class ApiMessage(Message):
    def __init__(self, config, message_class=None):
        super(ApiMessage, self).__init__(message_class=message_class)
        self.config = config

    def handle_message(self, message):
        headers = message.items()

        from_address = ''
        to_addresses = ''
        subject = ''
        text = ''
        html = ''

        self.api_send(self.config, from_address, to_addresses, subject, text, html)
