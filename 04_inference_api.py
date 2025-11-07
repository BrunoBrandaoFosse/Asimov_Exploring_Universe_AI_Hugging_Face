# ==============================================================
# Usando a API de Inferência do Hugging Face
# ==============================================================
# Quando termos um modelo muito grande, podemos usar a API de inferência hospedada no Hugging Face
# para fazer as predições sem precisar baixar o modelo localmente.

# import requests

# modelo = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# url = f"https://api-inference.huggingface.co/models/{modelo}"

# json = {
#     "inputs": "What is the capital of France?",
# }

# response = requests.post(url, json=json)

# print(response.json())

# ==============================================================

# from transformers import AutoTokenizer

# # modelo = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# modelo = "Felladrin/Llama-68M-Chat-v1"

# chat = [
#     {"role": "user", "content": "Olá, qual é o seu nome?"},
#     {"role": "assistant", "content": "Olá! Eu sou um modelo de IA. Como posso ajudar?"},
#     {"role": "user", "content": "Gostaria de aprender Python. Você tem alguma dica?"},
# ]

# tokenizer_mixtral = AutoTokenizer.from_pretrained(modelo)
# template_mixtral = tokenizer_mixtral.apply_chat_template(chat, tokenize=False, add_generation_token=True)

# print(template_mixtral)

# ==============================================================

import requests
from transformers import AutoTokenizer

modelo = "mistralai/Mixtral-8x7B-Instruct-v0.1"

chat = [
    {"role": "user", "content": "Olá, qual é o seu nome?"},
    {"role": "assistant", "content": "Olá! Eu sou um modelo de IA. Como posso ajudar?"},
    {"role": "user", "content": "Gostaria de aprender Python. Você tem alguma dica?"},
]

tokenizer = AutoTokenizer.from_pretrained(modelo)
template = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_token=True)

url = f"https://api-inference.huggingface.co/models/{modelo}"

json = {
    "inputs": template,
    "options": {"use_cache": False, "wait_for_model": True},
}

response = requests.post(url, json=json)

print(response.json())


