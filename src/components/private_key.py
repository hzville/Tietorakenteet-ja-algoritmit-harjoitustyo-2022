from operator import mod


class PrivateKey:
    ''' Luokka, jolla määritellään yksityinen avain.
    Attributes: 
        modulus:  avaimen modulaarinen arvo, tarvittava laskennallinen arvo
        exponent: avaimen eksponentti, tarvittava laskennallinen arvo'''

    def __init__(self, modulus, exponent):
        '''Konstruktori joka luo uuden yksityisen avaimen. 
        Alustaa modulaarin ja exponentin arvon'''
        self.modulus = modulus
        self.exponent = exponent

    def get_modulus(self):
        ''' Palauttaa avaimen modulaarisen arvon
        Returns: avaimen modulaarisen arvon'''
        return self.modulus
    
    def get_exponent(self):
        ''' Palauttaa avaimen eksponentin arvon
        Returns: avaimen eksponentin arvon'''
        return self.exponent