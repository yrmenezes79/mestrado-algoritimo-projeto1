import sys
import time

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        # Recursivamente ordena as duas metades
        merge_sort(esquerda)
        merge_sort(direita)

        # Combina as metades ordenadas
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

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

    merge_sort(numeros)

    arquivo_saida = f"ordenado_{arquivo}"
    with open(arquivo_saida, 'w') as f:
        f.write("Ordenando...\n")
        for num in numeros:
            f.write(f"{num}\n")

    data_fim = time.strftime("%Y-%m-%d %H:%M:%S")
    fim = time.time() * 1000  # Tempo em milissegundos

    tempo_total = fim - inicio
    with open("tempo1000_merge", 'a') as f:
        f.write(f"{tempo_total:.0f} milissegundos\n")

if __name__ == "__main__":
    main()
