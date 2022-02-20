from components.rsa_key_generator import RsaKeyGenerator
from components.certificate_module import CertificateModule
from tests.test_data.list_of_composite_numbers import list_of_composite_numbers
from tests.test_data.list_of_primes import list_of_primes
from tkinter import Tk
from ui.ui import Ui

def main():

        window = Tk()
        window.geometry("600x600")
        window.title('Opiskelijapassi')
        ui = Ui(window)
        ui.start()
        window.mainloop()

if __name__ == "__main__":
    main()
 