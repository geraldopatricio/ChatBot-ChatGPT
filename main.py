import openai
import os

openai.organization = "SUA-KEY-Organization-Aki"
openai.api_key = os.environ["SUA-KEY-AKI"]

def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1,stop=None, temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

def chat():
    print("Olá! Eu sou um ChatBot personalizado. Como posso ajudá-lo?")

    while True:
        user_input = input("Usuário: ")
        if user_input.lower() == "sair":
            break

        response = get_response(user_input)
        print("ChatBot: " + response)

if __name__ == "__main__":
    chat()
