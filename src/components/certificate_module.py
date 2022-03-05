import hashlib, json, os

class CertificateModule:
    ''' Luokka jolla luodaan ja allekirjoitetaan Opiskelijapassi'''

    def create_new_certificate(self,
    certificate_name,
    certificate_academy,
    certificate_student_number,
    certificate_validity,
    certificate_key):
        ''' Pyytää käyttäjältä tarvittavat tiedot kuten opiskelijan nimen, oppilaitoksen,
            opiskelijanumeron ja passin voimassaoloajan. Luo näiden perusteella uuden
            dokumentin juurikansioon sekä allekirjoittaa dokumentin käyttäjän valitsemalla
            avaimella.
            Args:
                certificate_name: opiskelijan nimi,
                certificate_academy: oppilaitos,
                certificate_student_number: opiskelijanumero,
                certificate_validity: passin voimassaolo,
                certificate_key: avain jolla passi allekirjoitetaan.
        '''
        json_object = {
            "opiskelijapassi":{
                "nimi": certificate_name.lower(),
                "oppilaitos": certificate_academy.lower(),
                "opiskelijanumero": certificate_student_number.lower(),
                "voimassaolo":certificate_validity.lower()
                },
            "allekirjoitus":""
            }

        if not os.path.isdir('opiskelijapassit'):
            os.mkdir('opiskelijapassit')

        with open('opiskelijapassit/'+certificate_name.lower(), 'w') as new_certificate:
            new_certificate.write(json.dumps(json_object, indent=4))
        new_certificate.close()
        self.sign_certificate(certificate_name, certificate_key)

    def get_public_key(self, key_name):
        '''Etsii julkisen avaimen halutusta tiedostosta.
            Args:
                key_name: avaimen nimi
            Returns:
                palauttaa julkisen avaimen tiedot'''
        try:
            json_data = json.load(open('./keys/public_keys/'+key_name.lower(), 'rb'))
            return json_data['key_pair']['public_key']
        except:
            return 'Avainta ei löytynyt'


    def get_private_key(self, key_name):
        '''Etsii yksityisen avaimen halutusta tiedostosta.
            Args:
                key_name: avaimen nimi
            Returns:
                palauttaa yksityisen avaimen tiedot'''
        try:
            json_data = json.load(open('./keys/private_keys/'+key_name.lower(), 'rb'))
            return json_data['key_pair']['private_key']
        except:
            return 'Avainta ei löytynyt'

    def sign_certificate(self,certificate_name, certificate_key):
        ''' Muodostaa tiivisteen opiskelijapassin datasta ja allekirjoittaa tiivisteen
            halutulla yksityisellä avaimella. Lisää opiskelijapassiin allekirjoitetun tiivisteen
            Args:
                certificate_name: opiskelijapassin nimi,
                certificate_key: avain jolla opiskelijapassi allekirjoitetaan'''

        private_key = self.get_private_key(certificate_key)
        if private_key is not None:
            modulus = private_key['modulus']
            exponent = private_key['exponent']
            json_data = json.load(open('./opiskelijapassit/'+certificate_name.lower(), 'r'))
            json_data['allekirjoitus'] = pow(int(hashlib.sha1(str(json_data['opiskelijapassi'])
            .encode('utf-8')).hexdigest(),16), exponent, modulus)
            json.dump(json_data, open('./opiskelijapassit/'+certificate_name.lower(), 'w'), indent=4) #pylint: disable=line-too-long

    def get_encrypted_signature(self, document):
        ''' Etsii opiskelijapassista allekirjoitetun tiivisteen ja palauttaa sen.
        Args:
            document: tiedosto mistä allekirjoitusta etsitään

        Returns: allekirjoitetun tiivisteen'''
        try:
            json_data = json.load(open('./opiskelijapassit/'+document.lower(), 'rb'))
            return json_data['allekirjoitus']
        except:
            return 'Virhe, allekirjoitusta ei löytynyt'


    def validate_certificate(self, certificate, key_to_use):
        ''' Todentaa opiskelijapassin allekirjoituksen purkamalla sen julkisella avaimella.
            Varmistaa myös että dokumentti on säilynyt muuttumattomana
        Args:
            certificate: tarkistettava opiskelijapassi
            key_to_use: tarkistukseen käytettävä julkinen avain
        Returns:
            True: jos opiskelijapassin purettu allekirjoitus täsmää opiskelijapassin tietoihin.
            False: jos opiskelijapassin purettu allekirjoitus ei täsmää opiskelijan tietoihin.
            '''

        encrypted_signature = self.get_encrypted_signature(certificate)
        public_key = self.get_public_key(key_to_use)

        if encrypted_signature is not None and public_key is not None:
            modulus = public_key['modulus']
            exponent = public_key['exponent']
            decrypted_signature = pow(int(encrypted_signature), exponent, modulus)

            json_data = json.load(open('./opiskelijapassit/'+certificate.lower(), 'rb'))
            certificate_signature = int(hashlib.sha1(str(json_data['opiskelijapassi'])
            .encode('utf-8')).hexdigest(),16)

            return certificate_signature == decrypted_signature

        return 'Tarkista Opiskelijapassin ja avaimen nimi\n'
