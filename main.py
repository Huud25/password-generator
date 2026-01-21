from secrets import choice

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"

def generate_password(length: int, use_symbols: bool = True, use_numbers: bool = True) -> str:
    alphabet = UPPER + LOWER

    if use_numbers:
        alphabet += DIGITS
    if use_symbols:
        alphabet += SYMBOLS

    return "".join(choice(alphabet) for _ in range(length))

def main():
    print("Password Generator - v1")

    length_str = input("Tamanho da senha (ex: 16): ").strip()
    if not length_str.isdigit():
        print("Erro: digite um número.")
        return

    length = int(length_str)
    if length < 8:
        print("Aviso: 8+ é recomendado (ideal 12+).")

    pw = generate_password(length=length, use_symbols=True, use_numbers=True)
    print("\nGenerated password:")
    print(pw)

if __name__ == "__main__":
    main()
