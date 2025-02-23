#!/bin/bash

# Nome do script de ordenação
script_ordenacao="./$1"
arquivo_entrada="$2"  

rm -Rf *ordenado* *.log

if [ ! -f "$script_ordenacao" ]; then
    echo "Erro: Script de ordenação '$script_ordenacao' não encontrado."
    exit 1
fi

if [ ! -f "$arquivo_entrada" ]; then
    echo "Erro: Arquivo de entrada '$arquivo_entrada' não encontrado."
    exit 1
fi

logfile="tempo_execucao.log"
echo "Execução | Tempo (ms)" > "$logfile"

for ((i=1; i<=30; i++)); do
    echo "Executando tentativa $i..."

    inicio=$(date +%s%3N)  # Tempo inicial em milissegundos
    python $script_ordenacao "$arquivo_entrada" > /dev/null  # Executa o script e descarta a saída padrão
    fim=$(date +%s%3N)  # Tempo final em milissegundos

    tempo_execucao=$((fim - inicio))  # Calcula tempo total
    echo "$i | $tempo_execucao" >> "$logfile"
done

echo "Execuções concluídas! Veja os tempos em '$logfile'"
echo "#################################"
cat $logfile |awk '{print $3}'
echo "#################################"
