#!/bin/bash

# Caminho onde estão os arquivos de relatório
backup_dir=~/ecommerce/vendas/backup

# Arquivo final consolidado
final_report=~/ecommerce/relatorio_final.txt

# Limpa o arquivo final consolidado antes de começar
> $final_report

# Percorre cada relatório no diretório de backup e adiciona ao arquivo final
for report in "$backup_dir"/relatorio*.txt; do
    if [[ -f "$report" ]]; then
        cat "$report" >> $final_report
        echo -e "\n-------------------\n" >> $final_report
    fi
done
