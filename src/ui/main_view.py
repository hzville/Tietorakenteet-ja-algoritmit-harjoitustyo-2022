from tkinter import ttk, constants, PhotoImage
from tkinter.ttk import Button, Label

class MainView:
    ''' Luo uuden päävalikon
    Attributes:
        self.root: kehyksen juurikomponentti
        self.frame: kehys näkymän näyttämiseen
        self.certificate_view: uuden opiskelijapassin näkymä
        self.rsakey_view: uuden RSA-avaimen näkymä
        self.validation_view: opiskelijapassin tarkistusnäkymä
        self.opiskelijapassi_img: päävalikon kuva
    '''

    def __init__(self, root, certificate_view, rsakey_view, validation_view ):
        self.root = root
        self.frame = None
        self.certificate_view = certificate_view
        self.rsakey_view = rsakey_view
        self.validation_view = validation_view
        self.opiskelijapassi_img = PhotoImage(file='./src/ui/images/opiskelijapassi_cut.png')
        self.initialize()

    def initialize(self):
        '''Luo tarvittavat komponentit näkymään'''
        self.frame = ttk.Frame(master = self.root)

        image_label = Label(master = self.frame, image=self.opiskelijapassi_img)

        image_label.pack()

        new_certificate_button = Button(master = self.frame, text = 'Luo uusi Opiskelijapassi'
                                        ,command=self.certificate_view)
        new_certificate_button.pack(pady=10)


        validate_certificate_button = Button(master = self.frame, text = 'Tarkista Opiskelijapassi',
                                        command=self.validation_view)
        validate_certificate_button.pack(pady=10)

        new_key_button = Button(master = self.frame, text = 'Luo uusi avainpari',
                            command=self.rsakey_view)
        new_key_button.pack(pady=10)

    def pack(self):
        '''Näkymän asettelu/alustus'''
        self.frame.pack(fill=constants.X)

    def destroy(self):
        '''Näkymän tuhoaminen'''
        self.frame.destroy()
