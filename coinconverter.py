import random
import string

def gerar_senha(comprimento=12, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Você deve selecionar pelo menos um tipo de caractere.")

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

if __name__ == "__main__":
    print("=== Gerador de Senhas Seguras ===")
    tamanho = int(input("Comprimento da senha (ex: 12): "))
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_digitos = input("Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    try:
        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_digitos, usar_simbolos)
        print(f"\nSenha gerada: {senha}")
    except ValueError as e:
        print(f"Erro: {e}")
