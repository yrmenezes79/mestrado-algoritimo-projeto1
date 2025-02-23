import sys
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontra o índice do menor elemento na parte não ordenada
        indice_menor = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
        arr[i], arr[indice_menor] = arr[indice_menor], arr[i]

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <arquivo_de_entrada>")
        sys.exit(1)

    arquivo = sys.argv[1]

    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        sys.exit(1)

    conteudo = conteudo.replace('.', '').replace('-', '')

    numeros = [int(num) for num in conteudo.split()]  # Converte para inteiros

    data_inicio = time.strftime("%Y-%m-%d %H:%M:%S")
    inicio = time.time() * 1000  # Tempo em milissegundos

    # Implementação do Selection Sort
    selection_sort(numeros)

    arquivo_saida = f"ordenado_{arquivo}"
    with open(arquivo_saida, 'w') as f:
        f.write("Ordenando...\n")
        for num in numeros:
            f.write(f"{num}\n")

    data_fim = time.strftime("%Y-%m-%d %H:%M:%S")
    fim = time.time() * 1000  # Tempo em milissegundos

    tempo_total = fim - inicio
    with open("tempo1000_selecao", 'a') as f:
        f.write(f"{tempo_total:.0f} milissegundos\n")

if __name__ == "__main__":
    main()
