import sys
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Verifica se o arquivo foi passado como argumento
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

    # Remove pontos e traços do conteúdo
    conteudo = conteudo.replace('.', '').replace('-', '')

    # Converte o conteúdo em uma lista de números
    numeros = conteudo.split()

    # Registra o início do processo
    data_inicio = time.strftime("%Y-%m-%d %H:%M:%S")
    inicio = time.time() * 1000  

    # Implementação do Bubble Sort
    bubble_sort(numeros)

    arquivo_saida = f"ordenado_{arquivo}"
    with open(arquivo_saida, 'w') as f:
        f.write("Ordenando...\n")
        for num in numeros:
            f.write(f"{num}\n")

    data_fim = time.strftime("%Y-%m-%d %H:%M:%S")
    fim = time.time() * 1000  # Tempo em milissegundos

    tempo_total = fim - inicio
    with open("tempo1000_bolha", 'a') as f:
        f.write(f"{tempo_total:.0f} milissegundos\n")

if __name__ == "__main__":
    main()
