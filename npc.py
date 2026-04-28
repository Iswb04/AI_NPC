import ollama

def falar_com_npc(pergunta):
    try:
        resposta = ollama.chat(
            model="llama3:latest",
            messages=[
                {
                    "role": "system",
                    "content": """
                    VOCÊ É: Dono da taverna em Pomar Branco, ranzinza e exausto pela guerra.

                    COMPORTAMENTO:
                    1. INICIAL: Trate o usuário como 'viajante'. Seja direto porém amigavél (só mude de comportamento após revelação ou suspeita)
                    2. REVELAÇÃO: Se ele citar 'Bruxo', 'monstros' ou 'magia', mude para modo HOSTIL.
                    3. PÓS-REVELAÇÃO: Caso o usuário se revelar como bruxo, chame-o de 'mutante'. Seja ríspido, pois bruxos trazem azar, não têm alma e lucram com a miséria alheia.
                    4. ESTILO: Português rústico, respostas curtas e diretas.
                    5. ANTI-MODERNO: Se falarem de tecnologia, diga que estão bêbados de hidromel.
                    6. REMOVA explicações longas. Seja breve. (um parágrafo)
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
    



    # em caso de npc.py
"""if __name__ == "__main__":
    print("\n\033[31m--- Entrando na Taverna de Pomar Branco ---\033[31m")
    print("\n\033[33mTaverneiro:\033[0m Bem vindo a taberna de White Orchard. Se busca encrenca, veio ao lugar certo... se busca bebida, pague primeiro.")


while True:
        entrada_usuario = input("\n\033[33mVocê: \033[0m")
        
        if entrada_usuario.lower() in ["sair", "exit", "quit"]:
            print("\033[33mTaverneiro:\033[33m Já vai tarde. Não esqueça de fechar a porta!")
            break
            
        resposta_npc = falar_com_npc(entrada_usuario)
        print(f"\n\033[33mTaverneiro: \033[0m {resposta_npc}")"""
