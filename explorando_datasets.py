from datasets import load_dataset

# Carregando o dataset IMDb em modo streaming
# Streaming é útil para trabalhar com datasets muito grandes que não cabem na memória
dataset = load_dataset("zapsdcn/imdb", streaming=True)

# print(dataset)

dataset_treino = dataset["train"]

for linha in dataset_treino:
    print(linha)
    input()

# print("==============================")

# print(dataset_treino[9])
# input()
# print(dataset_treino['label'])
# input()
# print(dataset_treino[9]['label'])

# print("==============================")

# df = dataset_treino.to_pandas()
# print(df)
