from tkinter.ttk import Label, Frame, Button, Entry
from tkinter import StringVar, constants
from components.rsa_key_generator import RsaKeyGenerator

class NewRsaKeyView:

    def __init__(self, root, create_main_view):
        self.root = root
        self.frame = None
        self.create_main_view = create_main_view
        self.key_name_var = StringVar()
        self.rsa_key_module = RsaKeyGenerator()
        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)
        self.create_labels()
        self.create_inputs()


    def create_labels(self):
        main_label = Label(master=self.frame, text='Luo uusi RSA-avainpari')
        name_label = Label(master=self.frame, text='Avaimen nimi:')
        create_new_rsakey_button = Button(master=self.frame, text='Luo uusi RSA-avainpari',
                                        command=self.create_new_rsakey)
        create_main_view_button = Button(master = self.frame, text='Takaisin päävalikkon',
                                    command=self.create_main_view)

        main_label.grid(row=1, column=1, padx=5, pady=5)
        name_label.grid(row=2, padx=5, pady=5)
        create_new_rsakey_button.grid(row=5, column=0, padx=5, pady=5)
        create_main_view_button.grid(row=5, column=2, padx=5, pady=5)

    def create_inputs(self):
        key_name_entry = Entry(master=self.frame, textvariable=self.key_name_var)

        key_name_entry.grid(row=2, column=1, padx=5, pady=5)
    def create_new_rsakey(self):
        self.rsa_key_module.generate_new_key(self.key_name_var.get())
        key_generated_label = Label(master=self.frame, text='Uusi avainpari luotu')
        key_generated_label.grid(row=4, column=1, padx=5, pady=5)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
