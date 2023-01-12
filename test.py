import unittest

import lib

class Testing(unittest.TestCase):
    """ Mescillaneous class for testing functions. """

    def test_gen_read_ministry_url(self):
        lib.gen_read_ministry_url()
        # print("Reached here.")

class TestConfig(unittest.TestCase):

    def test_config_data(self):
        assert isinstance(lib.config, dict), type(lib.config)
        assert lib.config.get('default'), lib.config.items()
        assert 'excel_file' in lib.config['default'], lib.config['default']