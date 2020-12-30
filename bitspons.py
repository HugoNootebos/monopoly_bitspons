import numpy as np
import matplotlib.pyplot as plt

bitsponsarr = [10, 10, 10]
diff = [0, 0, 0]


def update_bitspons(diff, bitsponsarr):
    avg = np.average(diff[-2:])
    if bitsponsarr[-1] >= 5:
        change = np.random.normal(np.clip(avg, -100, 100), 25) * 0.01
    else:
        change = np.random.normal(np.clip(avg, -100, 100), 250) * 0.01
    bitsponsarr += [np.clip((change + 1) * bitsponsarr[-1], 1, np.inf)]
    diff += [change]


def update_bitspons2(diff, bitsponsarr):
    avg = np.average(diff[-2:])
    if bitsponsarr[-1] <= 10:
        change = np.random.normal(np.clip(avg, -100, 100), 250 / bitsponsarr[-1]) * 0.01
    else:
        change = np.random.normal(np.clip(avg, -100, 100), 25) * 0.01
    bitsponsarr += [np.clip((change + 1) * bitsponsarr[-1], 1, np.inf)]
    diff += [change]


def update_bitspons3(diff, bitsponsarr):
    avg = np.average(diff[-2:])
    if bitsponsarr[-1] >= 10:
        change = np.random.normal(np.clip(avg, -100, 100), 25) * 0.01
        bitsponsarr += [np.clip((change + 1) * bitsponsarr[-1], -50, np.inf)]
    elif 0 <= bitsponsarr[-1] < 10:
        change = np.random.normal(np.clip(avg, -100, 100), 3)
        bitsponsarr += [change + bitsponsarr[-1]]
    elif -10 <= bitsponsarr[-1] < 0:
        change = np.random.normal(np.clip(avg + 1, -100, 100), 5)
        bitsponsarr += [change + bitsponsarr[-1]]
    elif bitsponsarr[-1] < -10:
        change = np.random.normal(np.clip(10, -100, 100), 25) * 0.01
        bitsponsarr += [(1 - change) * bitsponsarr[-1]]
    diff += [change]


def update_bitspons4(diff, bitsponsarr):
    avg = np.average(diff[-2:])
    if bitsponsarr[-1] >= 10:
        change = np.random.normal(np.clip(avg, -100, 100), 25) * 0.01
        relative_change = change
        bitsponsarr += [np.clip((change + 1) * bitsponsarr[-1], -50, np.inf)]
    elif 0 <= bitsponsarr[-1] < 10:
        change = np.random.normal(np.clip(avg * bitsponsarr[-1], -100, 100), 2)
        relative_change = change / bitsponsarr[-1]
        bitsponsarr += [change + bitsponsarr[-1]]
    elif -10 <= bitsponsarr[-1] < 0:
        change = np.random.normal(np.clip(3, -100, 100), 4)
        relative_change = change / bitsponsarr[-1]
        bitsponsarr += [change + bitsponsarr[-1]]
    elif bitsponsarr[-1] < -10:
        change = np.random.normal(np.clip(10, -100, 100), 25) * 0.01
        relative_change = change
        bitsponsarr += [(1 - change) * bitsponsarr[-1]]
    diff += [relative_change]


def update_bitspons_manually(diff, bitsponsarr, percentage):
    bitsponsarr += [bitsponsarr[-1] * (percentage * 0.01 + 1)]
    diff += [percentage * 0.01]


print("\nWELCOME TO THE BIT$ APP")
print("Type [help] to view available commands")

players = []
player_num = 0
turn_num = 1
n = int(input('Hoeveel spelers? '))
for i in range(int(n)):
    players += [input('Speler ' + str(i + 1) + ': ')]
print('Stalin (', players[0], ') is aan de beurt')

