# Documentacao da Etapa de Transformacao (Transform)

## Projeto Integrador: Desenvolvimento Low Code em Ciencia de Dados

### Centro Universitario Senac - Educacao a Distancia

**Disciplina:** Projeto Integrador - Desenvolvimento Low Code em Ciencia de Dados

**Responsavel pela Transformacao:** Maria Elayne Silva de Almeida

---

# Sumario

1. Introducao  
2. Objetivo da Transformacao  
3. Importacao das Bibliotecas  
4. Carregamento da Base de Dados  
5. Analise Inicial da Base  
6. Preparacao dos Dados  
7. Criacao da Faixa Etaria  
8. Tabelas Agregadas  
9. Cruzamento de Variaveis  
10. Estatisticas Gerais  
11. Conclusao  

---

# 1. Introducao

Este documento descreve a etapa de transformacao de dados realizada no processo ETL (Extract, Transform, Load) do Projeto Integrador. A etapa de transformacao tem como objetivo preparar os dados para analise e utilizacao no dashboard interativo desenvolvido em Streamlit.

Durante o processo foram aplicadas tecnicas de manipulacao de dados utilizando a biblioteca Pandas, incluindo verificacao de duplicatas, categorizacao de usuarios, agrupamentos e geracao de estatisticas.

---

# 2. Objetivo da Transformacao

A etapa de transformacao teve como principais objetivos:

- Preparar os dados para analise;
- Organizar informacoes em categorias;
- Criar tabelas agregadas;
- Gerar estatisticas relevantes;
- Facilitar a construcao do dashboard;
- Produzir informacoes estruturadas para tomada de decisao.

---

# 3. Importacao das Bibliotecas

Foram utilizadas as seguintes bibliotecas:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

## Bibliotecas Utilizadas

| Biblioteca | Finalidade |
|------------|------------|
| Pandas | Manipulacao e analise de dados |
| Matplotlib | Criacao de graficos e visualizacoes |

---

# 4. Carregamento da Base de Dados

A base foi carregada utilizando:

```python
df = pd.read_csv("base_original.csv")
```

## Objetivo desta etapa

- Ler o arquivo CSV;
- Transformar os dados em um DataFrame;
- Permitir manipulacao estruturada das informacoes.

---

# 5. Analise Inicial da Base

## 5.1 Visualizacao Inicial

Foi utilizado:

```python
df.head()
```

### Objetivo

Visualizar os primeiros registros da base para:

- Confirmar o carregamento correto;
- Verificar colunas existentes;
- Observar o formato inicial dos dados.

---

## 5.2 Verificacao da Estrutura

Foi utilizado:

```python
df.info()
```

### Objetivo

Analisar:

- Quantidade de linhas e colunas;
- Tipos de dados;
- Valores nulos;
- Consumo de memoria.

---

# 6. Preparacao dos Dados

## 6.1 Verificacao de Dados Duplicados

Foi utilizado:

```python
df.duplicated().sum()
```

### Objetivo

Identificar registros duplicados que poderiam comprometer as analises realizadas posteriormente.

### Resultado

Nao foram encontrados registros duplicados na base.

---

# 7. Criacao da Faixa Etaria

Foi criada a seguinte funcao:

```python
def faixa_etaria(idade):
    if idade < 18:
        return "Menor de idade"
    elif idade < 30:
        return "Jovem"
    elif idade < 60:
        return "Adulto"
    else:
        return "Senior"
```

## Objetivo

Classificar os usuarios em categorias etarias para facilitar analises segmentadas.

---

## Categorias Criadas

| Faixa Etaria | Condicao |
|--------------|-----------|
| Menor de idade | idade menor que 18 |
| Jovem | idade entre 18 e 29 |
| Adulto | idade entre 30 e 59 |
| Senior | idade igual ou maior que 60 |

---

## Aplicacao da Funcao

```python
df["Faixa_Etaria"] = df["Age"].apply(faixa_etaria)
```

---

## Verificacao das Categorias

Foi utilizado:

```python
df["Faixa_Etaria"].value_counts()
```

### Resultado Obtido

| Faixa Etaria | Quantidade |
|--------------|------------|
| Adulto | 11013 |
| Senior | 7694 |
| Jovem | 4480 |
| Menor de idade | 1813 |

---

## Verificacao de Valores Nulos

Foi utilizado:

```python
df["Faixa_Etaria"].isnull().sum()
```

### Resultado

Nao foram encontrados valores nulos na coluna criada.

---

# 8. Tabelas Agregadas

## 8.1 Quantidade de Usuarios por Pais

Foi criada a tabela:

```python
df_pais = df["Country"].value_counts().reset_index()
df_pais.columns = ["Country", "Quantidade"]
```

### Objetivo

Agrupar os usuarios por pais e contabilizar a quantidade de registros.

---

## 8.2 Quantidade por Faixa Etaria

Foi utilizado:

```python
df_faixa = df.groupby("Faixa_Etaria").size().reset_index(name="Quantidade")
```

### Objetivo

Agrupar usuarios conforme faixa etaria.

---

## 8.3 Quantidade por Genero Favorito

Foi criada a tabela:

```python
df_genero = df["Favorite_Genre"].value_counts().reset_index()
df_genero.columns = ["Favorite_Genre", "Quantidade"]
```

### Objetivo

Identificar os generos de conteudo mais populares entre os usuarios.

---

# 9. Cruzamento de Variaveis

## 9.1 Faixa Etaria x Genero Favorito

Foi utilizado:

```python
df_faixa_genero = df.groupby(
    ["Faixa_Etaria", "Favorite_Genre"]
).size().reset_index(name="Quantidade")
```

### Objetivo

Relacionar faixa etaria e genero favorito para identificar padroes de preferencia.

### Finalidade

- Identificar preferencias por idade;
- Comparar comportamentos;
- Descobrir padroes de consumo.

---

## 9.2 Pais x Faixa Etaria

Foi utilizado:

```python
df_pais_faixa = df.groupby(
    ["Country", "Faixa_Etaria"]
).size().reset_index(name="Quantidade")
```

### Objetivo

Analisar a distribuicao etaria dos usuarios em cada pais.

---

# 10. Estatisticas Gerais

## Total de Registros

```python
total_registros = df.shape[0]
```

### Resultado

25.000 registros.

---

## Quantidade de Paises

```python
total_paises = df["Country"].nunique()
```

### Resultado

10 paises unicos.

---

## Faixa Etaria Mais Comum

```python
faixa_mais_comum = df["Faixa_Etaria"].mode()[0]
```

### Resultado

A faixa etaria mais comum foi "Adulto".

---

## Criacao do Resumo Geral

Foi criado o seguinte dicionario:

```python
resumo = {
    "total_registros": df.shape[0],
    "total_paises": df["Country"].nunique(),
    "faixa_mais_comum": df["Faixa_Etaria"].mode()[0]
}
```

### Objetivo

Centralizar as principais metricas da analise em uma unica estrutura de dados.

---

# 11. Conclusao

Durante esta etapa foram aplicados conceitos fundamentais de analise e transformacao de dados utilizando Pandas.

As principais atividades realizadas foram:

- Exploracao inicial da base;
- Verificacao de duplicatas;
- Criacao de categorias etarias;
- Agrupamentos e tabelas agregadas;
- Cruzamento de variaveis;
- Geracao de estatisticas descritivas.

A transformacao dos dados permitiu estruturar informacoes relevantes para utilizacao nas visualizacoes e indicadores do dashboard desenvolvido em Streamlit.
