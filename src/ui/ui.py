from ui.new_certificate_view import NewCertificateView
from ui.new_certificate_view import NewCertificateView
from ui.main_view import MainView
from ui.new_rsakey_view import NewRsaKeyView

class Ui:

    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self.create_main_view()

    def create_main_view(self):
        self.hide_current_view()

        self.current_view = MainView(self.root, 
            self.show_new_certificate_view,
            self.show_new_rsakey_view)

        self.current_view.pack()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_new_certificate_view(self):
        self.hide_current_view()
        self.current_view = NewCertificateView(self.root, self.create_main_view)
        self.current_view.pack()

    def show_new_rsakey_view(self):
        self.hide_current_view()
        self.current_view = NewRsaKeyView(self.root, self.create_main_view)
        self.current_view.pack()
    