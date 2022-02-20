from tkinter.ttk import Label, Frame, Button, Entry
from tkinter import StringVar, constants
from components.certificate_module import CertificateModule

class NewCertificateView:

    def __init__(self, root, create_main_view):
        self.root = root
        self.frame = None
        self.create_main_view = create_main_view
        self.certificate_module = CertificateModule()
        self.name_var = StringVar()
        self.academy_var = StringVar()
        self.student_number_var = StringVar()
        self.certificate_validity_var = StringVar()
        self.key_var = StringVar()
        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)
        self.create_labels()
        self.create_inputs()
        
    def create_labels(self):
        main_label = Label(master=self.frame, text='Anna opiskelijan tiedot:')
        name_label = Label(master=self.frame, text='Nimi:')
        academy_label = Label(master=self.frame, text='Oppilaitos:')
        student_number_label = Label(master=self.frame, text='Opiskelijanumero:')
        certificate_validity_label = Label(master=self.frame, text='Voimassaolo:')
        key_label = Label(master=self.frame, text='Avain:')
        create_new_certificate_button = Button(master=self.frame, text='Luo uusi Opiskelijapassi',
                                        command=self.create_new_certificate)
        create_main_view_button = Button(master = self.frame, text='Takaisin päävalikkon',
                                    command=self.create_main_view)

        main_label.grid(row=1)
        name_label.grid(row=2)
        academy_label.grid(row=3)
        student_number_label.grid(row=4)
        certificate_validity_label.grid(row=5)
        key_label.grid(row=6)
        create_new_certificate_button.grid(row=7, column=0)
        create_main_view_button.grid(row=7, column=2)

    
    def create_inputs(self):
        name_entry = Entry(master=self.frame, textvariable=self.name_var)
        academy_entry = Entry(master=self.frame, textvariable=self.academy_var)
        student_number_entry = Entry(master=self.frame, textvariable=self.student_number_var)
        certificate_validity_entry = Entry(master=self.frame, textvariable=self.certificate_validity_var)
        key_entry = Entry(master=self.frame, textvariable=self.key_var)


        name_entry.grid(row=2, column=1)
        academy_entry.grid(row=3, column=1)
        student_number_entry.grid(row=4, column=1)
        certificate_validity_entry.grid(row=5, column=1)
        key_entry.grid(row=6, column=1)

    def create_new_certificate(self):
        self.certificate_module.create_new_certificate(
            self.name_var.get(),
            self.academy_var.get(),
            self.student_number_var.get(),
            self.certificate_validity_var.get(),
            self.key_var.get()
        )

    def pack(self):
        self.frame.pack(fill=constants.X)
    
    def destroy(self):
        self.frame.destroy()