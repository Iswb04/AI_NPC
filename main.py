import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
import pywinstyles # Biblioteca para customizar a barra do Windows
from npc import falar_com_npc

class AppChat:
    def __init__(self, root):
        self.root = root
        self.root.title("Taberna de Skyrim")
        self.root.geometry("450x650")
        self.root.configure(bg="#1a1a1a")

        # --- ESTILO DO SCROLLBAR ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", 
                        gripcount=0,
                        background="#333333", # Cor do botão de rolagem
                        darkcolor="#1a1a1a", 
                        lightcolor="#1a1a1a",
                        troughcolor="#1a1a1a", # Cor do fundo do scroll
                        bordercolor="#1a1a1a", 
                        arrowcolor="#d4af37") # Cor das setinhas

        # --- TOPO CUSTOMIZADO (Windows 10/11) ---
        # Isso deixa a barra de título escura
        pywinstyles.apply_style(self.root, "dark")
        # Você também pode tentar mudar para uma cor específica se o Windows permitir:
        # pywinstyles.change_header_color(self.root, "#333333")

        # Cabeçalho Interno
        self.header = tk.Label(
            root, text="⚔️ CRÔNICAS DE TAMRIEL ⚔️", 
            bg="#1a1a1a", fg="#d4af37", 
            font=("Georgia", 14, "bold"), pady=15
        )
        self.header.pack(fill=tk.X)

        # Container para o Chat + Scrollbar
        self.chat_container = tk.Frame(root, bg="#1a1a1a")
        self.chat_container.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Área de Chat
        self.chat_area = tk.Text(
            self.chat_container, state='disabled', wrap=tk.WORD, 
            bg="#121212", fg="#e0e0e0", 
            font=("Segoe UI", 11),
            borderwidth=0, padx=15, pady=15,
            insertbackground="white"
        )
        self.chat_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar Customizada
        self.scrollbar = ttk.Scrollbar(self.chat_container, orient="vertical", command=self.chat_area.yview, style="Vertical.TScrollbar")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_area.configure(yscrollcommand=self.scrollbar.set)

        # Configuração de cores
        self.chat_area.tag_config("NPC", foreground="#d4af37", font=("Segoe UI", 10, "bold"))
        self.chat_area.tag_config("Você", foreground="#ffffff", font=("Segoe UI", 10, "bold"))

        # Frame de Entrada
        self.entry_frame = tk.Frame(root, bg="#1a1a1a")
        self.entry_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        self.user_input = tk.Entry(
            self.entry_frame, bg="#333333", fg="white", 
            insertbackground="white", borderwidth=0, 
            font=("Segoe UI", 12), relief="flat"
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 10))
        self.user_input.bind("<Return>", self.ao_enviar)

        self.send_btn = tk.Button(
            self.entry_frame, text="FALAR", command=self.ao_enviar,
            bg="#333333", fg="#d4af37", borderwidth=1, 
            font=("Georgia", 10, "bold"), padx=15, cursor="hand2"
        )
        self.send_btn.pack(side=tk.RIGHT, ipady=5)

        self.root.after(500, lambda: self.exibir_efeito_digitacao("NPC", "Viajante... o que busca nestas terras gélidas?"))

    # ... (Mantenha as funções exibir_efeito_digitacao, ao_enviar e processar_npc iguais ao código anterior)
    def exibir_efeito_digitacao(self, autor, texto, index=0):
        self.chat_area.config(state='normal')
        if index == 0:
            self.chat_area.insert(tk.END, f"{autor}: ", autor)
        if index < len(texto):
            self.chat_area.insert(tk.END, texto[index])
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)
            self.root.after(20, lambda: self.exibir_efeito_digitacao(autor, texto, index + 1))
        else:
            self.chat_area.insert(tk.END, "\n\n")
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)

    def ao_enviar(self, event=None):
        msg = self.user_input.get()
        if msg.strip():
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"Você: ", "Você")
            self.chat_area.insert(tk.END, f"{msg}\n\n")
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)
            self.user_input.delete(0, tk.END)
            threading.Thread(target=self.processar_npc, args=(msg,), daemon=True).start()

    def processar_npc(self, texto_usuario):
        resposta = falar_com_npc(texto_usuario)
        self.root.after(0, lambda: self.exibir_efeito_digitacao("NPC", resposta))

if __name__ == "__main__":
    root = tk.Tk()
    app = AppChat(root)
    root.mainloop()