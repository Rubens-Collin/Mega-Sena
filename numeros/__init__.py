def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('ERRO! digite um número inteiro válido.')
            continue
        return n


def sorteio(msg):
    from time import sleep
    from random import randint
    n = leiaInt(msg)
    totjogos = n
    jogos = []
    lista = []
    x = 1
    while x <= totjogos:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >=6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        x += 1
    print('-=' *3, f'SORTEANDO {totjogos} JOGOS', '-=' *3)
    for i, l in enumerate(jogos):
        sleep(1)
        print(f'Jogo {i+1}: {l}')
    sleep(0.5)
    print('Obrigado por usar a nossa plataforma! :)')