while (True):
    inp = input()
    if inp == "":
        turn_num += 1
        update_bitspons3(diff, bitsponsarr)
        plt.plot(bitsponsarr)
        plt.show()
        if player_num >= int(n) - 1:
            player_num = 0
        else:
            player_num += 1
        print('Beurt ' + str(turn_num) + ": " + players[player_num])
        print()
        try:
            percent_change = round(100 * (bitsponsarr[-1] - bitsponsarr[-2]) / bitsponsarr[-2], 1)
        except ZeroDivisionError:
            percent_change = "inf"
        if percent_change < 0:
            print("1 Bit$ = ", round(bitsponsarr[-1], 2), "(" + str(percent_change), "%)")
        else:
            print("1 Bit$ = ", round(bitsponsarr[-1], 2), " (+" + str(percent_change), "%)")
        print()
        print("5 Bit$ = ", int(round(5 * bitsponsarr[-1])))
        print("15 Bit$ = ", int(round(15 * bitsponsarr[-1])))
    elif inp == "manual":
        change2 = input("Met welk percentage veranderd de koers?: ")
        if bitsponsarr[-1] >= 0:
            update_bitspons_manually(diff, bitsponsarr, int(change2))
        else:
            update_bitspons_manually(diff, bitsponsarr, -int(change2))
        plt.plot(bitsponsarr)
        plt.show()
        print("1 Bit$ = ", round(bitsponsarr[-1], 2))
    elif inp in ["invest", "inv", "in", "i"]:
        geld = int(input("Hoeveel $pons wil je investeren?: "))
        bit_num = int(geld / bitsponsarr[-1])
        cashback = int(round(geld % bitsponsarr[-1]))
        print("Je kan ", str(bit_num), " Bit$ kopen")
        print("Dan krijg je ", str(cashback), "$pons terug")
    elif inp == "q":
        break
    elif inp == "help":
        print("Type [] om een beurt te beïndigen")
        print("Type [manual] om de koers handmatig te veranderen")
        print("Type [invest] om een geldbedrag om te rekenen naar Bit$")
        print("Voer een getal in om van Bit$ naar $pons te rekenen")
        print("Type [stalin] om de Stalin acties te bekijken")
        print("Type [eliminate] om een speler weg te halen")
        print("Type [q] om te stoppen")
    elif inp == "stalin":
        communist = input('Hoe veel communistische wetten liggen er?: ')
        if communist == '5':
            print('Onteigen 1 onbebouwde bezitting van iedere speler voor een vergoeding van 10 $pons')
            print()
            print('Neem al het contante geld en verdeel het eerlijk')
        elif communist == '4':
            print('Laat alle huizenbezitters hun bezittingen opknappen:')
            print('25 $pons per ananas')
            print('100 $pons per kokante kab')
            print('400 $pons per groen hotel')
            print()
            print('200 $pons aan elke speler')
        elif communist == '3':
            print('De speler met de meeste Bit$ betaalt 5% van zijn Bit$ aan elke speler')
            print()
            print('Tankbelasting: 100 $pons per geplaatste tank')
        elif communist == '2':
            print(
                'Kaaiman eilanden: iedereen mag een contant geldbedrag verstoppen voor andere spelers en de belastingdienst')
            print()
            print('Betaal 300 $pons aan een speler om zijn volgende worp te bepalen')
        elif communist == '1':
            print('Huizen 50% afgeprijsd')
            print()
            print('Spelers bieden voor de keuze:')
            print('Bit$ stijgt met 100%')
            print('of')
            print('Bit$ daalt met 50%')
        elif communist == '0':
            print('Elke speler ontvangt:')
            print('25 $pons per ananas')
            print('100 $pons per kokante kab')
            print('400 $pons per groen hotel')
            print()
            print('Tanks for sale: 500 $pons per tank')
        else:
            print('Dit is geen getal tussen de 0 en 5 :(')
    elif inp == 'test':
        for i in range(100):
            update_bitspons3(diff, bitsponsarr)
        plt.plot(bitsponsarr)
        plt.show()
    elif inp == "eliminate":
        players.remove(players[player_num])
        print(players[player_num] + " is geëlimineerd")
        n -= 1
    else:
        try:
            print(inp + ' Bit$ = ' + str(int(round(float(inp) * bitsponsarr[-1]))) + ' $pons')
        except:
            pass

