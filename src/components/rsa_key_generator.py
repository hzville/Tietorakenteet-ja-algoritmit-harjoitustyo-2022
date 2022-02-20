import math, os, json
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
        ''' Luo tarvittavat avainparit salaukseen
        Returns: palauttaa julkisen ja yksityisen avaimen'''
        self.first_prime = self.prime_generator.get_new_prime(int(self.prime_size))
        self.second_prime = self.prime_generator.get_new_prime(int(self.prime_size))
        if self.first_prime != self.second_prime:
            self.modulus = self.first_prime * self.second_prime
            public_key = self.generate_public_key()
            private_key = self.generate_private_key()
            self.save_key_pair(public_key, private_key, key_name)
            return public_key, private_key
        else:
            print('Virhe, avaimien luonti ei onnistunut')

    def generate_public_key(self):
        ''' Luo julkisen avaimen
        Returns: palauttaa julkisen avaimen PublicKey oliona'''
        return PublicKey(self.modulus, self.public_key_exponent)

    def generate_private_key(self):
        ''' Luo yksityisen avaimen
        Returns: palauttaa yksityisen avaimen PrivateKey oliona'''
        return PrivateKey(self.modulus, pow(self.public_key_exponent, -1, ((self.first_prime-1) * (self.second_prime -1))//math.gcd(self.first_prime - 1 , self.second_prime - 1)))
    
    def save_key_pair(self, public_key, private_key, key_name):
        ''' Tallentaa muodostetun avainparin kansion "keys" sisälle.
            Args: 
                public_key: julkinen avain
                private_key: yksityinen avain
                key_name: avainparin haluttu nimi '''
        if not os.path.isdir('keys'):
            os.mkdir('keys')
            
        json_object = {'KeyPair':[
            {"Avainten_nimi": key_name},
            {"Julkinen_avain": [
                {"modulus": public_key.get_modulus()},
                {"exponent": public_key.get_exponent()}
                ]},
            {"Yksityinen_avain": [
                {"modulus": private_key.get_modulus()},
                {"exponent": private_key.get_exponent()}
                ]}
        ]}

        with open('./keys/'+key_name.lower(), 'w') as new_file:
            new_file.write(json.dumps(json_object, indent=4))
        new_file.close()
