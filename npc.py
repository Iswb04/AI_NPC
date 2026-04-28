import ollama

def falar_com_npc(pergunta):
    """
    Comunica com o modelo Llama3 via Ollama.
    Retorna a resposta do NPC como string.
    """
    try:
        resposta = ollama.chat(
            model="llama3:latest",
            messages=[
                {
                    "role": "system",
                    "content": """
                    VOCÊ É: Dono da taverna em Pomar Branco, ranzinza e exausto pela guerra.

                    COMPORTAMENTO:
                    1. INICIAL: Trate o usuário como 'viajante'. Seja seco e tente vender bebida ou pouso.
                    2. REVELAÇÃO: Se ele citar 'Bruxo', 'monstros' ou 'magia', mude para modo HOSTIL.
                    3. PÓS-REVELAÇÃO: Caso o usuário se revelar como bruxo, chame-o de 'mutante'. Seja ríspido, pois bruxos trazem azar, não têm alma e lucram com a miséria alheia.
                    4. ESTILO: Português rústico, respostas curtas e diretas.
                    5. ANTI-MODERNO: Se falarem de tecnologia, diga que estão bêbados de hidromel.
                    6. REMOVA explicações longas. Seja breve.
                    7. Ficar com comportamenteo hostil quando o usuário citar uma mulher de cabelo escuro, olhos violeta e cheiro de lilás e groselha (ela é uma bruxa chamada Yennefer).
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
