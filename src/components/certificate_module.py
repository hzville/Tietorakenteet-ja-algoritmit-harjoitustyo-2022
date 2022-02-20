import hashlib, json

class CertificateModule:
    ''' Luokka, jolla luodaan ja allekirjoitetaan Opiskelijapassi'''

    def create_new_certificate(self, 
    certificate_name,
    certificate_academy,
    certificate_student_number,
    certificate_validity,
    certificate_key):
        ''' Pyytää käyttäjältä tarvittavat tiedot kuten opiskelijan nimen, oppilaitoksen, 
            opiskelijanumeron ja passin voimassaoloajan. Luo näiden perusteella uuden dokumentin juurikansioon
            sekä allekirjoittaa dokumentin käyttäjän valitsemalla avaimella.
            Args:
                certificate_name: opiskelijan nimi,
                certificate_academy: oppilaitos,
                certificate_student_number: opiskelijanumero,
                certificate_validity: passin voimassaolo,
                certificate_key: avain jolla passi allekirjoitetaan.
        '''
        json_object = {
            "Opiskelijapassi":[  
                {"Nimi": certificate_name.lower()},
                {"Oppilaitos": certificate_academy.lower()},
                {"Opiskelijanumero": certificate_student_number.lower()},
                {"Voimassaolo":certificate_validity.lower()}],
            "Allekirjoitus":""
            }

        with open(certificate_name.lower(), 'w') as new_certificate:
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
                json_data = json.load(open('./keys/'+key_name.lower(), 'rb'))
                return (json_data['KeyPair'][1])
        except:
            print('Avainta ei löytynyt')


    def get_private_key(self, key_name):
        '''Etsii yksityisen avaimen halutusta tiedostosta.
            Args: 
                key_name: avaimen nimi
            Returns:
                palauttaa yksityisen avaimen tiedot'''
        try:
                json_data = json.load(open('./keys/'+key_name.lower(), 'rb'))
                return (json_data['KeyPair'][2])
        except:
            print('Avainta ei löytynyt')

    def sign_certificate(self,certificate_name, certificate_key):
        ''' Muodostaa tiivisteen opiskelijapassin datasta ja allekirjoittaa tiivisteen 
            halutulla yksityisellä avaimella. Lisää opiskelijapassiin allekirjoitetun tiivisteen '''
        private_key = self.get_private_key(certificate_key)
        if private_key is not None:
            modulus = private_key['Yksityinen_avain'][0]['modulus']
            exponent = private_key['Yksityinen_avain'][1]['exponent']

            json_data = json.load(open(certificate_name.lower(), 'r'))
            json_data['Allekirjoitus'] = pow(int(hashlib.sha1(str(json_data['Opiskelijapassi']).encode('utf-8')).hexdigest(),16), exponent, modulus)
            json.dump(json_data, open(certificate_name.lower(), 'w'), indent=4)

    def get_encrypted_signature(self, document):
        ''' Etsii opiskelijapassista allekirjoitetun tiivisteen ja palauttaa sen.
        Args:
            document: tiedosto josta allekirjoitusta etsitään
        
        Returns: allekirjoitetun tiivisteen'''
        try:
            json_data = json.load(open(document.lower(), 'rb'))
            return json_data['Allekirjoitus']
        except:
            print('Virhe, allekirjoitusta ei löytynyt')

    def validate_certificate(self):
        ''' Todentaa allekirjoituksen purkamalla sen julkisella avaimella.
            Varmistaa myös että dokumentti on säilynyt muuttumattomana'''

        document_to_validate = input('Anna Opiskelijapassin nimi: ')
        key_to_use = input('Anna avaimen nimi: ')
        encrypted_signature = self.get_encrypted_signature(document_to_validate)
        public_key = self.get_public_key(key_to_use)


        if encrypted_signature is not None and public_key is not None:
            modulus = public_key['Julkinen_avain'][0]['modulus']
            exponent = public_key['Julkinen_avain'][1]['exponent']
            decrypted_signature = pow(int(encrypted_signature), exponent, modulus)
            
            json_data = json.load(open(document_to_validate.lower(), 'rb'))
            certificate_signature = int(hashlib.sha1(str(json_data['Opiskelijapassi']).encode('utf-8')).hexdigest(),16)

            if certificate_signature == decrypted_signature:
                print('\n Success, cert is valid \n')
            else:
                print('Error: cert is invalid')

        else:
            print('Tarkista Opiskelijapassin ja avaimen nimi\n')