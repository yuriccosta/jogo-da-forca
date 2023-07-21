# Feito por zzAlfa / Versão 2.0

import random
import time
import funcoes as fc

wins = 0
while True:
    # Menu
    print('Bem vindo ao Jogo da Forca!!!')
    print('*' * 20)
    print(f'Número de vitórias: {wins}')
    print('*' * 20)
    print('''Temas disponíveis:
    (1) Frutas
    (2) Cidades
    (3) Animais

    (0) Sair
    ''')

    # Pega a escolha do jogador e valida
    while True:
        try:
            esc = int(input('Selecione o modo de jogo: '))
        except ValueError:
            print('Tente digitar um número inteiro: ')
        else:
            break

    '''
    life = vida do jogador, oculta = palavra oculta, trys = todas as tentativas do jogador
    points = pontos de acerto do jogador
    '''
    life = 4
    oculta = []
    trys = []
    points = 0

    # Escolha dos temas
    if esc == 1:
        fruta = ['MAÇÃ', 'BANANA', 'UVA']
        print('Bem vindo ao tema de frutas!!!')
        palavra = fruta[random.randint(0, len(fruta) - 1)]

    elif esc == 2:
        cidades = ['ARACAJU', 'BELO HORIZONTE', 'BOA VISTA', 'BRASÍLIA', 'CAMPO GRANDE', 'CUIABÁ', 'FLORIANÓPOLIS',
                   'FORTALEZA''GOIÂNIA', 'JOÃO PESSOA', 'MACAPÁ', 'MACEIÓ', 'MANAUS', 'NATAL', 'PALMAS', 'PORTO ALEGRE',
                   'PORTO VELHO', 'RECIFE', 'RIO BRANCO', 'RIO DE JANEIRO', 'SALVADOR', 'SÃO LUÍS', 'SÃO PAULO',
                   'TERESINA',
                   'VITÓRIA']
        print('Bem vindo ao tema de cidades!!!')
        palavra = cidades[random.randint(0, len(cidades) - 1)]

    elif esc == 3:
        animais = ['TIGRE', 'LOBO', 'JACARÉ', 'ONÇA-PINTADA', 'ARARA', 'CARANGUEIJO', 'CACHORRO', 'LEÃO']
        print('Bem vindo ao tema de animais!!!')
        palavra = animais[random.randint(0, len(animais) - 1)]

    else:
        print('Até a próxima')
        break

    # Transforma a palavra sorteada em uma palavra oculta, ignorando os espaços e hifens
    for c in palavra:
        if c == ' ':
            oculta.append(" ")
            points += 1
        elif c == '-':
            oculta.append("-")
            points += 1
        else:
            oculta.append("_")

    while True:
        fc.printforca(life, oculta, trys)
        letra = input("Digite sua tentativa!: ").upper()

        # Verifica se a tentativa está na palavra do jogo
        while True:
            if len(letra) > 1 or letra in " -":
                letra = input("Digite apenas uma letra!: ").upper()
            elif letra in trys:
                letra = input("Você já digitou essa letra, tente outra!: ").upper()
            else:
                break

        trys.append(letra)

        # Acrescenta a letra tentada na palavra oculta e os pontos de acerto, caso esteja na palavra sorteada
        loose = True
        for c in range(0, len(palavra)):
            if letra == palavra[c]:
                oculta.pop(c)
                oculta.insert(c, letra)
                points += 1
                loose = False

        if loose:
            life -= 1

        # Verifica se o jogador perdeu ou se ele ganhou
        if life == 0:
            fc.printforca(life, oculta, trys)
            print(f"Você perdeu! A palavra era: {palavra}")
            time.sleep(2)
            break
        elif points == len(palavra):
            wins += 1
            fc.printforca(life, oculta, trys)
            print(f"Você ganhou! A palavra era: {palavra}")
            time.sleep(2)
            break
