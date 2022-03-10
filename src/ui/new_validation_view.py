import os, json
from tkinter.ttk import Label, Frame, Button
from tkinter import constants, filedialog
from components.certificate_module import CertificateModule

class NewValidationView: #pylint: disable=too-many-instance-attributes

    def __init__(self, root, create_main_view):
        self.frame = Frame(master=root)
        self.create_main_view = create_main_view
        self.certificate_module = CertificateModule()
        self.choose_certificate_button = None
        self.certificate_label = Label(master=self.frame)
        self.choose_key_button = None
        self.key_label = Label(master=self.frame)
        self.certificate_data_label = Label(master=self.frame)
        self.result_label = Label(master=self.frame)
        self.result_label.grid(row=5, column=1, padx=5, pady=5)
        self.info_label = Label(master=self.frame)
        self.certificate = None
        self.key = None
        self.initialize()

    def initialize(self):
        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        Label(master=self.frame, text='Tarkista opiskelijapassi tiedot').grid(
            row=1, column=1, padx=5, pady=5)
        Label(master=self.frame, text='Opiskelijapassi:').grid(
            row=2, column=0, padx=5, pady=5)
        Label(master=self.frame, text='Avain:').grid(
            row=3, padx=5, pady=5)

    def create_buttons(self):
        self.choose_certificate_button = Button(master=self.frame, text='Valitse opiskelijapassi',
                                            command=self.choose_certificate)
        self.choose_certificate_button.grid(row=2, column=1, padx=5, pady=5)
        self.choose_key_button = Button(master=self.frame, text='Valitse avain',
                                            command=self.choose_key)
        self.choose_key_button.grid(row=3, column=1, padx=5, pady=5)
        Button(master = self.frame, text='Takaisin päävalikkon',
            command=self.create_main_view).grid(row=4, column=2, padx=5, pady=5)
        Button(master=self.frame, text='Tarkista opiskelijapassi',
            command=self.check_certificate).grid(row=4, column=0, padx=5, pady=5)

    def choose_certificate(self):
        self.certificate = filedialog.askopenfilename(initialdir='./')
        self.choose_certificate_button.grid(row=2, column=2, padx=5, pady=5)
        self.certificate_label.configure(text=os.path.basename(self.certificate))
        self.certificate_label.grid(row=2, column=1, padx=5, pady=5)

    def choose_key(self):
        self.key = filedialog.askopenfilename(initialdir='./')
        self.choose_key_button.grid(row=3, column=2, padx=5, pady=5)
        self.key_label.configure(text=os.path.basename(self.key))
        self.key_label.grid(row=3, column=1, padx=5, pady=5)

    def check_certificate(self):
        if self.certificate and self.key:
            result = self.certificate_module.validate_certificate(self.certificate, self.key)
            certificate_data = self.get_certificate_data_for_ui(self.certificate)
            self.certificate_data_label.config(text=certificate_data)
            self.certificate_data_label.grid(row=6, column=1, padx=5, pady=5)

            if result:
                self.result_label.config(text='Passi on kelvollinen', background='green',
                font=('Arial',30))
            else:
                self.result_label.config(text='Passi on virheellinen',
                    background='red', font=('Arial',30))
        else:
            self.result_label.config(text='Valitse opiskelijapassi ja avain',
                background='#F0F0F0', font=('Arial',12))

    def get_certificate_data_for_ui(self, certificate):
        try:
            json_data = json.load(open(certificate, 'rb'))
            parsed_json_data = f'Opiskelijpassin tiedot:\n\nNimi: {json_data["opiskelijapassi"]["nimi"]}\nOppilaitos: {json_data["opiskelijapassi"]["oppilaitos"]}\nOpiskelijanumero: {json_data["opiskelijapassi"]["opiskelijanumero"]}\nVoimassaolo: {json_data["opiskelijapassi"]["voimassaolo"]}' #pylint: disable=line-too-long
            return parsed_json_data
        except:
            return 'Opiskelijapassin dataa ei löytynyt'

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
