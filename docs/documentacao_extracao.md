# Documentacao da Etapa de Extracao (Extract)

## Projeto Integrador: Desenvolvimento Low Code em Ciencia de Dados

### Centro Universitario Senac - Educacao a Distancia

**Disciplina:** Projeto Integrador - Desenvolvimento Low Code em Ciencia de Dados

**Responsavel pela Extracao:** Janaina Figueiredo da Silva

---

## Sumario

1. Introducao
2. Fonte de Dados
3. Processo de Extracao
4. Estrutura dos Dados Extraidos
5. Analise Exploratoria Inicial
6. Consideracoes para as Etapas Seguintes
7. Referencias

---

## 1. Introducao

Este documento descreve o processo de extracao de dados realizado como parte da etapa Extract do pipeline ETL (Extract, Transform, Load) do Projeto Integrador. A extracao e a primeira etapa do processo e tem como objetivo realizar a leitura da base de dados original, validar sua integridade e disponibilizar os dados para as etapas subsequentes de limpeza, transformacao e carga.

O trabalho de extracao foi desenvolvido utilizando a linguagem Python em conjunto com a biblioteca Pandas, conforme as tecnologias definidas pelo grupo para o projeto.

---

## 2. Fonte de Dados

### 2.1 Origem

A base de dados utilizada neste projeto contem informacoes sobre o comportamento de usuarios da plataforma Netflix. O dataset foi obtido a partir da plataforma Kaggle e armazenado no repositorio do projeto na pasta `data/`.

- **Arquivo:** `base_original.csv`
- **Formato:** CSV (Comma-Separated Values)
- **Tamanho:** aproximadamente 1,5 MB
- **Total de registros:** 25.000
- **Total de colunas:** 8

### 2.2 Descricao do Dataset

A base contem informacoes relacionadas ao comportamento de usuarios da Netflix, incluindo dados demograficos, tipo de assinatura, tempo de uso da plataforma e preferencias de conteudo. Esses dados permitem analises sobre perfil de usuarios, preferencias de conteudo e padroes de consumo da plataforma.

---

## 3. Processo de Extracao

### 3.1 Tecnologias Utilizadas

| Tecnologia | Versao | Finalidade |
|------------|--------|------------|
| Python | 3.x | Linguagem de programacao principal |
| Pandas | 2.x | Leitura e manipulacao de dados tabulares |

### 3.2 Implementacao

O script de extracao foi implementado no arquivo `src/etl.py` e segue a seguinte logica:

1. **Configuracao de caminhos:** definicao dos caminhos para os arquivos de entrada (base original) e saida (base tratada), utilizando caminhos relativos ao diretorio raiz do projeto para garantir portabilidade.

2. **Leitura do arquivo CSV:** utilizacao da funcao `pd.read_csv()` da biblioteca Pandas para importar os dados do arquivo `data/base_original.csv` em um DataFrame.

3. **Validacao da existencia do arquivo:** verificacao automatica de que o arquivo de origem existe antes de tentar a leitura, com tratamento de erro adequado caso o arquivo nao seja encontrado.

4. **Geracao de relatorio:** apos a extracao, um relatorio automatizado e gerado contendo informacoes sobre dimensoes dos dados, tipos de dados, valores nulos, estatisticas descritivas e valores unicos em colunas categoricas.

### 3.3 Funcoes Implementadas

- **`extrair_dados(caminho_arquivo)`**: funcao principal que realiza a leitura do CSV e retorna um DataFrame do Pandas.
- **`exibir_relatorio_extracao(df)`**: funcao que gera um relatorio detalhado sobre os dados extraidos, facilitando a analise inicial e a comunicacao com os demais membros do grupo.

### 3.4 Execucao

Para executar o script de extracao:

```bash
python src/etl.py
```

---

## 4. Estrutura dos Dados Extraidos

### 4.1 Colunas do Dataset

| Coluna | Tipo de Dado | Descricao |
|--------|-------------|-----------|
| User_ID | int64 | Identificador unico do usuario |
| Name | string | Nome do usuario |
| Age | int64 | Idade do usuario (13 a 80 anos) |
| Country | string | Pais de origem do usuario |
| Subscription_Type | string | Tipo de plano de assinatura |
| Watch_Time_Hours | float64 | Total de horas assistidas na plataforma |
| Favorite_Genre | string | Genero de conteudo preferido |
| Last_Login | string | Data do ultimo acesso a plataforma |

