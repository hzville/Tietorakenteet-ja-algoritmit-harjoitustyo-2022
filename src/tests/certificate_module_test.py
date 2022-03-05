import unittest, json, os
from components.certificate_module import CertificateModule
from components.rsa_key_generator import RsaKeyGenerator

class TestCertificateModule(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.certificate_module = CertificateModule()
        self.rsa_key_generator = RsaKeyGenerator()
        self.name = 'test_person'
        self.academy = 'test academy'
        self.student_number = 'test studet number'
        self.validity = 'test validity'
        self.key_name = 'test-key'
        self.path = './opiskelijapassit/'
        self.certificate_key = self.rsa_key_generator.generate_new_key(self.key_name)
        self.test_certificate = self.certificate_module.create_new_certificate(
            self.name,
            self.academy,
            self.student_number,
            self.validity,
            self.key_name
        )

    @classmethod
    def tearDownClass(self):
        os.remove(self.path+'/'+self.name)
        os.remove('./keys/private_keys/wrong-key')
        os.remove('./keys/public_keys/wrong-key')
        os.remove('./keys/private_keys/test-key')
        os.remove('./keys/public_keys/test-key')

    def test_create_new_certificate(self):
        with open(self.path+self.name.lower(), 'r') as new_file:
            self.assertNotEqual(new_file, None)
    
    def test_certificate_contains_correct_data(self):
        with open(self.path+self.name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
            self.assertEqual(json_data['opiskelijapassi']['nimi'], self.name)
            self.assertEqual(json_data['opiskelijapassi']['oppilaitos'], self.academy)
            self.assertEqual(json_data['opiskelijapassi']['opiskelijanumero'], self.student_number)
            self.assertEqual(json_data['opiskelijapassi']['voimassaolo'], self.validity)
            self.assertNotEqual(json_data['allekirjoitus'], None)
            new_file.close()
    
    def test_certificate_signature_is_valid(self):
        result = self.certificate_module.validate_certificate(self.name, self.key_name)
        self.assertTrue(result)
    
    def test_certificate_signature_is_invalid_with_wrong_key(self):
        invalid_key_name = 'wrong-key'
        self.rsa_key_generator.generate_new_key(invalid_key_name)
        result = self.certificate_module.validate_certificate(self.name, invalid_key_name)
        self.assertFalse(result)
