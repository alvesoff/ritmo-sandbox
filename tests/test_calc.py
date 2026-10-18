import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import calc


class Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
