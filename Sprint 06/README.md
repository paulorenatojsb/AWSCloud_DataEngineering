# README Sprint 1

```markdown
# Sprint 1 - Projeto de Processamento de Vendas

## Visão Geral da Sprint

A Sprint 1 marcou o início do estágio e teve como foco o desenvolvimento de habilidades essenciais para automação de tarefas, controle de versão e metodologias ágeis. O objetivo principal foi o desenvolvimento de um projeto prático: um sistema de processamento de vendas utilizando Linux e Shell Script. O projeto, entregue como atividade final da sprint, aplicou conceitos e ferramentas abordadas nas primeiras semanas.

## Conteúdos e Ferramentas

Durante essas duas primeiras semanas, o aprendizado foi consolidado principalmente através da plataforma **Udemy**, com os seguintes tópicos:

- **Linux**: Exploração do ambiente Linux, incluindo comandos essenciais, estrutura de diretórios, permissões e manipulação de arquivos.
- **Shell Script**: Aprendemos a criar scripts em Linux, com o intuito de automatizar processos e manipular arquivos. O projeto de processamento de vendas foi a primeira aplicação prática desses conceitos.
- **Git e GitHub**: Conhecimento sobre controle de versão, que é essencial para colaboração em projetos. Aprendemos desde os comandos básicos de Git até o uso do GitHub para gerenciar versões e realizar revisões de código.
- **Metodologias Ágeis**: Introdução ao universo das metodologias ágeis, discutindo sua importância, princípios e algumas práticas utilizadas em equipes de desenvolvimento.

## Projeto de Processamento de Vendas

O projeto final da sprint foi um sistema de **processamento de vendas** desenvolvido em Shell Script, com o objetivo de:

1. **Automatizar a organização e backup de arquivos de vendas**.
2. **Gerar relatórios diários e consolidá-los em um relatório final**, facilitando a análise das vendas.

### Estrutura do Projeto

- **Scripts Principais**:
    - `processamento_de_vendas.sh`: Automatiza o processamento dos arquivos de vendas, criando backups diários e gerando relatórios individuais para cada dia.
    - `consolidador_de_processamento_de_vendas.sh`: Consolida os relatórios diários em um único arquivo, facilitando a análise e o acesso ao histórico de vendas.

- **Diretórios e Arquivos**:
    - Diretório `ecommerce/`: Contém os arquivos principais de vendas (`dados_de_venda.csv`) e backups diários.
    - Diretório `ecommerce/vendas/backup`: Armazena arquivos de relatório (`relatorio-<data>.txt`) e um arquivo consolidado (`relatorio_final.txt`).

### Execução dos Scripts

- Os scripts foram executados em ambiente Linux, diretamente na linha de comando, com permissões de execução configuradas.
- O agendamento do `processamento_de_vendas.sh` foi feito no **crontab**, garantindo que a tarefa seja executada automaticamente em horários predefinidos.

## Reflexão sobre a Sprint

Esta sprint proporcionou uma base sólida em Linux e Shell Script, e a criação do projeto de processamento de vendas permitiu aplicar o que foi aprendido de forma prática. A introdução às metodologias ágeis também foi valiosa para o entendimento do fluxo de trabalho em equipe, trazendo um entendimento inicial sobre organização de tarefas e entregas.