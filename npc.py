import ollama
import time
import sys

def digitar_texto(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def falar_com_npc(pergunta):
    resposta = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": """
                ""Você é um NPC do universo de Skyrim.
                Fale SEMPRE em português brasileiro.
                Fale como um habitante guerreiro de Tamriel.
                Use um tom medieval, sério e imersivo.
                Nunca fale como IA ou chatbot.
                Respostas simples e curtas.""
                """
            },
            {
                "role": "user",
                "content": pergunta
            }
        ],
        options={
            #"num_predict": 100,
            "temperature": 0.7
        }
    )
    
    return resposta['message']['content']


print("NPC: Viajante... aproxime-se.")

while True:
    user = input("Você: ")
    
    if user.lower() in ["sair", "exit", "quit", "adeus"]:
        print("NPC: Que a luz guie seu caminho.")
        break
    
    resposta = falar_com_npc(user)
    print("NPC: ", end="")
    digitar_texto(resposta)