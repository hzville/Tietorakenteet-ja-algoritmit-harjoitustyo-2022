import unittest
from components.rsa_key_generator import RsaKeyGenerator

class TestRsaGenerator(unittest.TestCase):
    def setUp(self):
        self.rsa_key_generator = RsaKeyGenerator()
        self.public_key = None
        self.private_key = None

    def test_generate_new_key(self):
        self.public_key, self.private_key = self.rsa_key_generator.generate_new_key()
        self.assertNotEqual(self.public_key, None)
        self.assertNotEqual(self.private_key, None)
        self.assertNotEqual(self.public_key.get_modulus(), None)
        self.assertNotEqual(self.public_key.get_exponent(), None)
        self.assertNotEqual(self.private_key.get_modulus(), None)
        self.assertNotEqual(self.private_key.get_exponent(), None)