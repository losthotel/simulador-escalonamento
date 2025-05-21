import os
import importlib.util
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Escalonamento de Processos")
        self.geometry("630x500")

        self.label = ctk.CTkLabel(self, text="Escolha o algoritmo de escalonamento", font=("Arial", 20))
        self.label.pack(pady=20)

        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=10)

        self.resultado_textbox = ctk.CTkTextbox(self, width=550, height=350)
        self.resultado_textbox.pack(pady=20)
        self.resultado_textbox.configure(font=("Courier New", 14))

        self.carregar_algoritmos()

    def carregar_algoritmos(self):
        pasta = "codigos"
        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".py") and not arquivo.startswith("__"):
                nome_modulo = arquivo[:-3]  # remove .py
                caminho = os.path.join(pasta, arquivo)
                btn = ctk.CTkButton(self.buttons_frame, text=nome_modulo.upper(), command=lambda c=caminho: self.executar_algoritmo(c))
                btn.pack(pady=5, padx=10)

    def executar_algoritmo(self, caminho_arquivo):
        spec = importlib.util.spec_from_file_location("modulo_escalonador", caminho_arquivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        if hasattr(modulo, "executar"):
            resultado = modulo.executar()
            self.resultado_textbox.delete("0.0", "end")
            self.resultado_textbox.insert("end", resultado)
        else:
            self.resultado_textbox.delete("0.0", "end")
            self.resultado_textbox.insert("end", "Erro: o módulo não possui uma função chamada 'executar'.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
