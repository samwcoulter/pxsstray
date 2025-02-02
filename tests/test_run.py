import unittest
from pxsstray import run


class TestRunMethods(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_echo(self):
        self.assertEqual(run.run(["echo", "hello"]), "hello\n")


if __name__ == "__main__":
    unittest.main()
