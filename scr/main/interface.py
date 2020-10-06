from tkinter import *

root = Tk()


class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.title()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Interface do RFID")
        self.root.configure(background = '#1e3743')
        self.root.geometry("500x300")
        self.root.resizable(False, False)

    def frame(self):
        self.frame = Frame(self.root, bd = 4, bg = "#fff", highlightbackground="#759fe6", highlightthickness=2)
        self.frame.place(relx=0.1, rely= 0.1, relwidth= 0.8, relheight= 0.8)
    
    def title(self):
        self.title = Label(self.frame, text="Interface RFID")
        self.title["font"] = ("Arial", "14", "italic", "bold")
        self.title.pack()

    def botoes(self):
        self.cadastrar = Button(self.frame, text="Cadastrar")
        self.cadastrar.place(relx=0.15, rely=0.35, relwidth=0.3, relheight= 0.2)

        self.leitura = Button(self.frame, text="Leitura")
        self.leitura.place(relx=0.55, rely=0.35, relwidth=0.3, relheight= 0.2)


Application()
