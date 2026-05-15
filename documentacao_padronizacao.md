# Documentacao da Etapa de Padronização (Data Standardization.)

## Projeto Integrador: Desenvolvimento Low Code em Ciencia de Dados

### Centro Universitario Senac - Educacao a Distancia

**Disciplina:** Projeto Integrador - Desenvolvimento Low Code em Ciencia de Dados

**Responsavel pela Padronização e Limpeza:** Yuri da Silva Camargo

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

Este documento descreve o processo de Limpeza e Padronização de dados como parte da etapa Transform do pipeline ETL (Extract, Transform, Load) do Projeto Integrador. A limpeza e a padronização dos dados é uma etapa de extrema importância para verificação da integridade dos dados.



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

## 3. Processo de Limpeza e Padronização

### 3.1 Tecnologias Utilizadas

| Tecnologia | Versao | Finalidade |
|------------|--------|------------|
| Python | 3.x | Linguagem de programacao principal |
| Pandas | 2.x | Leitura e manipulacao de dados tabulares |

### 3.2 Implementacao

1. A primeira parte importa a biblioteca Pandas que é ferramenta padrão para manipular DataFrames. Os arquivos são separados através de 'None", para que o Python não foque exatamente em um padrão específico de separador e logo após é feita a exibição das primeiras 5 linhas do arquivo depois da correção do separador.

|index|User\_ID|Name|Age|Country|Subscription\_Type|Watch\_Time\_Hours|Favorite\_Genre|Last\_Login|
|---|---|---|---|---|---|---|---|---|
|0|1|James Martinez|18|France|Premium|80\.26|Drama|2024-05-12|
|1|2|John Miller|23|USA|Premium|321\.75|Sci-Fi|2025-02-05|
|2|3|Emma Davis|60|UK|Basic|35\.89|Comedy|2025-01-24|
|3|4|Emma Miller|44|USA|Premium|261\.56|Documentary|2024-03-25|
|4|5|Jane Smith|68|USA|Standard|909\.3|Drama|2025-01-14|

2. São removidas as linhas duplicadas com o seguinte bloco de código: 'initial_rows = len(df)', seguido de 'df.drop_duplicates(inplace=True)' e a função 'print" para exibir o resultado da lógica do script. (Como apontado pela colaboradora Janaina, nesse arquivo .csv não existem valores nulos e após a verificação, constata-se que também não há duplicatas). 

3.  São removidos os espaços em branco das colunas.

|index|User\_ID|Name|Age|Country|Subscription\_Type|Watch\_Time\_Hours|Favorite\_Genre|Last\_Login|
|---|---|---|---|---|---|---|---|---|
|0|1|James Martinez|18|France|Premium|80\.26|Drama|2024-05-12|
|1|2|John Miller|23|USA|Premium|321\.75|Sci-Fi|2025-02-05|
|2|3|Emma Davis|60|UK|Basic|35\.89|Comedy|2025-01-24|
|3|4|Emma Miller|44|USA|Premium|261\.56|Documentary|2024-03-25|
|4|5|Jane Smith|68|USA|Standard|909\.3|Drama|2025-01-14|

4. A coluna 'Name' é padronizada para facilitar a visualização.

5. Como apontado na parte da Extração, a coluna 'Last_Login' precisava ser convertida para o tipo de dado 'datetime' para permitir análises baseadas em tempo. Para isso foi utilizado o script 'df['Last_Login'] = pd.to_datetime(df['Last_Login'])'. 

6. Finalizamos com a padronização dos nomes das colunas com 'df.rename()' de modo que fique mais fácil para um entendimento consistente dos dados. 

---

## Considerações finais

1. Os dados foram limpos e padronizados.
2. Todos os problemas apontados na parte de Extração foram sanados, permitindo melhor visualização e consistência nas informações. 
3. As colunas foram renomeadas e agrupadas por: ID, nome, idade, país, assinatura, horas assistidas e gênero. 

