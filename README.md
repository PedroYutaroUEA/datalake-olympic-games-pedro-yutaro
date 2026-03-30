# 🏅 Data Lake Olímpico (1896 - 2024)

Este projeto consiste na implementação de um Data Lake local focado na análise histórica dos Jogos Olímpicos, integrando dados desde a primeira edição na Era Moderna (Atenas 1896) até os recentes jogos de Paris 2024. O trabalho foi desenvolvido para a disciplina de Ciência de Dados da Universidade do Estado do Amazonas (UEA/EST).

### 👤 Autor

- Aluno: Pedro Yutaro Mont Morency Nakamura
- Instituição: Universidade do Estado do Amazonas (UEA/EST)
- Data: Março de 2026

---

## 🏗️ Arquitetura do Data Lake

O projeto segue a Arquitetura Medallion, dividindo os dados em camadas de refinamento crescente para garantir a linhagem e a qualidade da informação.

- Camada Bronze (Raw): Armazena os dados brutos em formato .csv e seus respectivos metadados em .json, preservando a fonte original (Histórico 1896-2022 e Paris 2024).
- Camada Silver (Trusted): Contém os dados limpos, normalizados e convertidos para o formato Apache Parquet. Nesta camada, realizamos a integração (JOIN) entre as fontes usando o edition_id como chave de domínio.
- Camada Gold (Refined): Armazena datasets agregados de alto valor, como o quadro de medalhas consolidado, análises de gênero e dominância por modalidades.

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: Python 3.14.3.
- Principais Bibliotecas: Pandas, Matplotlib, Seaborn e PyArrow (Engine Parquet).
- Formato de Dados: Parquet (proporcionando até 99% de redução no volume de dados lidos e 34x mais velocidade em consultas).

---

## 📂 Estrutura do Repositório

```
.
├── bronze/              # Dados brutos (CSV) e metadados iniciais (JSON)
├── silver/              # Dados normalizados e integrados (Parquet)
├── gold/                # Análises finais, gráficos (PNG) e relatórios (CSV)
├── pipeline/            # Notebooks de orquestração divididos por etapas
├── src/                 # Módulos Python (Metadados, Catálogo, Processamento)
├── metadata_schema.json # Catálogo central de metadados do Data Lake
└── README.md            # Documentação do projeto
```

---

## ⚙️ Funcionamento da Pipeline

A pipeline foi modularizada para garantir a escalabilidade e facilitar o debug.

1. Ingestion (01): Varre as pastas de origem, armazena em Bronze e gera o inventário inicial de metadados.
2. Clean & Normalize (02): Converte CSVs para Parquet, padroniza nomes de países (ex: Rússia/URSS) e tipos de dados.
3. Domain Joins (03): Realiza o cruzamento de dados de atletas e medalhas. O diferencial técnico foi o uso de tabelas de Dimensão (Games) para popular anos e estações (year/season) no histórico de forma íntegra via edition_id .

---

## 📊 Análises Realizadas (Camada Gold)

As análises foram baseadas nos requisitos oficiais da atividade:

- Quadro de Medalhas: Consolidação total por país, separada por Jogos de Verão, Inverno e Geral.
- Evolução de Gênero: Visualização da curva de participação feminina, atingindo a equidade nos jogos de Paris 2024.
- Visualização: Geração de gráficos de barras para os 50 países mais bem colocados em cada categoria.

---

## 📜 Metadados e Governança

Cada dataset possui um arquivo de metadados .json associado, contendo informações como:

- Nome e descrição do dataset.
- Esquema técnico (campos, tipos de dados e contagem de nulos).
- Origem (linhagem) e data de coleta/processamento.

Todos esses metadados são centralizados no arquivo metadata_schema.json na raiz do projeto, servindo como o Data Catalog oficial.
