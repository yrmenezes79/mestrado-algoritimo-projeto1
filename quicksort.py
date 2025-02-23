import sys
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Caso base da recursão

    pivo = arr[len(arr) // 2]  # Escolhe o pivô como o elemento do meio
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)

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

    numeros = quick_sort(numeros)

    arquivo_saida = f"ordenado_{arquivo}"
    with open(arquivo_saida, 'w') as f:
        f.write("Ordenando...\n")
        for num in numeros:
            f.write(f"{num}\n")
    data_fim = time.strftime("%Y-%m-%d %H:%M:%S")
    fim = time.time() * 1000  # Tempo em milissegundos
    tempo_total = fim - inicio
    with open("tempo1000_quick", 'a') as f:
        f.write(f"{tempo_total:.0f} milissegundos\n")

if __name__ == "__main__":
    main()
