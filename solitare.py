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

# dodawanie losowych kart do każdej kolumny
for i in range(LICZBA_KOLUMN):
	kolumny.append({})
	for a in range(i+1):
		kolor = random.randint(0, 3)
		karta = random.choice(stos)
		if a == i:
			kolumny[i][karta] = True
		else:
			kolumny[i][karta] = False
		stos.remove(karta)

# pętla główna
gameOn = True
while gameOn:
	print('------------------------')
	# wypisanie stosu
	print(stos[-1], end='\n' * 2)
	# wypisywanie kolumn
	for i in range(len(max(kolumny, key=len))):
		for k in kolumny:
			if len(k) > i:
				karta = list(k.keys())[i]
				face_up = k[karta]
				if not face_up:
					print('###', end='  ')
				else:
					if len(str(karta)) == 2:
						print(karta, end='   ')
					else:
						print(karta, end='  ')
			else:
				print('     ', end='')
		print()
	print('------------------------')
	user_input = input("Co teraz?: ")
	# wykonywanie komend
	if user_input == ' ':
		stos.append(stos[0])
		stos.remove(stos[0])
		print()
	elif user_input == 'Q' or user_input == 'q':
		gameOn = False
	elif len(user_input) == 1 and user_input.isdigit() and LICZBA_KOLUMN+1 > int(user_input) > -1:
		print(int(user_input)-1)
		kolumny[int(user_input)-1][(stos[-1])] = True
		stos.remove(stos[-1])
	elif len(user_input) == 3:
		a, b = user_input.split()
		a = int(a)
		b = int(b)
		if -1 < a < LICZBA_KOLUMN+1 and -1 < b < LICZBA_KOLUMN+1:
			kolumny[b - 1][list(kolumny[a - 1])[-1]] = True
			kolumny[a-1].pop(list(kolumny[a-1])[-1])
			kolumny[a - 1][list(kolumny[a-1])[-1]] = True
		else:
			print('Taka akcja nie istnieje')
	else:
		print('Taka akcja nie istnieje')

