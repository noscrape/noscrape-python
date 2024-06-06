import unittest

import noscrape

class TestNoscrape(unittest.TestCase):
    def test_noscrape(self):
        n = noscrape.Noscrape("example/example.ttf")

        xy = n.obfuscate("test")
        self.assertNotEquals(xy, "test")

        xyz = n.render()
        self.assertNotEquals(xyz, "test")


if __name__ == '__main__':
    unittest.main()
