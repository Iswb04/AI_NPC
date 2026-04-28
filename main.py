import tkinter as tk
from tkinter import ttk
import threading
from npc import falar_com_npc

class AppChat:
    def __init__(self, root):
        self.root = root
    
        self.root.overrideredirect(True) 
        self.root.geometry("450x700") 
        self.root.configure(bg="#1a0f00") # Marrom rústico (madeira velha)

        # Movimentação da janela personalizada
        self.root.bind("<ButtonPress-1>", self.iniciar_movimento)
        self.root.bind("<B1-Motion>", self.movimentar_janela)

        # Estilo do Scrollbar customizado (Couro e Ouro)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", 
                        background="#3a2304", 
                        troughcolor="#1a0f00", 
                        bordercolor="#1a0f00", 
                        arrowcolor="#c29a4a")

        # Cabeçalho
        self.header_frame = tk.Frame(root, bg="#26150a")
        self.header_frame.pack(fill=tk.X)

        self.header_label = tk.Label(
            self.header_frame, text="ꕤ TAVERNA DE WHITE ORCHARD", 
            bg="#26150a", fg="#c29a4a", 
            font=("Constantia", 12, "bold"), pady=15
        )
        self.header_label.pack(side=tk.LEFT, padx=20)

        # Área de Chat
        self.chat_container = tk.Frame(root, bg="#1a0f00")
        self.chat_container.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        self.chat_area = tk.Text(
            self.chat_container, state='disabled', wrap=tk.WORD, 
            bg="#0d0700", fg="#d9c5b2", font=("Palatino Linotype", 11),
            borderwidth=0, padx=15, pady=15
        )
        self.chat_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.chat_container, orient="vertical", command=self.chat_area.yview, style="Vertical.TScrollbar")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_area.configure(yscrollcommand=self.scrollbar.set)

        # Tags de cores para o Chat
        self.chat_area.tag_config("NPC", foreground="#c29a4a", font=("Palatino Linotype", 10, "bold"))
        self.chat_area.tag_config("Você", foreground="#f2f2f2", font=("Palatino Linotype", 10, "bold"))

        # --- CONTAINER DE INTERAÇÃO ---
        self.interaction_frame = tk.Frame(root, bg="#1a0f00")
        self.interaction_frame.pack(fill=tk.X, padx=20, pady=20)

        # Campo de entrada
        self.user_input = tk.Entry(
            self.interaction_frame, bg="#26150a", fg="white", 
            insertbackground="#c29a4a", borderwidth=0, font=("Segoe UI", 12)
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.ao_enviar)

        # Coluna de Botões
        self.button_column = tk.Frame(self.interaction_frame, bg="#1a0f00")
        self.button_column.pack(side=tk.RIGHT)

        self.send_btn = tk.Button(
            self.button_column, text="CONVERSAR", command=self.ao_enviar,
            bg="#4d2b1a", fg="#ffffff", borderwidth=1, font=("Arial", 8, "bold"), 
            width=12, cursor="hand2", activebackground="#633926"
        )
        self.send_btn.pack(side=tk.TOP, pady=(0, 5))

        self.exit_btn = tk.Button(
            self.button_column, text="IR EMBORA", command=root.quit,
            bg="#0d0700", fg="#ffffff", borderwidth=1, font=("Arial", 8, "bold"), 
            width=12, cursor="hand2"
        )
        self.exit_btn.pack(side=tk.TOP)

        # SAUDAÇÃO INICIAL (O ajuste que você pediu)
        self.root.after(500, lambda: self.exibir_efeito_digitacao("NPC", "Bem vindo a taberna de White Orchard. Se busca encrenca, veio ao lugar certo... se busca bebida, pague primeiro."))

    # Funções de movimento para janelas sem borda
    def iniciar_movimento(self, event):
        self.x = event.x
        self.y = event.y

    def movimentar_janela(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    # Lógica do efeito de máquina de escrever
    def exibir_efeito_digitacao(self, autor, texto, index=0):
        self.chat_area.config(state='normal')
        if index == 0: 
            self.chat_area.insert(tk.END, f"{autor}: ", autor)
        
        if index < len(texto):
            self.chat_area.insert(tk.END, texto[index])
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)
            # 20ms de velocidade entre letras
            self.root.after(20, lambda: self.exibir_efeito_digitacao(autor, texto, index + 1))
        else:
            self.chat_area.insert(tk.END, "\n\n")
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)

    def ao_enviar(self, event=None):
        msg = self.user_input.get()
        if msg.strip():
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, "Você: ", "Você")
            self.chat_area.insert(tk.END, f"{msg}\n\n")
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)
            self.user_input.delete(0, tk.END)
            # Inicia busca da resposta na IA
            threading.Thread(target=self.processar_npc, args=(msg,), daemon=True).start()

    def processar_npc(self, texto_usuario):
        resposta = falar_com_npc(texto_usuario)
        # Retorna para a thread principal para exibir a animação
        self.root.after(0, lambda: self.exibir_efeito_digitacao("NPC", resposta))

if __name__ == "__main__":
    root = tk.Tk()
    app = AppChat(root)
    root.mainloop()