import ollama

def falar_com_npc(pergunta):
    """
    Comunica com o modelo Llama3 via Ollama.
    Retorna a resposta do NPC como string.
    """
    try:
        resposta = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "system",
                    "content": """
                    Você é um frequentador da taverna de Pomar Branco em The Witcher 3.
                    Você odeia bruxos e está tenso por causa da guerra com Nilfgaard.
                    Fale em português brasileiro, use um tom rústico e defensivo, mas ao mesmo tempo amigavel.
                    Tente ser breve, não exagere nos textos.
                    """
                },
                {
                    "role": "user",
                    "content": pergunta
                }
            ],
            options={
                "temperature": 0.7
            }
        )
        return resposta['message']['content']
    except Exception as e:
        return f"Pelos deuses... a guerra destruiu tudo, até a conexão. (Erro: {e})"

def digitar_texto(texto=None):
    """
    Função mantida para compatibilidade com o seu código anterior,
    embora a animação agora seja gerada pela Interface Gráfica.
    """
    pass