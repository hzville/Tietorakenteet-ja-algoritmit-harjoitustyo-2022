import unittest, json
from components.certificate_module import CertificateModule

class TestCertificateModule(unittest.TestCase):
    def setUp(self):
        self.certificate_module = CertificateModule()
        self.name = 'test_person'
        self.academy = 'test academy'
        self.student_number = 'test studet number'
        self.certificate_validity = 'test validity'
        self.certificate_key = 'test-key'
        self.certificate_path = './opiskelijapassit/'

    def test_create_new_certificate(self):
        self.certificate_module.create_new_certificate(
            self.name,
            self.academy,
            self.student_number,
            self.certificate_validity,
            self.certificate_key
        )
        with open(self.certificate_path+self.name.lower(), 'r') as new_file:
            self.assertNotEqual(new_file, None)
    
    def test_certificate_contains_correct_data(self):
        self.certificate_module.create_new_certificate(
            self.name,
            self.academy,
            self.student_number,
            self.certificate_validity,
            self.certificate_key
        )
        with open(self.certificate_path+self.name.lower(), 'r') as new_file:
            json_data = json.load(new_file)
            self.assertEqual(json_data['Opiskelijapassi'][0]['Nimi'], self.name)
            self.assertEqual(json_data['Opiskelijapassi'][1]['Oppilaitos'], self.academy)
            self.assertEqual(json_data['Opiskelijapassi'][2]['Opiskelijanumero'], self.student_number)
            self.assertEqual(json_data['Opiskelijapassi'][3]['Voimassaolo'], self.certificate_validity)
            self.assertNotEqual(json_data['Allekirjoitus'], None)

