import unittest
import tenc


class TestStringMethods(unittest.TestCase):

    def test_encrypt(self):
        self.assertIsNotNone(tenc.encrypt(
            'Test', '5a04ec902686fb05a6b7a338b6e07760'))

        with self.assertRaises(ValueError):
            tenc.encrypt('Test', '123')

        with self.assertRaises(AttributeError):
            tenc.encrypt('Test', None)

    def test_decrypt(self):
        self.assertEqual(tenc.decrypt(tenc.encrypt('Test', '5a04ec902686fb05a6b7a338b6e07760'),
                                      '5a04ec902686fb05a6b7a338b6e07760'), 'Test')

        with self.assertRaises(ValueError):
            tenc.decrypt(tenc.encrypt(
                'Test', '5a04ec902686fb05a6b7a338b6e07760'), '12')


if __name__ == '__main__':
    unittest.main()
