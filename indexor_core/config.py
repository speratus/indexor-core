import os
import configparser


class Config:

    def __init__(self, engine_url="", sql_dialect="", db_url=""):
        self.engine_url = engine_url
        self.sql_dialect = sql_dialect
        self.db_url = db_url


def ini_file_loader(path):
    if not os.path.exists(path):
        return Config()

    config = configparser.ConfigParser()

    config.read(path)

    config.sections()

    if 'server' not in config:
        return Config()

    return Config(engine_url=config['server']['engine_url'])
