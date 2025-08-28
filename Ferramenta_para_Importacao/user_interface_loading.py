import tkinter as tk
from tkinter import ttk

class LoadingInterface:
    def __init__(self, mensagem="Processando..."):
        self.root = tk.Tk()
        self.root.title("Carregando")
        self.root.geometry("300x100")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text=mensagem)
        self.label.pack(pady=10)

        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(fill='x', padx=20, pady=10)
        self.progress.start(10)

    def iniciar(self):
        self.root.mainloop()

    def fechar(self):
        self.progress.stop()
        self.root.destroy()