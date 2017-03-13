from configparser import ConfigParser
from importlib import import_module
from email.message import EmailMessage


def get_handler():
    """
    Gets message handler specified in configuration

    Returns
    -------
    aiosmtpd.handlers.Message
    """
    config = get_config(parser=ConfigParser)
    base_class = get_base_class(config)

    class MessageHandler(base_class):
        def __init__(self, message_class=None):
            super(MessageHandler, self).__init__(message_class=EmailMessage)
            self.config = config

    return MessageHandler


def get_config(parser, path='config.ini'):
    """
    Gets configuration read from the specified file.

    Parameters
    ----------
    parser : ConfigParser()
        configuration parser
    path : string
        path to the configuration file

    Returns
    -------
    ConfigParser
        ConfigParser object
    """
    config = parser()
    config.read(path)
    return config


def get_base_class(config):
    """
    Gets message class name based on configuration

    Parameters
    ----------
    config : ConfigParser

    Returns
    -------
    smtp2api.api.ApiMessage
    """
    vendor = config.get('API', 'vendor')

    module = import_module('smtp2api.' + vendor.lower())

    return getattr(module, vendor.capitalize())
