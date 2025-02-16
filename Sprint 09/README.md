# README SPRINT 9 - Desafio Etapa 4 (Camada Refined)

Nesta sprint, realizamos a execução do desafio para criar a camada Refined do Data Lake. Durante esta etapa, os dados oriundos da camada Trusted (armazenados em arquivos Parquet no S3) foram transformados e organizados em um modelo dimensional (esquema estrela), utilizando AWS Glue e Apache Spark. Além disso, um crawler foi configurado e executado para atualizar o Glue Data Catalog, permitindo a consulta via AWS Athena e a criação de dashboards com AWS QuickSight.

## Principais Atividades

- **Transformação dos Dados:**  
  - Leitura de múltiplos arquivos Parquet da Trusted Zone.
  - Aplicação de transformações para criar as tabelas:
    - **FatoMidia:** Contendo métricas (nota média, número de votos) e referências às dimensões.
    - **DimMidia, DimTempo, DimArtista, DimGenero:** Armazenando informações sobre títulos, datas, artistas e gêneros.
    - **BridgeMidiaGenero e BridgeMidiaArtista:** Para associar títulos com gêneros e artistas.
  - Escrita dos dados transformados na camada Refined, em formato Parquet com particionamento.

- **Atualização do Glue Data Catalog:**  
  - Criação e execução de um crawler para registrar as novas tabelas e schemas.

## Execução do Desafio

- O job AWS Glue foi executado com sucesso, transformando os dados e salvando-os na camada Refined.
- O crawler foi criado e executado, atualizando o Glue Data Catalog para que os dados possam ser consultados via Athena e visualizados no QuickSight.

## Documentação Completa

Para mais detalhes sobre a modelagem de dados, o código do job AWS Glue, a configuração do crawler e demais instruções, consulte o [README completo](../Sprint%2009/Desafio/README.md).

