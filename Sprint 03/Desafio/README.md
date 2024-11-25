# Desafio da Sprint 3 - ETL e Análise em Python do googleplayestro.csv

## Objetivo
Este desafio foi realizado com o intuito de praticar e consolidar conhecimentos adquiridos durante a sprint, utilizando a linguagem Python para realizar a ETL (extract, transform, load), analisar dados e gerar visualizações gráficas.

---

## Descrição do Desafio
No desafio precisei processar um arquivo .CSV contendo dados de aplicativos da Google Play Store. A análise incluiu a limpeza de dados, cálculos relacionados e a criação de gráficos para exibir os resultados de forma visual.

## Etapas do Desenvolvimento

### 1. Preparação
1. O arquivo `googleplaystore.csv` foi baixado e armazenado na máquina local.
2. O ambiente foi configurado no Jupyter Notebook, com as bibliotecas `pandas` e `matplotlib` instaladas.

![Evidencia 1] ()

### 2. Limpeza e Preparação dos Dados
1. **Remoção de Linhas Duplicadas**:
   - O dataset foi limpo para eliminar duplicatas, garantindo que os dados fossem únicos.
2. **Conversão de Colunas**:
   - Colunas como `Installs` e `Price` foram convertidas para valores numéricos após a remoção de caracteres especiais (`+`, `,`, `$`).
3. **Tratamento de Valores Inválidos**:
   - Valores ausentes ou inválidos foram tratados, garantindo consistência nos dados analisados.

---

### 3. Análises Realizadas

#### 3.1. Gráficos
1. **Gráfico de Barras - Top 5 Apps Mais Instalados**:
   - Gerado para destacar os 5 aplicativos com o maior número de instalações.
2. **Gráfico de Pizza - Distribuição por Categoria**:
   - Mostra a proporção de categorias no dataset, agrupando categorias com menos de 2.3% de frequência em "Outros".
3. **Gráficos Adicionais**:
   - Gráfico de linha exibindo a média de instalações por categoria.
   - Gráfico de dispersão mostrando a relação entre o preço dos aplicativos e o número de reviews.

#### 3.2. Cálculos e Insights
1. **App Mais Caro**:
   - Identificado o app com o maior preço no dataset.
2. **Apps 'Mature 17+'**:
   - Contado o número de aplicativos classificados como `Mature 17+`.
3. **Top 10 Apps por Reviews**:
   - Selecionados os 10 aplicativos mais avaliados, exibidos em ordem decrescente.
4. **Top 5 Apps Pagos Mais Baixados**:
   - Identificados os 5 aplicativos pagos mais baixados, com destaque para o número de instalações e o preço.
5. **Média de Preço dos Apps**:
   - Calculada a média do preço dos aplicativos disponíveis.

---

### 4. Ferramentas Utilizadas
- **Python**:
  - Linguagem principal para a manipulação e análise de dados.
- **Jupyter Notebook**:
  - Ambiente interativo para execução do código e documentação.
- **Pandas**:
  - Para a manipulação e processamento dos dados do dataset.
- **Matplotlib**:
  - Para a criação dos gráficos utilizados na análise.

---

### 5. Resultados
O desafio resultou em:
1. **Visualizações Gráficas**:
   - Gráficos informativos sobre categorias, instalações e correlações entre preço e reviews.
2. **Insights Significativos**:
   - Identificação de aplicativos mais populares, mais caros e mais avaliados.
3. **Documentação**:
   - Um arquivo Jupyter Notebook contendo todo o código necessário para replicar os resultados.

---

## Considerações Finais
O projeto foi desenvolvido com foco em boas práticas de programação e análise de dados. As etapas foram realizadas de forma modular para facilitar a reprodutibilidade e a compreensão.

Este arquivo README.md serve como guia para o avaliador entender o que foi realizado durante o desafio. O código completo e os gráficos gerados estão disponíveis no arquivo `.ipynb`.