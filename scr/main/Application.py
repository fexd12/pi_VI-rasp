from tkinter import *

from main import cadastrar_rfid,ler_rfid

class Application():
    def __init__(self, root):
        self.tag = "123456789"
        self.root = root
        self.tela()
        self.frame()
        self.title()
        self.botoes()
        mainloop()



    def tela(self):
        self.root.title("Interface do RFID")
        self.root.configure(background = '#1e3743')
        self.root.geometry("500x300")
        self.root.resizable(False, False)

    def frame(self):
        self.frame = Frame(self.root, bd = 4, bg = "#fff", highlightbackground="#759fe6", highlightthickness=2)
        self.frame.place(relx=0.1, rely= 0.1, relwidth= 0.8, relheight= 0.8)

        imagem = PhotoImage(file="main/icons/teste.png")
        self.w = Label(self.root, image=imagem, bg="#fff")
        self.w.imagem = imagem
        self.w.place(relx=0.785, rely= 0.71)
        
      

    
    def title(self):
        self.title = Label(self.frame, text="Interface RFID", bg="#fff")
        self.title["font"] = ("Arial", "14", "italic", "bold")
        self.title.pack()

   


    def botoes(self):
        self.leitura = Button(self.frame, text="Leitura")
        self.leitura.place(relx=0.15, rely=0.3, relwidth=0.2, relheight= 0.15)


        self.lb_leitura = Label(self.frame, text="Código da Tag : ", bg="#fff")
        self.lb_leitura.place(relx=0.38, rely=0.3, relwidth=0.22, relheight= 0.15)

        self.entry_leitura = Label(self.frame, text=self.tag)
        self.entry_leitura["font"] = ("Arial", "10", "bold")
        self.entry_leitura.place(relx=0.65, rely=0.3, relwidth=0.2, relheight= 0.15)

        self.cadastrar = Button(self.frame, text="Cadastrar",command=cadastrar_rfid, bg="green", fg="white")
        self.cadastrar.place(relx=0.35, rely=0.6, relwidth=0.3, relheight= 0.2)
    
        
 

if __name__ == '__main__':
    root = Tk()
    app = Application(root)