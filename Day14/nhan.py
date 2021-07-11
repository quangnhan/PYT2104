import unittest
from log import Log

class SimpleTest(unittest.TestCase):
    def test_send_log(self):
        string = "abc"
        self.assertEquals(string.upper(),"ABC")
    
        




