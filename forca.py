import random
import funcoes as fc

# Feito por zzAlfa / Versão 1.0

wins = 0
while True:
    boneco = {"cabeça": "('_')", "corpo": " (|)", "pernas": r" / \ "}
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
    while True:
        try:
            esc = int(input('Selecione o modo de jogo: '))
            break
        except ValueError:
            print('Tente digitar um número inteiro')

    if esc == 1:
        fruta = ['MAÇÃ', 'BANANA', 'UVA']
        print('Bem vindo ao tema de frutas!!!')
        play = fruta[random.randint(0, 2)]
        trys = []
        myword = ''
        count = 0
        life = 4
        while True:
            acert = 0
            fc.forca(play, trys, life)
            if myword == play:
                print('Você ganhou o Jogo!!!')
                wins += 1
                break
            elif life == 0:
                print('Você perdeu o jogo')
            while True:
                letra = input('Qual palavra deseja tentar: ').upper()
                if letra not in trys:
                    trys.append(letra)
                    break
                else:
                    print('Você está digitando a mesma letra, tente novamente')

            print('=' * 30)
            for c in range(0, len(play)):
                if trys[count] == play[c]:
                    print(f'Você acertou a letra {trys[count]}')
                    myword = myword + play[c]
                    acert = 1
            if acert != 1:
                print(f'Você errou a letra {trys[count]}')
                life = life - 1
            count += 1
            print('=' * 60)
    elif esc == 2:
        cidades = ['ARACAJU', 'BELO HORIZONTE', 'BOA VISTA', 'BRASÍLIA', 'CAMPO GRANDE', 'CUIABÁ', 'FLORIANÓPOLIS',
                   'FORTALEZA''GOIÂNIA', 'JOÃO PESSOA', 'MACAPÁ', 'MACEIÓ', 'MANAUS', 'NATAL', 'PALMAS', 'PORTO ALEGRE',
                   'PORTO VELHO', 'RECIFE', 'RIO BRANCO', 'RIO DE JANEIRO', 'SALVADOR', 'SÃO LUÍS', 'SÃO PAULO', 'TERESINA',
                   'VITÓRIA']
        print('Bem vindo ao tema de cidades!!!')
        play = cidades[random.randint(0, 2)]
        trys = []
        myword = ''
        count = 0
        life = 4
        while True:
            acert = 0
            fc.forca(play, trys, life)
            if myword == play:
                print('Você ganhou o Jogo!!!')
                wins += 1
                break
            elif life == 0:
                print('Você perdeu o jogo')
            while True:
                letra = input('Qual palavra deseja tentar: ').upper()
                if letra not in trys:
                    trys.append(letra)
                    break
                else:
                    print('Você está digitando a mesma letra, tente novamente')

            print('=' * 30)
            for c in range(0, len(play)):
                if trys[count] == play[c]:
                    print(f'Você acertou a letra {trys[count]}')
                    myword = myword + play[c]
                    acert = 1
            if acert != 1:
                print(f'Você errou a letra {trys[count]}')
                life = life - 1
            count += 1
            print('=' * 60)
    elif esc == 3:
        animais = ['TIGRE', 'LOBO', 'JACARÉ', 'ONÇA-PINTADA', 'ARARA', 'CARANGUEIJO', 'CACHORRO', 'LEÃO']
        print('Bem vindo ao tema de cidades!!!')
        play = animais[random.randint(0, 2)]
        trys = []
        myword = ''
        count = 0
        life = 4
        while True:
            acert = 0
            fc.forca(play, trys, life)
            if myword == play:
                print('Você ganhou o Jogo!!!')
                wins += 1
                break
            elif life == 0:
                print('Você perdeu o jogo')
            while True:
                letra = input('Qual palavra deseja tentar: ').upper()
                if letra not in trys:
                    trys.append(letra)
                    break
                else:
                    print('Você está digitando a mesma letra, tente novamente')

            print('=' * 30)
            for c in range(0, len(play)):
                if trys[count] == play[c]:
                    print(f'Você acertou a letra {trys[count]}')
                    myword = myword + play[c]
                    acert = 1
            if acert != 1:
                print(f'Você errou a letra {trys[count]}')
                life = life - 1
            count += 1
            print('=' * 60)
    elif esc == 0:
        print('Até a próxima')
        break
