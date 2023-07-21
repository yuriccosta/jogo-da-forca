# Feito por zzAlfa / Versão 2.0

# Printa o corpo do boneco, a vida e a palavra do jogo
def printforca(life=0, oculta=[], trys=[]):
    boneco = ["('_')", " /|\\", "  |", " / \\"]

    print("=" * 20)
    for c in range(0, life):
        print(' ' * 6, boneco[c])
    if life == 0:
        print("(X_X)")

    print(f"Vida: {life}", end=' ' * 5)
    print("Palavra: ", end='')
    for c in oculta:
        print(c, end=' ')
    print("Suas tentativas: ", trys)
    print()
