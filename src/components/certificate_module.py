import hashlib, json, os

class CertificateModule:
    ''' Luokka jolla luodaan ja allekirjoitetaan opiskelijapassi'''

    def create_new_certificate(self,
    name,
    academy,
    student_number,
    validity,
    key_path):
        ''' Luo uuden opiskelijapassin annettujen parametrien perusteella.
            Opiskelijapassi sijoitetaan opiskelijapassit kansion sisään ja 
            allekirjoitetaan käyttäjän valitsemalla
            avaimella.
            Args:
                name: opiskelijan nimi,
                academy: oppilaitos,
                student_number: opiskelijanumero,
                validity: passin voimassaolo,
                key_path: avain jolla passi allekirjoitetaan.
        '''
        json_object = {
            "opiskelijapassi":{
                "nimi": name.lower(),
                "oppilaitos": academy.lower(),
                "opiskelijanumero": student_number.lower(),
                "voimassaolo":validity.lower()
                },
            "allekirjoitus":""
            }

        if not os.path.isdir('opiskelijapassit'):
            os.mkdir('opiskelijapassit')

        with open('opiskelijapassit/'+name.lower(), 'w') as new_certificate:
            new_certificate.write(json.dumps(json_object, indent=4))
        new_certificate.close()
        self.sign_certificate(name, key_path)

    def get_public_key(self, key_path):
        '''Etsii julkisen avaimen halutusta tiedostosta.
            Args:
                key_path: avaimen sijainti
            Returns:
                palauttaa julkisen avaimen tiedot'''
        try:
            json_data = json.load(open(key_path, 'rb'))
            return json_data['key_pair']['public_key']
        except:
            return 'Avainta ei löytynyt'


    def get_private_key(self, key_path):
        '''Etsii yksityisen avaimen halutusta tiedostosta.
            Args:
                key_path: avaimen sijainti
            Returns:
                palauttaa yksityisen avaimen tiedot'''
        try:
            json_data = json.load(open(key_path, 'rb'))
            return json_data['key_pair']['private_key']
        except:
            return 'Avainta ei löytynyt'

    def sign_certificate(self, name, key_path):
        ''' Muodostaa tiivisteen opiskelijapassin datasta ja allekirjoittaa tiivisteen
            halutulla yksityisellä avaimella. Lisää opiskelijapassiin allekirjoitetun tiivisteen
            Args:
                name: opiskelijapassin nimi,
                key_path: avaimen sijainti, jolla opiskelijapassi allekirjoitetaan'''

        private_key = self.get_private_key(key_path)
        if private_key is not None:
            modulus = private_key['modulus']
            exponent = private_key['exponent']
            json_data = json.load(open('./opiskelijapassit/'+name.lower(), 'r'))
            json_data['allekirjoitus'] = pow(int(hashlib.sha1(str(json_data['opiskelijapassi'])
            .encode('utf-8')).hexdigest(),16), exponent, modulus)
            json.dump(json_data, open('./opiskelijapassit/'+name.lower(), 'w'), indent=4)

    def get_encrypted_signature(self, certificate_path):
        ''' Etsii opiskelijapassista allekirjoitetun tiivisteen ja palauttaa sen.
        Args:
            certificate_path: tiedosto mistä allekirjoitusta etsitään

        Returns: allekirjoitetun tiivisteen'''
        try:
            json_data = json.load(open(certificate_path, 'rb'))
            return json_data['allekirjoitus']
        except:
            return 'Virhe, allekirjoitusta ei löytynyt'

    def validate_certificate(self, certificate_path, key_to_use):
        ''' Todentaa opiskelijapassin allekirjoituksen purkamalla sen julkisella avaimella.
            Varmistaa myös että dokumentti on säilynyt muuttumattomana
        Args:
            certificate_path: tarkistettava opiskelijapassin sijainti
            key_to_use: tarkistukseen käytettävä julkisen avaimen sijainti
        Returns:
            True: jos opiskelijapassin purettu allekirjoitus täsmää opiskelijapassin tietoihin.
            False: jos opiskelijapassin purettu allekirjoitus ei täsmää opiskelijan tietoihin.
            '''
        encrypted_signature = self.get_encrypted_signature(certificate_path)
        public_key = self.get_public_key(key_to_use)

        if encrypted_signature is not None and public_key is not None:
            modulus = public_key['modulus']
            exponent = public_key['exponent']
            decrypted_signature = pow(int(encrypted_signature), exponent, modulus)

            json_data = json.load(open(certificate_path, 'rb'))
            certificate_signature = int(hashlib.sha1(str(json_data['opiskelijapassi'])
                .encode('utf-8')).hexdigest(),16)

            return certificate_signature == decrypted_signature

        return 'Tarkista Opiskelijapassin ja avaimen nimi\n'
