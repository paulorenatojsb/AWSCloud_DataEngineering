# README DESAFIO SPRINT 1 - Processamento de Vendas

```markdown

Este projeto automatiza o processamento e a consolidação de relatórios de vendas, organizando arquivos de backup e consolidando-os em um relatório final. Este documento fornece uma descrição dos passos para configurar, executar e verificar os resultados gerados pelos scripts `processamento_de_vendas.sh` e `consolidador_de_processamento_de_vendas.sh`.

[LINK PARA O VIDEO DO DESAFIO](https://compasso-my.sharepoint.com/personal/paulo_braga_pb_compasso_com_br/_layouts/15/stream.aspx?id=%2Fpersonal%2Fpaulo%5Fbraga%5Fpb%5Fcompasso%5Fcom%5Fbr%2FDocuments%2FPauloRenato%2EBraga%2DSprint01%2Ewebm&nav=%7B%22defaultNavPanel%22%3A%7B%22pluginName%22%3A%22MediaSettingsLayer%22%7D%7D&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ebd30914d%2D8f79%2D4c62%2D8114%2Dde587291f97b)

## Estrutura do Projeto e Arquivos

### Estrutura de Diretórios

O projeto está organizado com os scripts principais na pasta `home`, enquanto os dados e backups de vendas estão dentro do diretório `ecommerce`, conforme a estrutura a seguir:

```
~/
├── processamento_de_vendas.sh                  # Script para processamento de vendas e criação de backups
├── consolidador_de_processamento_de_vendas.sh  # Script para consolidação dos backups
├── ecommerce/
│   ├── dados_de_venda.csv                      # Arquivo principal de dados de vendas
│   ├── dados_de_venda20241025.csv              # Arquivos de vendas com data no nome (backup diário)
│   ├── dados_de_venda20241026.csv
│   ├── dados_de_venda20241027.csv
│   ├── relatorio_de_vendas.txt                 # Relatório final consolidado das vendas
│   └── vendas/
│       ├── backup/                             # Diretório com backups diários e relatórios
│       │   ├── relatorio-20241025.txt
│       │   ├── relatorio-20241026.txt
│       │   ├── relatorio-20241027.txt
│       │   ├── relatorio-20241028.txt
│       │   └── relatorio_final.txt             # Arquivo consolidado de todos os relatórios
│       └── backup-dados-*.zip                  # Arquivos zip com backup de dados diários
```

### Descrição dos Arquivos e Scripts

- **dados_de_venda.csv**: Arquivo inicial contendo registros de vendas.
- **processamento_de_vendas.sh**: Gera cópias de backup do arquivo `dados_de_venda.csv`, salva-os no formato `dados_de_venda<yyyymmdd>.csv` em `ecommerce/`, e cria relatórios individuais (`relatorio-<yyyymmdd>.txt`) no diretório `backup`.
- **consolidador_de_processamento_de_vendas.sh**: Percorre todos os arquivos `relatorio-*.txt` no diretório `backup` e gera um arquivo consolidado `relatorio_final.txt`.

### Estrutura dos Arquivos de Backup e do Relatório Consolidado

- Os arquivos de backup de vendas são salvos como `dados_de_venda<yyyymmdd>.csv` no diretório `ecommerce/`.
- Cada relatório diário é salvo no formato `relatorio-<data>.txt` dentro de `ecommerce/vendas/backup`.
- O relatório consolidado é gerado como `relatorio_final.txt` no diretório `backup`.

## Configuração e Execução

### Passo 1: Configurar Diretórios e Permissões

Certifique-se de que os diretórios e arquivos estão na estrutura correta e que os scripts tenham permissões de execução:
```bash
chmod +x ~/processamento_de_vendas.sh
chmod +x ~/consolidador_de_processamento_de_vendas.sh
```

### Passo 2: Executar o Script de Processamento de Vendas

Para gerar arquivos de backup e relatórios, execute:
```bash
~/processamento_de_vendas.sh
```
[Evidencia 1](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(1).png)

[Evidencia 3](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(3).png)

[Evidencia 4](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(4).png)

Esse comando realiza as seguintes ações:
1. Cria um backup de `dados_de_venda.csv` em `ecommerce/` com a data no nome.
2. Gera um relatório diário `relatorio-<data>.txt` no diretório `backup`.

[Evidencia 6](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(6).png)

### Passo 3: Agendar Execução Automática com Cron

Para agendar o script `processamento_de_vendas.sh` para execução diária às 15h27, adicione-o ao `crontab`:
```bash
crontab -e
```

Adicione a linha abaixo ao `crontab`:
```bash
27 15 * * * ~/processamento_de_vendas.sh
```

### Passo 4: Executar o Script de Consolidação de Relatórios

Para consolidar os arquivos de relatórios, execute:
```bash
~/consolidador_de_processamento_de_vendas.sh
```
[Evidencia 2](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(2).png)

Esse comando:
1. Percorre todos os arquivos `relatorio-*.txt` em `backup/`.
2. Copia o conteúdo de cada arquivo para `relatorio_final.txt` em `~/ecommerce/vendas/backup`, separando cada arquivo com uma linha `-------------------`.

### Verificação dos Resultados

- **Arquivos de Backup**: Os backups diários e relatórios estão em `~/ecommerce` e `~/ecommerce/vendas/backup`.
- **Relatório Consolidado**: O arquivo consolidado estará em `~/ecommerce/vendas/backup/relatorio_final.txt`.

### Exemplo de Conteúdo dos Arquivos

- **Exemplo de `dados_de_venda.csv`**:
    ```
    id,produto,quantidade,preco,data
    1,camiseta,2,50.00,15/05/2023
    2,notebook,1,2500.00,20/06/2023
    ```

[Evidencia 5](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(5).png)

[Evidencia 7](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(7).png)

- **Exemplo de `relatorio_final.txt`**:
    ```
    Data do Sistema: 2024/10/27 15:27
    Data do primeiro registro: 15/05/2023
    Data do último registro: 20/06/2023
    Quantidade total de itens vendidos: 2
    -------------------
    [conteúdo do próximo relatório]
    ```
[Evidencia 8](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2001/Evid%C3%AAncias/Evidencia%20Desafio%20Sprint1%20(8).png)