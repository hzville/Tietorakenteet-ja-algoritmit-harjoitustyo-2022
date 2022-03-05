import unittest, json, os
from components.rsa_key_generator import RsaKeyGenerator

class TestRsaGenerator(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.rsa_key_generator = RsaKeyGenerator()
        self.public_key = None
        self.private_key = None
        self.key_name = 'rsa_test-key'
        self.private_key_path ='./keys/private_keys/'
        self.public_key_path ='./keys/public_keys/'

    @classmethod
    def tearDownClass(self):
        os.remove(self.private_key_path+self.key_name)
        os.remove(self.public_key_path+self.key_name)

    def test_generate_new_key(self):
        self.rsa_key_generator.generate_new_key(self.key_name)
        with open(self.private_key_path+self.key_name.lower(), 'r') as new_file:
            self.assertNotEqual(new_file, None)
            new_file.close()
        with open(self.public_key_path+self.key_name.lower(), 'r') as new_file:
            self.assertNotEqual(new_file, None)
            new_file.close()

    def test_key_name_is_correct(self):
        with open(self.public_key_path+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
            self.assertEqual(json_data['key_pair']['key_name'], self.key_name)

        with open(self.private_key_path+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
            self.assertEqual(json_data['key_pair']['key_name'], self.key_name)
    
    def test_key_file_has_public_key(self):
        with open(self.public_key_path+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
        self.assertIn('public_key', str(json_data['key_pair']))

    def test_key_file_has_private_key(self):
        with open(self.private_key_path+self.key_name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
        self.assertIn('private_key', str(json_data['key_pair']))


