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