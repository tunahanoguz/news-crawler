from configparser import ConfigParser, Error as ConfigParserError
import os
from exceptions import ConfigFileNotFoundException, InvalidConfigFileException


class ConfigFileParser:
    def __init__(self, file_name, section):
        self._file_name = file_name
        self._section = section

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        self._section = value

    def parse(self):
        try:
            config_file_path = os.path.join(os.path.dirname(__file__), self._file_name)

            if not os.path.isfile(config_file_path):
                raise OSError

            parser = ConfigParser()
            parser.read(config_file_path)

            if not parser.has_section(self._section):
                raise ConfigParserError

            db_config = {}
            for param in parser.items(self._section):
                db_config[param[0]] = param[1]

            if not db_config:
                raise ConfigParserError

            return db_config
        except OSError:
            raise ConfigFileNotFoundException
        except ConfigParserError as e:
            raise InvalidConfigFileException(e)

    def __str__(self):
        return f"File Name: {self._file_name}, Section: {self._section}"
