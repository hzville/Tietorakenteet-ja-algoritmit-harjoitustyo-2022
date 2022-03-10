from tkinter.ttk import Label, Frame, Button, Entry
from tkinter import StringVar, constants
from components.rsa_key_generator import RsaKeyGenerator

class NewRsaKeyView:

    def __init__(self, root, create_main_view):
        self.frame = Frame(master=root)
        self.create_main_view = create_main_view
        self.key_name_var = StringVar()
        self.rsa_key_module = RsaKeyGenerator()
        self.key_info_label = Label(master=self.frame)
        self.initialize()

    def initialize(self):
        self.create_labels()
        self.create_inputs()


    def create_labels(self):
        Label(master=self.frame, text='Luo uusi RSA-avainpari').grid(
            row=1, column=1, padx=5, pady=5)
        Label(master=self.frame, text='Avaimen nimi:').grid(row=2, padx=5, pady=5)
        Button(master=self.frame, text='Luo uusi RSA-avainpari',
            command=self.create_new_rsakey).grid(row=5, column=0, padx=5, pady=5)
        Button(master = self.frame, text='Takaisin päävalikkon',
            command=self.create_main_view).grid(row=5, column=2, padx=5, pady=5)
        self.key_info_label.grid(row=4, column=1, padx=5, pady=5)

    def create_inputs(self):
        Entry(master=self.frame, textvariable=self.key_name_var).grid(
            row=2, column=1, padx=5, pady=5)

    def create_new_rsakey(self):
        if self.key_name_var.get():
            self.rsa_key_module.generate_new_key(self.key_name_var.get())
            self.key_info_label.config(text='Uusi avainpari luotu')
        else:
            self.key_info_label.config(text='Syötä uuden avaimen nimi')

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