### 4.2 Valores Unicos em Colunas Categoricas

**Country (10 paises):**
Australia, Brazil, Canada, France, Germany, India, Japan, Mexico, UK, USA

**Subscription_Type (3 tipos de plano):**
Basic, Premium, Standard

**Favorite_Genre (7 generos):**
Action, Comedy, Documentary, Drama, Horror, Romance, Sci-Fi

---

## 5. Analise Exploratoria Inicial

### 5.1 Dimensoes

- **Registros:** 25.000 usuarios
- **Colunas:** 8 atributos

### 5.2 Valores Nulos

A base de dados nao apresenta valores nulos em nenhuma coluna. Todos os 25.000 registros possuem dados completos para todas as 8 colunas.

### 5.3 Estatisticas Descritivas

| Metrica | User_ID | Age | Watch_Time_Hours |
|---------|---------|-----|-----------------|
| Media | 12.500,50 | 46,48 | 500,47 |
| Desvio Padrao | 7.217,02 | 19,59 | 286,38 |
| Minimo | 1 | 13 | 0,12 |
| 1o Quartil (25%) | 6.250,75 | 29 | 256,57 |
| Mediana (50%) | 12.500,50 | 46 | 501,51 |
| 3o Quartil (75%) | 18.750,25 | 63 | 745,73 |
| Maximo | 25.000 | 80 | 999,99 |

### 5.4 Observacoes Relevantes

1. **Faixa etaria:** os usuarios possuem idades entre 13 e 80 anos, com media de aproximadamente 46 anos.
2. **Tempo de uso:** o tempo de uso varia de 0,12 a 999,99 horas, com media de 500 horas, indicando uma distribuicao ampla de engajamento.
3. **Distribuicao geografica:** os usuarios estao distribuidos em 10 paises, incluindo o Brasil.
4. **Planos de assinatura:** existem 3 tipos de plano (Basic, Standard, Premium).
5. **Generos de conteudo:** 7 generos diferentes de conteudo sao preferidos pelos usuarios.
6. **Qualidade dos dados:** a ausencia de valores nulos indica uma base de dados limpa na etapa de extracao.

---

## 6. Consideracoes para as Etapas Seguintes

Com base na analise exploratoria realizada durante a extracao, as seguintes observacoes sao relevantes para os demais membros do grupo:

### Para Yuri (Limpeza e Padronizacao)

- A base nao possui valores nulos, porem e importante verificar possiveis duplicatas.
- A coluna `Last_Login` esta no formato string e pode necessitar de conversao para tipo data (`datetime`).
- Os nomes das colunas utilizam o padrao *snake_case* com letras maiusculas (ex.: `Subscription_Type`), que pode ser padronizado.

### Para Maria Elayne (Transformacao com Pandas)

- A coluna `Age` pode ser categorizada em faixas etarias para facilitar a analise.
- A coluna `Watch_Time_Hours` pode ser segmentada em niveis de engajamento (baixo, medio, alto).
- Cruzamentos entre `Country` e `Subscription_Type` ou `Favorite_Genre` podem gerar *insights* relevantes.

### Para Ian, Gabrielli e Thiago (Dashboard Streamlit)

- Os dados suportam as visualizacoes planejadas: grafico de pizza (planos), grafico de barras (generos), filtros por pais e genero.
- Metricas como idade media, total de assinantes por pais e media de horas assistidas podem ser calculadas diretamente a partir do DataFrame.

---

## 7. Referencias

CORREIA, E. **Pandas Python: data wrangling para ciencia de dados.** Sao Paulo: Casa do Codigo, 2020. E-book.

PANDAS. **Pandas Documentation.** Disponivel em: https://pandas.pydata.org/docs/. Acesso em: maio 2026.

PYTHON SOFTWARE FOUNDATION. **Python Documentation.** Disponivel em: https://docs.python.org/3/. Acesso em: maio 2026.

KAGGLE. **Netflix Userbase Dataset.** Disponivel em: https://www.kaggle.com/. Acesso em: fevereiro 2026.
