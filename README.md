Redes Neurais para Reconhecimento de Fala Atípica
Trabalho de Conclusão de Curso - Bacharelado em Matemática Industrial
Universidade Federal do Paraná (UFPR)

Autora: Mariana Marques Cabral
Orientadora: Profª Drª Evelin Heringer Manoel Krulikovski
Coorientador: Prof. Dr. Lucas Garcia Pedroso
Ano: 2026


Descrição
Este trabalho desenvolve e avalia um modelo de aprendizado de máquina para reconhecimento automático de dígitos falados (0–9), com ênfase em fala atípica decorrente de condições como paralisia cerebral e disartria.

A abordagem utiliza uma Rede Neural Convolucional (CNN) treinada sobre representações de áudio extraídas por coeficientes MFCC (Mel Frequency Cepstral Coefficients). O modelo é treinado com dados de fala típica e disártrica combinados, atingindo 98,12% de acurácia no conjunto de teste (11 classes: dígitos 0–9 + classe nao_numero).


Bases de Dados
Os áudios não estão incluídos neste repositório por limitação de tamanho. As duas bases utilizadas são públicas e podem ser baixadas nos links abaixo:

Base
Descrição
Link
UA-Speech
19 falantes com paralisia cerebral, gravações de dígitos 0–9 e palavras isoladas
UA-Speech Dataset
FSDD
Free Spoken Digit Dataset — dígitos 0–9 por múltiplos falantes (fala típica)
FSDD no GitHub


Após baixar as bases, organize os arquivos da seguinte forma:

.gitignore/

├── trabalho2/      ← arquivos .wav da UA-Speech

└── trabalho4/      ← arquivos .wav do FSDD


Estrutura do Repositório
├── README.md

├── requirements.txt                        # Dependências do projeto

├── dados_preparados2.csv                   # Índice dos áudios com rótulos e divisão treino/teste

│

├── codigo/

│   ├── Untitled-1.ipynb                    # Notebook principal: pré-processamento, treinamento e avaliação

│   ├── script 1_preparar_dados.py          # Script de organização e balanceamento das bases

│   ├── imagem2_preparardados.py            # Script para geração de figura do fluxo de dados

│   └── Graficos                            # Script para geração de gráficos auxiliares

│

├── modelo/

│   ├── modelo_cnn_digitos.h5               # !!! Não incluído (arquivo > 25 MB - gere executando o notebook)

│   ├── label_encoder_digits.pkl            # LabelEncoder para decodificação das classes

│   └── max_frames.pkl                      # Valor de MAX_FRAMES (percentil 90) usado no pré-processamento

│

└── figuras/

    ├── matriz_confusao.jpg                 # Figura: matriz de confusão no conjunto de teste

    ├── espectrograma.png                   # Figura: espectrograma de exemplo

    ├── mfccs.png                           # Figura: matriz de MFCCs normalizada

    ├── figura1_mfcc_bruta.jpg              # Figura: primeiros coeficientes MFCC ao longo do tempo

    └── Grafico_1_motivacao.png             # Figura: panorama epidemiológico (capítulo Motivação)


Instalação
pip install -r requirements.txt

Versões utilizadas no desenvolvimento:

Python 3.10
TensorFlow 2.15.0
librosa 0.10.1
numpy 1.26.4
scipy 1.10.1
scikit-learn
pandas
matplotlib


Como Reproduzir
1. Preparar os dados
python "script 1_preparar_dados.py"

Isso gera o arquivo dados_preparados2.csv com os caminhos dos áudios, rótulos e divisão treino/teste.
2. Executar o notebook principal
Abra e execute o Untitled-1.ipynb em ordem. O notebook cobre:

Exploração dos dados (forma de onda, espectrograma, MFCCs)
Extração de 40 coeficientes MFCC por áudio (SR = 16.000 Hz)
Normalização z-score e padronização temporal (MAX_FRAMES = 95)
Divisão treino/teste estratificada (70/30)
Definição e treinamento da CNN (early stopping, class weights)
Avaliação: acurácia, F1-score, matriz de confusão
3. Usar o modelo salvo
O arquivo modelo_cnn_digitos.h5 não está incluído no repositório por exceder o limite de tamanho do GitHub (> 25 MB). Para obtê-lo, execute o notebook Untitled-1.ipynb completo — o modelo será salvo automaticamente na pasta local.

Após gerar o modelo, para carregá-lo:

import joblib

from tensorflow.keras.models import load_model

model = load_model("modelo_cnn_digitos.h5")

encoder = joblib.load("label_encoder_digits.pkl")

MAX_FRAMES = joblib.load("max_frames.pkl")


Resultados
Métrica
Valor
Acurácia (teste)
98,12%
F1-score médio
0,98
Classes
11 (dígitos 0–9 + nao_numero)
Amostras de teste
21.379



Arquitetura do Modelo
Rede Neural Convolucional sequencial com:

3 blocos convolucionais (Conv2D + BatchNorm + MaxPooling)
2 camadas densas (256 e 128 neurônios, ReLU)
Dropout (0,4 e 0,3)
Saída Softmax com 11 classes
Total de parâmetros treináveis: 1.929.931

Entrada: matriz MFCC de shape (40, 95, 1)


Licença
Este repositório é disponibilizado para fins acadêmicos.
Os dados de áudio pertencem às suas respectivas bases originais (UA-Speech e FSDD).

