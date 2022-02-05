from components.prime_generator import PrimeGenerator
from tests.test_data.list_of_composite_numbers import list_of_composite_numbers
from tests.test_data.list_of_primes import list_of_primes

def main():

    prime_generator = PrimeGenerator()
    
    while True:
        print('Valitse komento :')
        print('1 : Alkuluvun luonti')
        print('2 : Lopeta')
        command = input('Komento: ')


        if int(command) == 1:
            size = input('Anna alkuluvun haluttu pituus biteissä: ')
            print('Alkuluku oli: ', prime_generator.get_new_prime(int(size)))

        if int(command) == 2:
            print('Kiitos ja näkemiin!')
            break

if __name__ == "__main__":
    main()
