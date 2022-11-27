import os
from tkinter import *


class AppPane(Frame):
    def __int__(self):
        super().__init__(master=None)
        # ATRIBUTOS DA CLASSE

        # Criação da janela
        self.master.title('Ping Scan')
        self.master.geometry('800x500+200+100')
        self.master.resizable(width=False, height=False)

    def shutdown(self):
        # shutdown -s -t {time}
        pass

    def reboot(self):
        # shutdown -r {time}
        pass

    def cancel(self):
        # shutdown -a
        pass



