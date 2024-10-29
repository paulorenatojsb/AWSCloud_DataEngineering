#!/bin/bash

# Criação dos diretórios e cópia do arquivo
mkdir -p ~/ecommerce/vendas/backup
cp ~/ecommerce/dados_de_vendas.csv ~/ecommerce/vendas/

# Obter a data atual no formato yyyymmdd
data=$(date +%Y%m%d)

# Copiar o arquivo para o diretório backup com o nome incluindo a data
cp ~/ecommerce/vendas/dados_de_vendas.csv ~/ecommerce/vendas/backup/dados-$data.csv

# Renomear o arquivo para o padrão 'backup-dados-<yyyymmdd>.csv'
mv ~/ecommerce/vendas/backup/dados-$data.csv ~/ecommerce/vendas/backup/backup-dados-$data.csv

# Criar o arquivo relatorio.txt no diretório backup
relatorio=~/ecommerce/vendas/backup/relatorio-$data.txt

# Informações no relatorio.txt
echo "Data do Sistema: $(date '+%Y/%m/%d %H:%M')" > $relatorio
echo "Data do primeiro registro: $(head -n 2 ~/ecommerce/vendas/dados_de_vendas.csv | tail -n 1 | cut -d ',' -f5)" >> $relatorio
echo "Data do último registro: $(tail -n 1 ~/ecommerce/vendas/dados_de_vendas.csv | cut -d ',' -f5)" >> $relatorio
echo "Quantidade total de itens vendidos: $(cut -d ',' -f2 ~/ecommerce/vendas/dados_de_vendas.csv | sed '1d' | sort | uniq | wc -l)" >> $relatorio

# Incluir as primeiras 10 linhas do arquivo renomeado no relatorio.txt
echo "Primeiras 10 linhas do arquivo:" >> $relatorio
head -n 10 ~/ecommerce/vendas/backup/backup-dados-$data.csv >> $relatorio

# Compactar o arquivo
zip ~/ecommerce/vendas/backup/backup-dados-$data.zip ~/ecommerce/vendas/backup/backup-dados-$data.csv

# Apagar os arquivos desnecessários
rm ~/ecommerce/vendas/backup/backup-dados-$data.csv
rm ~/ecommerce/vendas/dados_de_vendas.csv
