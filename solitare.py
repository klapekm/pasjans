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
	for a in range(i+1):
		kolor = random.randint(0, 3)
		karta = random.choice(stos)
		kolumny[i].append(karta)
		stos.remove(karta)

gameOn = True

while gameOn:
	print('------------------------')
	print(stos[-1], end='\n' * 2)
	for i in range(len(max(kolumny, key=len))):
		for k in range(len(kolumny)):
			if len(kolumny[k]) > i:
				if not kolumny[k][i] is kolumny[k][-1]:
					print('###', end='  ')
				else:
					if len(kolumny[k][-1]) == 2:
						print(kolumny[k][-1], end='   ')
					else:
						print(kolumny[k][-1], end='  ')
			else:
				print('     ', end='')
		print()

	user_input = input()
	print()
	if user_input == ' ':
		stos.append(stos[0])
		stos.remove(stos[0])
		print()
	elif user_input == 'LEAVE':
		gameOn = False
	elif len(user_input) == 1 and user_input.isdigit() and LICZBA_KOLUMN+17 > int(user_input) > -1:
		print(int(user_input)-1)
		kolumny[int(user_input)-1].append(stos[-1])
		stos.remove(stos[-1])
	elif len(user_input) == 3:
		a, b = user_input.split()
		a = int(a)
		b = int(b)
		if -1 < a < LICZBA_KOLUMN+1 and -1 < b < LICZBA_KOLUMN+1:
			kolumny[b - 1].append(kolumny[a - 1][-1])
			kolumny[a-1].remove(kolumny[a-1][-1])
		else:
			print('Taka akcja nie istnieje')
	else:
		print('Taka akcja nie istnieje')

