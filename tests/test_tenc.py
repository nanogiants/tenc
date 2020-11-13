import unittest
from tenc import encrypt, decrypt


class TestStringMethods(unittest.TestCase):

    def test_encrypt(self):
        self.assertIsNotNone(encrypt('Test', '123'))

        with self.assertRaises(AttributeError):
            encrypt('Test', None)

    def test_decrypt(self):
        self.assertEqual(decrypt(encrypt('Test', '123'), '123'), 'Test')

        with self.assertRaises(ValueError):
            decrypt(encrypt('Test', '123'), '12')


if __name__ == '__main__':
    unittest.main()
