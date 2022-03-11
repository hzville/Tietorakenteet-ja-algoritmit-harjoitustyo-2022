from tkinter.ttk import Label, Frame, Button, Entry
from tkinter import StringVar, constants
from components.rsa_key_generator import RsaKeyGenerator

class NewRsaKeyView:
    ''' Luo uuden RSA-avaimen luomiseen käytettävän näkymän
    Attributes:
        self.frame: kehys näkymän näyttämiseen,
        self.create_main_view: päävalikon näkymä
        self.key_name_var: syötekentän arvo
        self.rsa_key_module: avaimien luomiseen käytettävä RsaKeyGenerator moduuli
        self.key_info_label = ilmoitus/virheviestien tekstikomponentti 
    '''
    def __init__(self, root, create_main_view):
        self.frame = Frame(master=root)
        self.create_main_view = create_main_view
        self.key_name_var = StringVar()
        self.rsa_key_module = RsaKeyGenerator()
        self.key_info_label = Label(master=self.frame)
        self.initialize()

    def initialize(self):
        '''Luo tarvittavat komponentit näkymään'''
        self.create_labels()
        self.create_inputs()


    def create_labels(self):
        '''Luo tarvittavat tekstikomponentit'''
        Label(master=self.frame, text='Luo uusi RSA-avainpari').grid(
            row=1, column=1, padx=5, pady=5)
        Label(master=self.frame, text='Avaimen nimi:').grid(row=2, padx=5, pady=5)
        Button(master=self.frame, text='Luo uusi RSA-avainpari',
            command=self.create_new_rsakey).grid(row=5, column=0, padx=5, pady=5)
        Button(master = self.frame, text='Takaisin päävalikkoon',
            command=self.create_main_view).grid(row=5, column=2, padx=5, pady=5)
        self.key_info_label.grid(row=4, column=1, padx=5, pady=5)

    def create_inputs(self):
        '''Luo tarvittavat syötekomponentit'''
        Entry(master=self.frame, textvariable=self.key_name_var).grid(
            row=2, column=1, padx=5, pady=5)

    def create_new_rsakey(self):
        '''Luo uuden RSA-avainparin'''
        if self.key_name_var.get():
            self.rsa_key_module.generate_new_key(self.key_name_var.get())
            self.key_info_label.config(text='Uusi avainpari luotu')
        else:
            self.key_info_label.config(text='Syötä uuden avaimen nimi')

    def pack(self):
        '''Näkymän asettelu/alustus'''
        self.frame.pack(fill=constants.X)

    def destroy(self):
        '''Näkymän tuhoaminen'''
        self.frame.destroy()
