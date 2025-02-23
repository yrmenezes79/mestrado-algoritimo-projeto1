import sys
import time

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        trocou = False  # Flag para verificar se houve trocas
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True  # Indica que houve troca
        if not trocou:  # Se não houve trocas, o array já está ordenado
            break

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

    # Converte o conteúdo em uma lista de números
    numeros = conteudo.split()

    data_inicio = time.strftime("%Y-%m-%d %H:%M:%S")
    inicio = time.time() * 1000  # Tempo em milissegundos

    optimized_bubble_sort(numeros)

    arquivo_saida = f"ordenado_{arquivo}"
    with open(arquivo_saida, 'w') as f:
        f.write("Ordenando...\n")
        for num in numeros:
            f.write(f"{num}\n")

    data_fim = time.strftime("%Y-%m-%d %H:%M:%S")
    fim = time.time() * 1000  # Tempo em milissegundos

    # Calcula o tempo total
    tempo_total = fim - inicio
    with open("tempo1000_bolha_otimizado", 'a') as f:
        f.write(f"{tempo_total:.0f} milissegundos\n")

if __name__ == "__main__":
    main()
