import os
import pandas as pd
import random
import re

# Caminhos das bases
paths = {
    "disartria": r"C:\Users\pm26937\Downloads\TCC_AudioCNN\Projeto-Mariana\.gitignore\trabalho2",
    "normal": r"C:\Users\pm26937\Downloads\TCC_AudioCNN\Projeto-Mariana\.gitignore\trabalho4"
}


# Lista para armazenar os dados
dados = []

print("Verificando caminhos:")
for tipo, caminho in paths.items():
    print(f" - {tipo}: {os.path.exists(caminho)}  ({caminho})")


# Percorrer cada base
for tipo_base, caminho_base in paths.items():
    for root, _, files in os.walk(caminho_base):
        for file in files:
            if file.endswith(".wav"):
                nome = file.lower()
                numero = None

                # Identificar número falado
                # base disartria (D0..D9)
                if tipo_base == "disartria":
                    match = re.search(r'_d(\d)_', nome)
                    if match:
                        numero = match.group(1)
                        
                # base normal (0_48_45.wav etc)
                elif tipo_base == "normal":
                    if nome[0].isdigit():
                        numero = nome[0]
                
                if numero is None:
                    numero = "nao_numero"
                caminho_completo = os.path.join(root, file)
                dados.append({
                    "caminho": caminho_completo,
                    "numero": numero,
                    "origem": tipo_base
                })

# DataFrame
df = pd.DataFrame(dados)
print(f"Total de áudios encontrados: {len(df)}")

print("\nDistribuição ORIGINAL:")
print(df["numero"].value_counts())

# BALANCEAMENTO DO DATASET
# separar dígitos e nao_numero
df_digitos = df[df["numero"] != "nao_numero"]
df_nao = df[df["numero"] == "nao_numero"]
print("\nTotal de dígitos:", len(df_digitos))
print("Total de nao_numero original:", len(df_nao)) 

# limitar quantidade de nao_numero
limite_nao = len(df_digitos)

df_nao_balanceado = df_nao.sample(
    n=limite_nao,
    random_state=42
)

# juntar novamente
df = pd.concat([df_digitos, df_nao_balanceado])

print("\nDistribuição APÓS BALANCEAMENTO:")
print(df["numero"].value_counts())

# Embaralhar
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Separar treino/teste (70/30) mantendo proporção por origem e número
def dividir_treino_teste(grupo):
    n_treino = int(0.7 * len(grupo))
    grupo["tipo"] = ["treino"] * n_treino + ["teste"] * (len(grupo) - n_treino)
    return grupo

df = df.groupby(["origem", "numero"], group_keys=False).apply(dividir_treino_teste)

# Salvar CSV
saida_csv = os.path.join(os.path.dirname(__file__), "dados_preparados2.csv")
df.to_csv(saida_csv, index=False, encoding="utf-8")
print(f"✅ Arquivo salvo em: {saida_csv}")

# Resumo
print("\nResumo por origem e tipo:")
print(df.groupby(["origem", "tipo"])["caminho"].count())
