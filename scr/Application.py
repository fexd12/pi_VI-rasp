from tkinter import *
# from pi.cadastro_tag import cadastrar
# from pi.leitura_tag import ler

class Application():
    def __init__(self, root):
        self.tag = "4565654645654654654645645"
        self.root = root
        self.tela()
        self.frame()
        self.title()
        self.botoes()
        self.root.mainloop()
        
    def tela(self):
        self.root.title("Interface do RFID")
        self.root.configure(background = '#1e3743')
        self.root.geometry("500x300")
        self.root.resizable(False, False)

    def frame(self):
        self.frame = Frame(self.root, bd = 4, bg = "#fff", highlightbackground="#759fe6", highlightthickness=2)
        self.frame.place(relx=0.1, rely= 0.1, relwidth= 0.8, relheight= 0.8)

    def title(self):
        self.title = Label(self.frame, text="Interface RFID", bg="#fff")
        self.title["font"] = ("Arial", "14", "italic", "bold")
        self.title.pack()
    
    def leitura_tag(self):
        # id,text = ler()
        self.tag = id
        self.entry_leitura['text'] = self.tag
    
    def cadastrar_tag(self):
        # cadastrar(self.tag)
        self.entry_leitura['text'] = ''

    def botoes(self):
        self.leitura = Button(self.frame,command=self.leitura_tag, text="Leitura")
        self.leitura.place(relx=0.15, rely=0.3, relwidth=0.2, relheight= 0.15)

        self.lb_leitura = Label(self.frame, text="Código da Tag : ", bg="#fff")
        self.lb_leitura.place(relx=0.38, rely=0.3, relwidth=0.22, relheight= 0.15)

        self.entry_leitura = Label(self.frame, text=self.tag)
        self.entry_leitura["font"] = ("Arial", "10", "bold")
        self.entry_leitura.place(relx=0.65, rely=0.3, relwidth=0.2, relheight= 0.15)

        self.cadastrar = Button(self.frame, text="Cadastrar",command=self.cadastrar_tag, bg="green", fg="white")
        self.cadastrar.place(relx=0.35, rely=0.6, relwidth=0.3, relheight= 0.2)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)