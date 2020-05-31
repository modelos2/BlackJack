from random import shuffle


def baraja():
    return [(n, p) for n in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K'] for p in ['P', 'C', 'T', 'D']]


def surtir(baraja):
    shuffle(baraja)
    return baraja


def valor_carta(card):
    if card[0] in ('J', 'Q', 'K'):
        return 10
    elif card[0] == 'A':
        return 1
    else:
        return int(card[0])


def valor_mano(mano):
    if mano == []:
        return 0
    else:
        return valor_carta(mano[0]) + valor_mano(mano[1:])


def valor_mano_real(mano):
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)


def evaluar(mano):
    if valor_mano_real(mano) == 21:
        return True
    elif valor_mano_real(mano) > 21:
        return False
    else:
        return None


def evaluar_final(jugador, repartidor):
    if valor_mano_real(jugador) == valor_mano_real(repartidor):
        print("EMPATE")
    elif valor_mano_real(jugador) > valor_mano_real(repartidor):
        print("GANA JUGADOR")
    else:
        print("GANA REPARTIDOR")


def jugar(mazo, jugador, repartidor):
    if len(jugador) != 0:
        print("Mano jugador")
        print(jugador)
        print("Mano repartidor")
        print(repartidor)
    if len(jugador) == 0:
        jugar(mazo[4:], jugador + mazo[0:2], repartidor + mazo[2:4])
    elif evaluar(jugador) and evaluar(repartidor):
        print("EMPATE")
    elif evaluar(jugador):
        print("GANA JUGADOR")
    elif evaluar(repartidor):
        print("GANA REPARTIDOR")
    elif evaluar(jugador) == False:
        print("PIERDE JUGADOR")
    elif evaluar(repartidor) == False:
        print("PIERDE REPARTIDOR")
    elif evaluar(jugador) == None:
        if input("Para plantarse 0: ") == '0':
            evaluar_final(jugador, repartidor)
        else:
            jugar(mazo[1:], jugador + [mazo[0]], repartidor + [mazo[1]])


jugar(surtir(baraja()), [], [])
