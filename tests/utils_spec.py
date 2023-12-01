import unittest
from modules.utils import string_to_number, decode_coodinate

class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_string_to_number(self):
        resolved = string_to_number('eighttkbtzjz6nineeightnine')
        self.assertEqual(resolved, '8')

        resolved = string_to_number('eighttkbtzjz6nineeightnine', reverse_search=True)
        self.assertEqual(resolved, '9')

    def test_decode_coordinate(self):
        resolved = decode_coodinate('eighttkbtzjz6nineeight')

        self.assertEqual(resolved, 88)
    
    def test_decode_coordinate_2(self):
        resolved = decode_coodinate('fivefafasfaone78onethree')

        self.assertEqual(resolved, 53)

if __name__ == '__main__':
    unittest.main()