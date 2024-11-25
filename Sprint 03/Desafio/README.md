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

![Evidencia 1](../Evidências/Evidencia%20Desafio%20Sprint%203-v2.png)

### 2. Limpeza e Preparação dos Dados
1. **Remoção de Linhas Duplicadas**:
   - O dataset foi limpo para eliminar duplicatas, garantindo que os dados fossem únicos.
2. **Conversão de Colunas**:
   - Colunas como `Installs` e `Price` foram convertidas para valores numéricos após a remoção de caracteres especiais (`+`, `,`, `$`).
3. **Tratamento de Valores Inválidos**:
   - Valores ausentes ou inválidos foram tratados, garantindo consistência nos dados analisados.

![Evidencia 2](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(1).png)

### 3. Análises Realizadas

#### 3.1. Gráficos
1. **Gráfico de Barras - Top 5 Apps Mais Instalados**:
   - Gerado para destacar os 5 aplicativos com o maior número de instalações.

![Evidencia 3](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(2).png)

2. **Gráfico de Pizza - Distribuição por Categoria**:
   - Para o gráfico pizza, realizei 2 versões diferentes, pois sem agrupar as categorias com menor % (< 2.3%>) parte do gráfico ficava ilegível. Por isso, fiz uma segunda visualização, com a criação do "Outros".

Versão 1 ![Evidencia 4](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(3).png)

Versão 2 ![Evidencia 5](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(4).png)

#### 3.2. Cálculos e Insights
1. **App Mais Caro**:
   - Identificado o app com o maior preço no dataset.
![Evidencia 8](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(5).png)

2. **Apps 'Mature 17+'**:
   - Sumarizando o número de aplicativos classificados como `Mature 17+`.
![Evidencia 9](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(7).png)

3. **Top 10 Apps por Reviews**:
   - Selecionados os 10 aplicativos mais avaliados, exibidos em ordem decrescente.
![Evidencia 10](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(8).png)

#### 3.3. Cálculos e Insights Adicionais

1. **Média de Preço dos Apps** e 2. **Total de Instalações**
![Evidencia 11](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(9).png)

3. **Top 10 Apps por número de reviews**:
![Evidencia 12](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(10).png)

4. **Top 5 Apps Pagos Mais Baixados**
![Evidencia 13](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(11).png)

5. **Gráfico de linha - média de instalações por categoria**:
![Evidencia 14](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(13).png)

6. **Gráfico de Disperção - relação entre preço e número de reviews**:
   - Calculada a média do preço dos aplicativos disponíveis.
![Evidencia 15](../Evidências/Evidencias%20Desafio%20-%20Sprint%203%20(12).png)

### 4. Ferramentas Utilizadas
- **Python**:
  - Linguagem principal para a manipulação e análise de dados.
- **Jupyter Notebook**:
  - Ambiente interativo para execução do código e documentação.
- **Biblioteca Pandas**:
  - Para a manipulação e processamento dos dados do dataset.
- **Biblioteca Matplotlib**:
  - Para a criação dos gráficos utilizados na análise.

---

## Considerações Finais
O projeto foi desenvolvido para trabalhar e praticar a programação e análise de dados utilizando a linguagem **Python**. As etapas foram realizadas de forma modular para facilitar a compreensão.

EO código completo e os gráficos gerados estão disponíveis no arquivo `.ipynb`.