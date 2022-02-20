from asyncio import constants
from tkinter import ttk, constants
from tkinter.ttk import Button

class MainView:

    def __init__(self, root, certificate_view, rsakey_view):
        self.root = root
        self.frame = None
        self.certificate_view = certificate_view
        self.rsakey_view = rsakey_view
        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
    

    def initialize(self):
        self.frame = ttk.Frame(master = self.root)
        new_certificate_button = Button(master = self.frame, text = 'Luo uusi Opiskelijapassi' 
                                        ,command=self.certificate_view)
        new_certificate_button.grid(row = 1)
        
        validate_certificate_button = Button(master = self.frame, text = 'Tarkista Opiskelijapassi') 
        validate_certificate_button.grid(row = 2)


        new_key_button = Button(master = self.frame, text = 'Luo uusi avainpari',
                            command=self.rsakey_view) 
        new_key_button.grid(row = 3)