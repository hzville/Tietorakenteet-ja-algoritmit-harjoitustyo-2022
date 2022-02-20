import unittest, json
from components.rsa_key_generator import RsaKeyGenerator

class TestRsaGenerator(unittest.TestCase):
    def setUp(self):
        self.rsa_key_generator = RsaKeyGenerator()
        self.public_key = None
        self.private_key = None
        self.key_name = 'test-key'

    def test_generate_new_key(self):
        self.rsa_key_generator.generate_new_key(self.key_name)
        with open('./keys/'+self.key_name.lower(), 'r') as new_file:
            self.assertNotEqual(new_file, None)
            new_file.close()

    def test_key_name_is_correct(self):
        with open('./keys/'+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
            self.assertEqual(json_data['KeyPair'][0]['Avainten_nimi'], self.key_name)
    
    def test_key_file_has_public_key(self):
        with open('./keys/'+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
        self.assertIn('Julkinen_avain', str(json_data['KeyPair'][1]))

    def test_key_file_has_private_key(self):
        with open('./keys/'+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
        self.assertIn('Yksityinen_avain', str(json_data['KeyPair'][2]))