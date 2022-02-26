import math, os, json #pylint: disable=multiple-imports
from components.prime_generator import PrimeGenerator
from components.public_key import PublicKey
from components.private_key import PrivateKey


class RsaKeyGenerator:
    ''' Luokka jolla luodaan RSA-salauksen avainparit

    Attributes:
        prime_generator: alkulukujen luomiseen tarvittava moduuli
        prime_size: halutun alkuluvun koko biteissä
        first_prime: ensimmäinen tarvittava alkuluku
        second_prime: toinen tarvittava alkuluku
        modulus: salauksessa tarvittava luku
        public_key_exponent: julkisen avaimen eksponentti, yksi yleisesti käytetty luku on 65537'''

    def __init__(self):
        ''' Konstruktori joka luo uuden RsaKeyGeneraattorin.
        Alussa alustetaan tarvittavat muuttujat'''
        self.prime_generator = PrimeGenerator()
        self.prime_size = 512
        self.first_prime = None
        self.second_prime = None
        self.modulus = None
        self.public_key_exponent = 65537

    def generate_new_key(self, key_name):
        ''' Luo tarvittavat avainparit salaukseen, palauttaa julkisen ja yksityisen avaimen
        Args:
            key_name: avaimen nimi
        Returns:
            public_key: julkinen avain
            private_key: yksityisen avain'''
        while self.first_prime == self.second_prime:
            self.first_prime = self.prime_generator.get_new_prime(int(self.prime_size))
            self.second_prime = self.prime_generator.get_new_prime(int(self.prime_size))
            if self.first_prime != self.second_prime:
                self.modulus = self.first_prime * self.second_prime
                public_key = PublicKey(self.modulus, self.public_key_exponent)
                private_key = self.generate_private_key()
                self.save_key_pair(public_key, private_key, key_name)
            else:
                print('Virhe, avaimien luonti ei onnistunut')
        return public_key, private_key

    def generate_private_key(self):
        ''' Luo yksityisen avaimen
        Returns: palauttaa yksityisen avaimen PrivateKey oliona'''
        key_lambda = (self.first_prime-1) * (self.second_prime-1)//math.gcd(self.first_prime-1 , self.second_prime-1) #pylint: disable=line-too-long
        private_key_exponent = pow(self.public_key_exponent, -1, key_lambda)
        return PrivateKey(self.modulus, private_key_exponent)

    def save_key_pair(self, public_key, private_key, key_name):
        ''' Luo tarvittavat kansiot tallentaa muodostetun avainparin kansion "keys" sisälle.
            Args:
                public_key: julkinen avain
                private_key: yksityinen avain
                key_name: avainparin haluttu nimi '''
        self.create_directorys_and_files()

        json_private_key = {'KeyPair':[
            {"Key_name": key_name},
            {"Public_key": [
                {"modulus": public_key.get_modulus()},
                {"exponent": public_key.get_exponent()}
                ]},
            {"Private_key": [
                {"modulus": private_key.get_modulus()},
                {"exponent": private_key.get_exponent()}
                ]}
        ]}

        json_public_key = {'KeyPair':[
            {"Key_name": key_name},
            {"Public_key": [
                {"modulus": public_key.get_modulus()},
                {"exponent": public_key.get_exponent()}
                ]}
        ]}

        with open('./keys/private_keys/'+key_name.lower(), 'w') as new_file:
            new_file.write(json.dumps(json_private_key, indent=4))
        new_file.close()

        with open('./keys/public_keys/'+key_name.lower(), 'w') as new_file:
            new_file.write(json.dumps(json_public_key, indent=4))
        new_file.close()

    def create_directorys_and_files(self):
        '''Luo tarvittavat kansiot avaimille'''
        if not os.path.isdir('keys'):
            os.mkdir('keys')

        if not os.path.isdir('./keys/private_keys'):
            os.mkdir('keys/private_keys')

        if not os.path.isdir('./keys/public_keys'):
            os.mkdir('keys/public_keys')
