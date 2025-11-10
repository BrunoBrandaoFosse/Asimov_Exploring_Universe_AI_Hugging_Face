from transformers import pipeline

modelo = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"

reviews = [
  "Eu amo este produto! Funciona muito bem e superou minhas expectativas.",
  "Esta é a pior compra que já fiz. Completamente decepcionado.",
  "Está ok, não é o melhor, mas também não é o pior.",
  "Excelente qualidade e ótimo custo-benefício.",
  "Não gostei do atendimento ao cliente, foi muito ruim.",
]

classificador = pipeline(task="text-classification", model=modelo)

resultados = classificador(reviews)

for review, resultado in zip(reviews, resultados):
    print(f"Review: {review}")
    print(f"Sentimento: {resultado['label']}, Score: {resultado['score']:.4f}")
    print()

