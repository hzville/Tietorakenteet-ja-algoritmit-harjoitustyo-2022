from ui.new_certificate_view import NewCertificateView
from ui.main_view import MainView
from ui.new_rsakey_view import NewRsaKeyView
from ui.new_validation_view import NewValidationView

class Ui:
    '''Luo käyttöliittymän ja siihen tarvittavat näkymät
    Args:
        root: TkInterin juurikomponentti
    Attributes:
        self.root: ui luokan juurikomponentti
        self.current_view: näytettävä näkymä
        '''

    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        '''Käynnistää käyttöliittmän ja näyttää päävalikon'''
        self.create_main_view()

    def create_main_view(self):
        '''Näyttää päävalikon'''
        self.hide_current_view()

        self.current_view = MainView(self.root,
            self.show_new_certificate_view,
            self.show_new_rsakey_view,
            self.show_new_validation_view)

        self.current_view.pack()

    def hide_current_view(self):
        '''Hävittää nykyisen näkymän'''
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_new_certificate_view(self):
        '''Näyttää uuden opiskelijapassin luomiseen käytettävää näkymää'''
        self.hide_current_view()
        self.current_view = NewCertificateView(self.root, self.create_main_view)
        self.current_view.pack()

    def show_new_rsakey_view(self):
        '''Näyttää uuden RSA-avainparin luomiseen käytettävää näkymää'''
        self.hide_current_view()
        self.current_view = NewRsaKeyView(self.root, self.create_main_view)
        self.current_view.pack()

    def show_new_validation_view(self):
        '''Näyttää opiskelijapassin tarkistamiseen käytettävää näkymää'''
        self.hide_current_view()
        self.current_view = NewValidationView(self.root, self.create_main_view)
        self.current_view.pack()
    