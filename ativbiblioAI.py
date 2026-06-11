from datetime import datetime
import json
import os
import random
import statistics

# 1. Cria a pasta 'saida/' caso ela não exista
diretorio = "saida"
os.makedirs(diretorio, exist_ok=True)

# 2. Gera 30 números aleatórios entre 1 e 500
numeros = [random.randint(1, 500) for _ in range(30)]

# 3. Calcula a média, o maior e o menor valor
# Usando a stdlib 'statistics' estudada anteriormente + funções built-in
media = statistics.mean(numeros)
maior = max(numeros)
menor = min(numeros)

# 4. Captura a data e hora atual formatada
data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 5. Estrutura os dados para o formato JSON
dados_finais = {
    "data_hora": data_hora_atual,
    "metricas": {"media": media, "maior": maior, "menor": menor},
    "numeros_gerados": numeros,
}

# 6. Define o nome do arquivo e salva na pasta 'saida/'
caminho_arquivo = os.path.join(diretorio, "resultados.json")

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(dados_finais, arquivo, indent=4, ensure_ascii=False)

print(f"Sucesso! O arquivo foi salvo em: {caminho_arquivo}")
