from transformers import pipeline

chatbot = pipeline(
    task="text-generation",
    model="Felladrin/Llama-68M-Chat-v1",
    max_new_tokens=300,
    penalty_alpha=0.5,
    top_k=4
)

# <|im_start|>system
# {system_message}<|im_end|>
# <|im_start|>user
# {user_message}<|im_end|>
# <|im_start|>assistant

mensagem_sistema = "You are a helpful artificial intelligence."
prompt_sistema = f'<|im_start|>system\n{mensagem_sistema}<|im_end|>\n'

pergunta = "Hi, what is your name?"
prompt_usuario = f"<|im_start|>user\n{pergunta}<|im_end|>\n"
prompt_completo = f"{prompt_sistema}{prompt_usuario}<|im_start|>assistant\n"

resposta = chatbot(prompt_completo)

resposta_formatada = resposta[0]['generated_text'].split("<|im_start|>assistant\n")[-1].rstrip('<|im_end|>')

print(f"Sua pergunta: {pergunta}")
print(f"Resposta do bot: {resposta_formatada}")
