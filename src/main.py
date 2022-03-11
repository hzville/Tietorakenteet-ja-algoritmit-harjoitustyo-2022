from tkinter import Tk
from ui.ui import Ui

def main():
    '''Alustaa käyttöliittymän ja käynnistää sovelluksen'''
    window = Tk()
    window.geometry("600x600")
    window.title('Opiskelijapassi')
    ui = Ui(window) # pylint: disable=invalid-name
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()
 