import os, json
from tkinter.ttk import Label, Frame, Button
from tkinter import constants, filedialog
from components.certificate_module import CertificateModule

class NewValidationView: #pylint: disable=too-many-instance-attributes

    def __init__(self, root, create_main_view):
        self.root = root
        self.frame = None
        self.create_main_view = create_main_view
        self.certificate_module = CertificateModule()
        self.choose_certificate_button = None
        self.chosen_certificate_label = None
        self.choose_key_button = None
        self.chosen_key_label = None
        self.chosen_certificate_name = None
        self.certificate_data_label = None
        self.result_label = None
        self.key = None
        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)
        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        main_label = Label(master=self.frame, text='Tarkista opiskelijapassi tiedot')
        certificate_label = Label(master=self.frame, text='Opiskelijapassi:')
        key_label = Label(master=self.frame, text='Avain:')
        self.chosen_certificate_label = Label(master=self.frame)
        self.chosen_key_label = Label(master=self.frame)
        self.result_label = Label(master=self.frame)
        self.certificate_data_label = Label(master=self.frame)

        main_label.grid(row=1, column=1)
        certificate_label.grid(row=2, column=0)
        key_label.grid(row=3)


    def create_buttons(self):
        self.choose_certificate_button = Button(master=self.frame, text='Valitse opiskelijapassi',
                                            command=self.choose_certificate)
        self.choose_key_button = Button(master=self.frame, text='Valitse avain',
                                            command=self.choose_key)
        return_main_view_button = Button(master = self.frame, text='Takaisin päävalikkon',
                                command=self.create_main_view)
        check_certificate_button = Button(master=self.frame, text='Tarkista opiskelijapassi',
                                command=self.check_certificate)
        self.choose_certificate_button.grid(row=2, column=1)
        self.choose_key_button.grid(row=3, column=1)
        return_main_view_button.grid(row=4, column=2)
        check_certificate_button.grid(row=4, column=0)


    def choose_certificate(self):
        file_path = filedialog.askopenfilename()
        self.chosen_certificate_name = os.path.basename(file_path)
        self.choose_certificate_button.grid(row=2, column=2)
        self.chosen_certificate_label.configure(text=self.chosen_certificate_name)
        self.chosen_certificate_label.grid(row=2, column=1)

    def choose_key(self):
        file_path = filedialog.askopenfilename()
        self.key = os.path.basename(file_path)
        self.choose_key_button.grid(row=3, column=2)
        self.chosen_key_label.configure(text=self.key)
        self.chosen_key_label.grid(row=3, column=1)

    def check_certificate(self):
        result = self.certificate_module.validate_certificate(self.chosen_certificate_name, self.key) #pylint: disable=line-too-long
        certificate_data = self.get_certificate_data_for_ui(self.chosen_certificate_name) #pylint: disable=line-too-long
        self.certificate_data_label.config(text=certificate_data)
        self.certificate_data_label.grid(row=5, column=0)
        if result:
            self.result_label.config(text='VALID', background='green', font=('Arial',30))
            self.result_label.grid(row=5, column=1)
        else:
            self.result_label.config(text='INVALID', background='red', font=('Arial',30))
            self.result_label.grid(row=5, column=1)

    def get_certificate_data_for_ui(self, certificate):
        try:
            json_data = json.load(open('./opiskelijapassit/'+certificate.lower(), 'rb'))
            parsed_json_data = f'Opiskelijpassin tiedot:\n\nNimi: {json_data["opiskelijapassi"]["nimi"]}\nOppilaitos: {json_data["opiskelijapassi"]["oppilaitos"]}\nOpiskelijanumero: {json_data["opiskelijapassi"]["opiskelijanumero"]}\nVoimassaolo: {json_data["opiskelijapassi"]["voimassaolo"]}' #pylint: disable=line-too-long
            return parsed_json_data
        except:
            return 'Opiskelijapassin dataa ei löytynyt'

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
