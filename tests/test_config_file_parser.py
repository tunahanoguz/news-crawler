import unittest
from configs import ConfigFileParser
from exceptions import ConfigFileNotFoundException, InvalidConfigFileException


class TestConfigFileParser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestConfigFileParser, self).__init__(*args, **kwargs)

    def test_parse_with_wrong_file_name(self):
        with self.assertRaises(ConfigFileNotFoundException):
            parser = ConfigFileParser('wrong_config_file.ini', 'postgresql')
            parser.parse()

    def test_parse_with_wrong_section(self):
        with self.assertRaises(InvalidConfigFileException):
            parser = ConfigFileParser('database_config.ini', 'wrong_section')
            parser.parse()

