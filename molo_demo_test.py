import sys
import unittest
from molo_demo import *

class Test(unittest.TestCase):
    def setUp(self):
        self.host = '10.135.0.18'
        self.port = '18151'
        self.ver = 146
        pass
    def tearDown(self):
        pass

    def test_CmdGetSessionXml(self):
        req = getReq(self.ver, 1000117, 0, 0)
        xmltext = getResponse(self.host, self.port, req)
        decodeBase64(xmltext)
        self.assertEqual(1, 1)


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test_CmdGetSessionXml"))

    Runner = unittest.TextTestRunner()
    Runner.run(suite)
