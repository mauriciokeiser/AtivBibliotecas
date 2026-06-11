import random
import statistics
from datetime import datetime
import json
import pathlib
import os


#Cria os valores
valores = [random.randint(1, 501) for _ in range(30)]
print(f"{valores}")

#Média dos valores
media = statistics.mean(valores)
print(f"Média: {statistics.mean(valores):.2f}")

#Maior valor
maior_valor = max(valores)
print(f"Maior: {maior_valor:.2f}")

#Menor Valor
menor_valor = min(valores)
print(f"Menor: {menor_valor:.2f}")

#Cria pasta de nome "saida"
pasta = pathlib.Path("saida_meu")
pasta.mkdir(exist_ok=True)
arquivo = pasta / "resultados.json"


arquivo.write_text("valores gerados", encoding="utf-8")
print(arquivo.read_text(encoding="utf-8"))

# 4. Captura a data e hora atual formatada
data_hora_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# 5. Estrutura os dados para o formato JSON
dados_finais = {
    "data_hora": data_hora_atual,
    "metricas": {"media": media, "maior": maior_valor, "menor": menor_valor},
    "numeros_gerados": valores,
}

# 6. Define o nome do arquivo e salva na pasta 'saida/'
caminho_arquivo = os.path.join(pasta, "resultados.json")

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(dados_finais, arquivo, indent=4, ensure_ascii=False)

print(f"Sucesso! O arquivo foi salvo em: {caminho_arquivo}")