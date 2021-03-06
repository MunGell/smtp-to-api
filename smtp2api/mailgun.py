import logging
import requests

from smtp2api.api import ApiMessage

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Mailgun(ApiMessage):
    def api_send(self, config, from_address, to_addresses, subject, text, html=None,
                 cc=None, bcc=None, attachments=None):
        data = {
            "from": from_address,
            "to": to_addresses,
            "subject": subject,
            "text": text
        }

        if html is not None:
            data['html'] = html

        response = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(config.get('API', 'login')),
            auth=("api", config.get('API', 'api_key')),
            data=data)

        log.info('Email to % got response %', to_addresses, response)

        return response
