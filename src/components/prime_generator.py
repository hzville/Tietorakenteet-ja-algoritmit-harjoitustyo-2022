import random

class PrimeGenerator:
    ''' Luokka jolla luodaan tarvittavat alkuluvut

    Attributes:
        size: halutun alkuluvun koko biteissä'''

    def __init__(self):
        ''' Konstruktori joka luo uuden PrimeGeneraattorin
        Alussa alustetaan alkuluvun koko tyhjäksi.'''
        self.size = None

    def get_new_prime(self, size):
        ''' Luo halutun mittaisen alkuluvun.
        Args:
            size: Alkuluvun koko biteissä.
        Returns:
            löydetty alkuluku'''
        self.size = size

        while True:
            prime_candidate = random.getrandbits(size)

            if self.check_if_prime(prime_candidate):
                return prime_candidate

    def check_if_prime(self, prime_candidate):
        ''' Tarkistaa onko annettu luku alkuluku
        Args:
            prime_candidate: tarkistettava luku
        Returns:
            True jos luku on alkuluku
            False jos luku ei ole alkuluku'''
        accuracy_rounds = 10

        if prime_candidate in [2,3]:
            return True

        if prime_candidate % 2 == 0 or prime_candidate < 2:
            return False

        multiplier = prime_candidate -1
        division_rounds = 0

        while True:
            if multiplier % 2 != 0:
                break
            multiplier //= 2
            division_rounds += 1

        for first_round in range(accuracy_rounds): #pylint: disable=unused-variable
            result = pow(random.randint(2,prime_candidate - 2), multiplier, prime_candidate)
            if result in [1, prime_candidate - 1]:
                continue
            for second_round in range(division_rounds - 1): #pylint: disable=unused-variable
                result = pow(result, 2, prime_candidate)
                if result == prime_candidate -1:
                    break
            else:
                return False
        return True
