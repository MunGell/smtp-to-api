from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP as Server


class SMTPController(Controller):
    def factory(self):
        return Server(self.handler, decode_data=True)
