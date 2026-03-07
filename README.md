# 📊 Projeto Integrador – Desenvolvimento Low Code em Ciência de Dados

Repositório desenvolvido para o **Projeto Integrador da disciplina Desenvolvimento Low Code em Ciência de Dados – SENAC**.

O projeto tem como objetivo implementar um **processo de ETL (Extract, Transform, Load)** utilizando **Python e Pandas**, além da criação de um **dashboard interativo com Streamlit** para análise de dados de usuários da Netflix.

---

# 👥 Integrantes do Grupo

- **Integrante 1** – Gestão de Repositório  
- **Integrante 2** – Engenharia de Dados (Extração)  
- **Integrante 3** – Análise de Dados (Transformação com Pandas)  
- **Integrante 4** – Limpeza e Padronização de Dados  
- **Integrante 5** – Desenvolvimento do Dashboard (Layout Streamlit)  
- **Integrante 6** – Desenvolvimento do Dashboard (Visualizações)  
- **Integrante 7** – Documentação e Qualidade (QA)

---

# 📂 Estrutura do Repositório


**data/**  
Armazena a base de dados original e a base tratada após o processo ETL.

**src/**  
Contém o script responsável pela implementação do processo de ETL utilizando Python e Pandas.

**app/**  
Contém a aplicação desenvolvida com Streamlit para visualização dos dados.

---

# 📊 Base de Dados

Fonte: Kaggle  

Dataset utilizado:  
https://www.kaggle.com/datasets/shivamb/netflix-shows

### Descrição

A base contém informações relacionadas ao comportamento de usuários da Netflix, incluindo:

- Identificador de usuário
- Idade
- Tipo de plano (Básico, Padrão ou Premium)
- Total de horas assistidas
- Gênero preferido
- Data do último login

Esses dados permitem análises sobre perfil de usuários, preferências de conteúdo e padrões de consumo da plataforma.

---

# 🎯 Objetivo da Análise

Aplicar o processo de **ETL** para transformar dados brutos em informações estruturadas e utilizá-las na construção de um **dashboard interativo**.

A análise busca identificar:

- Distribuição de usuários por faixa etária
- Planos mais utilizados
- Relação entre idade e tempo de uso da plataforma
- Preferências de gênero de conteúdo

---

# 🔄 Planejamento do Processo ETL

**Extract**

- Leitura da base original em formato CSV
- Importação dos dados utilizando Pandas

**Transform**

- Limpeza de valores nulos
- Padronização de colunas
- Conversão de tipos de dados
- Organização estrutural das informações

**Load**

- Exportação da base tratada
- Utilização dos dados tratados no dashboard Streamlit

---

# 📈 Planejamento do Dashboard

O dashboard será desenvolvido utilizando **Streamlit** e apresentará visualizações interativas baseadas na base tratada.

### Métricas principais

- Idade média dos usuários
- Total de assinantes por país
- Média de horas assistidas

### Visualizações planejadas

- **Gráfico de pizza** – Distribuição dos tipos de plano  
- **Gráfico de barras** – Relação entre idade e horas assistidas  
- **Filtros interativos** – Tipo de plano e data de último acesso

---

# 📅 Cronograma de Desenvolvimento

| Período | Atividade |
|-------|-------|
| Até 28/02 | Criação e organização do repositório |
| Até 06/03 | Definição da base de dados e contextualização |
| 07/03 – 14/03 | Planejamento do processo ETL |
| 15/03 – 20/03 | Planejamento do dashboard |
| 21/03 – 22/03 | Revisão da documentação |
| 23/03/2026 | Entrega da Etapa 1 |

---

# 🚀 Tecnologias Utilizadas

- Python  
- Pandas  
- Streamlit  
- Git e GitHub  

---

# 📌 Etapas do Projeto

1. Definição da base de dados
2. Implementação do processo ETL
3. Tratamento e organização dos dados
4. Desenvolvimento do dashboard interativo
5. Documentação e publicação do projeto
