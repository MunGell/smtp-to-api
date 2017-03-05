import asyncio
import configparser

from smtp_server import server

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(server(loop=loop, config=config))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

# import smtpd
# import asyncore
#
# import smtp_to_api.config
#
# server = smtpd.SMTPServer((SMTP_HOST, SMTP_PORT), None)
#
# asyncore.loop()

# class CustomSMTPServer(smtpd.SMTPServer):
#     def process_message(self, peer, mailfrom, rcpttos, data):
#         print('Receiving message from:', peer)
#         print('Message addressed from:', mailfrom)
#         print('Message addressed to  :', rcpttos)
#         print('Message length        :', len(data))
#         return

#
# server = CustomSMTPServer(('127.0.0.1', 1025), None)
#
# asyncore.loop()

# from flask import Flask, request
#
# app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config')
#
#
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def index():
#     print(request)
#     exit()
