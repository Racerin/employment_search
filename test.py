import unittest

import lib

class Testing(unittest.TestCase):

    def test_gen_read_ministry_url(self):
        lib.gen_read_ministry_url()
        # print("Reached here.")