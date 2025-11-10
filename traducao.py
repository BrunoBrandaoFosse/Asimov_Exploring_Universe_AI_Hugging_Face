from transformers import pipeline

modelo = "facebook/mbart-large-50-many-to-many-mmt"

mensagem = "Olá, estou aprendendo a usar modelos de tradução automática."

tradutor = pipeline(task="translation", model=modelo)

traducao = tradutor(mensagem, src_lang="pt_XX", tgt_lang="en_XX")

print(traducao)
