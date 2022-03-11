class Key:
    ''' Luokka, jolla luodaan avain.
    Attributes:
        modulus:  avaimen modulaarinen arvo, tarvittava laskennallinen arvo
        exponent: avaimen eksponentti, tarvittava laskennallinen arvo'''

    def __init__(self, modulus, exponent):
        '''Konstruktori joka luo uuden avaimen.
        Asettaa modulaarin ja exponentin arvon'''
        self.modulus = modulus
        self.exponent = exponent

    def get_modulus(self):
        ''' Palauttaa avaimen modulaarisen arvon
        Returns: avaimen modulaarinen arvo'''
        return self.modulus

    def get_exponent(self):
        ''' Palauttaa avaimen eksponentin arvon
        Returns: avaimen eksponentin arvo'''
        return self.exponent
