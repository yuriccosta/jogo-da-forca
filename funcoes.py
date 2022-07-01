# Feito por zzAlfa / Versão 1.0

def forca(palavra='', trys=None, points=0):
    def letras():
        tabel = []
        for c in range(0, len(palavra)):
            tabel.append('_')
        for c in range(0, len(palavra)):
            for p in range(0, len(trys)):
                if palavra[c] == trys[p]:
                    if len(tabel) == 0:
                        tabel.append(trys[p])
                    else:
                        tabel.pop(c)
                        tabel.insert(c, trys[p])
        tabelstr = ''
        for c in range(0, len(tabel)):
            tabelstr = tabelstr + tabel[c] + ' '

        return tabelstr

    if points == 4:
        print(f'Número de vidas: {points}')
        print(f'Número de palavras: {len(palavra)}')
        print(f'Letras tentadas: {trys}')
        print(fr'''{'=' * 30}
('_')
 (|)
 / \
/   \
''')
        print(letras())
        print(f"{'=' * 30}")
    elif points == 3:
        print(f'Número de vidas: {points}')
        print(f'Número de palavras: {len(palavra)}')
        print(f'Letras tentadas: {trys}')
        print(fr'''{'=' * 30}
('_')
 (|)
 / \
''')
        print(letras())
        print(f"{'=' * 30}")
    elif points == 2:
        print(f'Número de vidas: {points}')
        print(f'Número de palavras: {len(palavra)}')
        print(f'Letras tentadas: {trys}')
        print(f'''{'=' * 30}
('_')
 (|)
''')
        print(letras())
        print(f"{'=' * 30}")
    elif points == 1:
        print(f'Número de vidas: {points}')
        print(f'Número de palavras: {len(palavra)}')
        print(f'Letras tentadas: {trys}')
        print(f"{'=' * 30}")
        print("('_')")
        print(letras())
    elif points == 0:
        print(f'Número de vidas: {points}')
        print(f'Número de palavras: {len(palavra)}')
        print(f'Letras tentadas: {trys}')
        print(f"{'=' * 30}")
        print("(X_X)")
        print(letras())
        print(f"{'=' * 30}")

