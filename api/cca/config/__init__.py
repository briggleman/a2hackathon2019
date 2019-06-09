import os

from box import Box


def configuration():
    """
    Config object, stores application configuration options
    :return: python-box object
    """
    return Box({
        "route": os.environ.get("ROUTE", "/cca"),
        "address": os.environ.get("ADDRESS", "0x5A4fEC17609eB37b64107A8eB31C0247672D7ad8"),
        "host": "10.248.32.86:7545"
    })


# config object
CONFIG = configuration()
