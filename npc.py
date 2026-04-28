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
                    Você é um NPC do universo de Skyrim.
                    Fale SEMPRE em português brasileiro.
                    Fale como um habitante guerreiro de Tamriel.
                    Use um tom medieval, sério e imersivo.
                    Nunca fale como IA ou chatbot.
                    Respostas simples e curtas.
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
        return f"Pelos deuses... os ventos de Oblivion impedem minha fala. (Erro: {e})"

def digitar_texto(texto=None):
    """
    Função mantida para compatibilidade com o seu código anterior,
    embora a animação agora seja gerada pela Interface Gráfica.
    """
    pass