import hashlib
import json

class CertificateModule:
    ''' Luokka, jolla luodaan ja allekirjoitetaan Opiskelijapassi'''

    def create_new_certificate(self):
        ''' Pyytää käyttäjältä tarvittavat tiedot kuten opiskelijan nimen, oppilaitoksen, 
            opiskelijanumeron ja passin voimassaoloajan. Luo näiden perusteella uuden dokumentin juurikansioon.
        Returns: palauttaa opiskelijapassin.
        '''

        certificate_name = input('Nimi: ')
        certificate_academy = input('Oppilaitos: ')
        certificate_student_number = input('Opiskelijanumero: ')
        certificate_validity = input('Passin voimassaolo: ')

        json_object = {"Opiskelijapassi":[  
            {"Nimi": certificate_name},
            {"Oppilaitos": certificate_academy},
            {"Opiskelijanumero": certificate_student_number},
            {"Voimassaolo":certificate_validity}]}

        with open('opiskelijapassi.txt', 'w') as new_certificate:
            new_certificate.write(json.dumps(json_object, indent=4))
        new_certificate.close()

        return new_certificate

    def sign_certificate(self,certificate, private_key):
        ''' Muodostaa tiivisteen opiskelijapassin datasta ja allekirjoittaa tiivisteen 
            halutulla yksityisellä avaimella. Lisää opiskelijapassiin allekirjoitetun tiivisteen '''
    
        with open('opiskelijapassi.txt', 'rb') as certificate_to_encrypt:
                certificate_signature = int(hashlib.sha1(certificate_to_encrypt.read()).hexdigest(),16)
        
        encyrpted_signature = pow(certificate_signature, private_key.get_exponent(), private_key.get_modulus())
        certificate = open('opiskelijapassi.txt','a')
        certificate.write(f'\nOpiskelijapassin allekirjoitus: {encyrpted_signature}')
        certificate.close()
    
    def get_encrypted_signature(self):
        ''' Etsii opiskelijapassista allekirjoitetun tiivisteen ja palauttaa sen.
        Returns: allekirjoitetun tiivisteen'''
        for line in open('opiskelijapassi.txt').readlines():
            if 'Opiskelijapassin allekirjoitus' in line:
                signature = line.strip('Opiskelijapassin allekirjoitus: ')
                return signature
        print('Virhe, allekirjoitusta ei löytynyt')

    def validate_document(self, signature, public_key):
        ''' Todentaa allekirjoituksen purkamalla sen julkisella avaimella.
            Toteutus kesken.'''
        decrypted_signature = pow(int(signature), public_key.get_exponent(), public_key.get_modulus())

        return False
