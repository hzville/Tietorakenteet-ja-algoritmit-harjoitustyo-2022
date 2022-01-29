import random

class PrimeGenerator:

    ''' Luokka jolla luodaan tarvittavat alkuluvut

    Attributes:
        size: halutun alkuluvun koko biteissä

    '''

    def __init__(self):
        ''' Konstruktori joka luo uuden PrimeGeneraattorin
        Alussa alustetaan alkuluvun koko tyhjäksi.
        '''
        self.size = None

    def get_new_prime(self, size):
        ''' Luo halutun mittaisen alkuluvun.
        Args:
            size: Alkuluvun koko biteissä.
        Returns:
            löydetty alkuluku
        '''
        self.size = size

        while True:
            prime_candidate = self.generate_random_number(self.size)

            if self.check_if_prime(prime_candidate):
                return prime_candidate


    def generate_random_number(self, size):
        ''' Luo satunnaisen numeron annetun pituuden mukaan
        Args:
            size: halutun luvun pituus biteissä
        Returns:
            satunnaisen luvun halutulla pituudella
        '''
        return random.getrandbits(size)

    def check_if_prime(self, prime_candidate):
        ''' Tarkistaa onko annettu luku alkuluku
        Args:
            prime_candidate: tarkistettava luku
        Returns:
            True jos luku on alkuluku
            False jos luku ei ole alkuluku
        '''

        if prime_candidate == 2:
            return True

        if prime_candidate % 2 == 0:
            return False

        return True
