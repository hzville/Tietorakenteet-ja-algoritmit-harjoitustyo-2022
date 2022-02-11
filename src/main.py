from components.rsa_key_generator import RsaKeyGenerator
from components.certificate_module import CertificateModule
from tests.test_data.list_of_composite_numbers import list_of_composite_numbers
from tests.test_data.list_of_primes import list_of_primes

def main():

    rsa_key_generator = RsaKeyGenerator()
    certificate_module = CertificateModule()
    
    while True:
        print('Valitse komento :')
        print('1 : Luo uusi Opiskelijapassi')
        print('2 : Lopeta')
        command = input('Valinta: ')


        if int(command) == 1:
            
            new_cert = certificate_module.create_new_certificate()
            public_key, private_key = rsa_key_generator.generate_new_key()
            certificate_module.sign_certificate(new_cert, private_key)

        if int(command) == 2:
            print('Kiitos ja näkemiin!')
            break

if __name__ == "__main__":
    main()
 