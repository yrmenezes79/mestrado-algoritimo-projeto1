import random

def gerar_cpf():
    """Gera um CPF válido aleatório."""
    def calcular_digito(cpf_parcial):
        soma = sum(int(cpf_parcial[i]) * (10 - i) for i in range(9))
        digito = 11 - (soma % 11)
        return str(digito if digito < 10 else 0)

    nove_digitos = [str(random.randint(0, 9)) for _ in range(9)]
    primeiro_digito = calcular_digito(nove_digitos)
    segundo_digito = calcular_digito(nove_digitos + [primeiro_digito])

    return "{}.{}.{}-{}".format(
        "".join(nove_digitos[:3]), "".join(nove_digitos[3:6]), "".join(nove_digitos[6:9]), primeiro_digito + segundo_digito
    )

def gerar_arquivo_cpfs(nome_arquivo, quantidade):
    """Gera um arquivo contendo CPFs válidos."""
    with open(nome_arquivo, "w") as f:
        for _ in range(quantidade):
            f.write(gerar_cpf() + "\n")

# Gerar um arquivo com 10000 CPFs
gerar_arquivo_cpfs("cpfs.txt", 100000)
print("Arquivo 'cpfs.txt' gerado com sucesso!")
