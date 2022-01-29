from components.prime_generator import PrimeGenerator

def main():

    prime_generator = PrimeGenerator()
    while True:
        print('Valitse komento :')
        print('1 : Alkuluvun luonti')
        print('2 : Lopeta')
        command = input('Komento: ')


        if int(command) == 1:
            size = input('Anna alkuluvun haluttu pituus biteissä: ')
            print('alkuluku oli: ', prime_generator.get_new_prime(int(size)))

        if int(command) == 2:
            print('Kiitos ja näkemiin!')
            break

if __name__ == "__main__":
    main()
