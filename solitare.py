import random

LICZBA_KOLUMN = 7

# symbole do tworzenia kart
symbole = ['♥', '♦', '♠', '♣']

# słowniki kart i ich wartości
karty_trefl = {}
karty_karo = {}
karty_pik = {}
karty_kier = {}

# lista słowników kart
karty = [karty_kier, karty_karo, karty_pik, karty_trefl]

# tworzenie i dodawanie kart do odpowiednich grup
for k in karty:
	k[(symbole[karty.index(k)] + 'A')] = 1
	for i in range(2, 11):
		k[(symbole[karty.index(k)] + str(i))] = i
	k[(symbole[karty.index(k)] + 'J')] = 11
	k[(symbole[karty.index(k)] + 'Q')] = 12
	k[(symbole[karty.index(k)] + 'K')] = 13

# tworzenie stosu
stos = []
for g in karty:
	for k in g:
		stos.append(k)

# tasownaie kart
random.shuffle(stos)

kolumny = []

for i in range(LICZBA_KOLUMN):
	kolumny.append([])
	for a in range(LICZBA_KOLUMN - i):
		kolor = random.randint(0, 3)
		karta = random.choice(stos)
		kolumny[i].append(karta)
		stos.remove(karta)

print('##', end='\n' * 2)

while True:
	for i in range(len(max(kolumny, key=len))):
		for k in range(len(kolumny)):
			if len(kolumny[k]) > i:
				if not kolumny[k][i] is kolumny[k][-1]:
					print('##', end=' ')
				else:
					print(kolumny[k][-1], end='  ')
			else:
				pass
		print()

	user_input = input()
	print()
	if user_input == ' ':
		stos.append(stos[0])
		stos.remove(stos[0])
		print()
	elif len(user_input) == 1 and user_input.isdigit() and 11 > int(user_input) > 0:
		kolumny[int(user_input)].append(stos[-1])
		stos.remove(stos[-1])
	elif user_input == '1 2':
		kolumny[0].remove(kolumny[0][-1])
	else:
		print('Taka akcja nie istnieje')
	print('------------------------')
	print(stos[-1], end='\n' * 2)
