import asyncio
import configparser

from .smtp_server import server


class Application:
    @staticmethod
    def run():
        config = configparser.ConfigParser()
        config.read('config.ini')
        loop = asyncio.get_event_loop()
        loop.create_task(server(loop=loop, config=config))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
