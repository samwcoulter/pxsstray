import unittest
from pxsstray import xset


class TestXSetMethods(unittest.TestCase):
    def test_echo(self):
        print(xset.xset_q())


if __name__ == "__main__":
    unittest.main()
