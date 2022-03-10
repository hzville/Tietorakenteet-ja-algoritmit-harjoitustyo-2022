import os
from tkinter.ttk import Label, Frame, Button, Entry
from tkinter import StringVar, constants, filedialog
from components.certificate_module import CertificateModule

class NewCertificateView: #pylint: disable=too-many-instance-attributes

    def __init__(self, root, create_main_view):
        self.frame = Frame(master=root)
        self.create_main_view = create_main_view
        self.certificate_module = CertificateModule()
        self.name_var = StringVar()
        self.academy_var = StringVar()
        self.student_number_var = StringVar()
        self.validity_var = StringVar()
        self.key_path = None
        self.file_label = Label(master=self.frame)
        self.open_file_button = None
        self.info_label = Label(master=self.frame)
        self.initialize()

    def initialize(self):
        self.create_labels()
        self.create_buttons()
        self.create_inputs()

    def create_labels(self):
        Label(master=self.frame,text='Anna opiskelijan tiedot').grid(
            row=1, column=1, padx=5, pady=5)
        Label(master=self.frame, text='Nimi:').grid(
            row=2, padx=5, pady=5)
        Label(master=self.frame, text='Oppilaitos:').grid(
            row=3, padx=5, pady=5)
        Label(master=self.frame, text='Opiskelijanumero:').grid(
            row=4, padx=5, pady=5)
        Label(master=self.frame, text='Voimassaolo:').grid(
            row=5, padx=5, pady=5)
        Label(master=self.frame, text='Avain:').grid(
            row=6, padx=5, pady=5)
        self.info_label.grid(row=7, column=1, padx=5, pady=5)

    def create_buttons(self):
        Button(master=self.frame, text='Luo uusi Opiskelijapassi',
            command=self.create_new_certificate).grid(row=8, column=0, padx=5, pady=5)
        Button(master = self.frame, text='Takaisin päävalikkon',
            command=self.create_main_view).grid(row=8, column=2, padx=5, pady=5)
        self.open_file_button = Button(master=self.frame, text='Valitse avain',
                                    command=self.choose_key)
        self.open_file_button.grid(row=6, column=1, padx=5, pady=5)

    def create_inputs(self):
        Entry(master=self.frame, textvariable=self.name_var).grid(
            row=2, column=1, padx=5, pady=5)
        Entry(master=self.frame, textvariable=self.academy_var).grid(
            row=3, column=1, padx=5, pady=5)
        Entry(master=self.frame, textvariable=self.student_number_var).grid(
            row=4, column=1, padx=5, pady=5)
        Entry(master=self.frame, textvariable=self.validity_var).grid(
            row=5, column=1, padx=5, pady=5)

    def choose_key(self):
        self.key_path = filedialog.askopenfilename(initialdir='./')
        self.open_file_button.grid(row=6, column=2, padx=5, pady=5)
        self.file_label.configure(text=os.path.basename(self.key_path))
        self.file_label.grid(row=6, column=1, padx=5, pady=5)

    def create_new_certificate(self):
        entry_checker = []
        entry_checker.append(self.name_var.get())
        entry_checker.append(self.academy_var.get())
        entry_checker.append(self.student_number_var.get())
        entry_checker.append(self.validity_var.get())
        entry_checker.append(self.key_path)

        if all(entry_checker):
            self.certificate_module.create_new_certificate(
                self.name_var.get(),
                self.academy_var.get(),
                self.student_number_var.get(),
                self.validity_var.get(),
                self.key_path
            )
            self.info_label.config(text='Uusi opiskelijapassi luotu')
        else:
            self.info_label.config(text='Tietoja puuttuu, täytä kaikki kentät')

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
