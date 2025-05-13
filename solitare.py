import random
import emoji

LICZBA_KOLUMN = 7

# symbole do tworzenia kart
symbole = ['♥',  '♦', '♠', '♣']

# słowniki kart i ich wartości
karty_kier = {}
karty_karo = {}
karty_pik = {}
karty_trefl = {}

# lista słowników kart
karty = [karty_kier, karty_karo, karty_pik, karty_trefl]


# funkcja do sprawdzania czy daną kartę można przełożyć
def mozna_polozyc(a, b):
	karta_a = a
	karta_b = b
	print(karty[symbole.index(karta_b[0])][karta_b], karty[symbole.index(karta_a[0])][karta_a] + 1)
	if (symbole.index(karta_a[0]) in [0, 1] and symbole.index(karta_b[0]) in [2, 3]) or (symbole.index(karta_a[0]) in [2, 3] and symbole.index(karta_b[0]) in [0, 1]):
		if karty[symbole.index(karta_b[0])][karta_b] == karty[symbole.index(karta_a[0])][karta_a] + 1:
			return True
		else:
			print('Zła kolejność')
			return False
	else:
		print('Kolory kart nie pasują')


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
	kolumny.append([])
	for a in range(i+1):
		karta = random.choice(stos)
		if a == i:
			kolumny[i].append((karta, True))
		else:
			kolumny[i].append((karta, False))
		stos.remove(karta)

# pętla główna
gameOn = True
while gameOn:
	print('------------------------')
	# wypisanie stosu
	print(stos[-1], end='\n' * 2)
	# wypisywanie kolumn
	for i in range(LICZBA_KOLUMN):
		print(i+1, end=4*' ')
	print()
	for i in range(len(max(kolumny, key=len))):
		for k in kolumny:
			if len(k) > i:
				karta = k[i][0]
				face_up = k[i][1]
				if not face_up:
					print('###', end=2*' ')
				else:
					if len(str(karta)) == 2:
						print(karta, end=3*' ')
					else:
						print(karta, end=2*' ')
			else:
				print(5*' ', end='')
		print()
	print('------------------------')
	user_input = input("Co teraz?: ")
	# wykonywanie komend
	if user_input == ' ':
		stos.append(stos[0])
		stos.remove(stos[0])
		print()
	# wyjście z gry
	elif user_input == 'Q' or user_input == 'q':
		gameOn = False
	# przekładanie z stosu na jedną z kolumn
	elif len(user_input) == 1 and user_input.isdigit() and LICZBA_KOLUMN+1 > int(user_input) > -1 and mozna_polozyc(stos[-1], kolumny[int(user_input)-1][-1][0]):
		print(int(user_input)-1)
		kolumny[int(user_input)-1].append((stos[-1], True))
		stos.remove(stos[-1])
	# przekładanie z kolumny na kolumnę
	elif len(user_input) == 3:
		a, b = user_input.split()
		a = int(a)
		b = int(b)
		if -1 < a < LICZBA_KOLUMN+1 and -1 < b < LICZBA_KOLUMN+1:
			a_karta = kolumny[a-1][-1][0]
			b_karta = kolumny[b-1][-1][0]
			if mozna_polozyc(a_karta, b_karta):
				kolumny[b-1].append((kolumny[a - 1][-1][0],  True))
				kolumny[a-1].remove(kolumny[a-1][-1])
				if not len(kolumny[a - 1]) == 0:
					kolumny[a-1][-1] = (kolumny[a-1][-1][0], True)
		else:
			print('Kolumny o takich numerach nie istnieją')

	elif len(user_input) == 5:
		a, b, c = user_input.split()
		a = int(a)
		b = int(b)
		c = int(c)
		if kolumny[b-1][-a][1] and mozna_polozyc(kolumny[b-1][-a][0], kolumny[c-1][-1][0]):
			print(-1, -a, -1)
			kolumny[b - 1][-1] = (kolumny[b - 1][-1][0], True)
			if not -a == -1:
				for i in range(-1, -a, -1):
					kolumny[c-1].append(kolumny[b-1][i])
					kolumny[b-1].remove(kolumny[b-1][i])
			else:
				kolumny[c - 1].append(kolumny[b - 1][-1])
				kolumny[b - 1].remove(kolumny[b - 1][-1])

	else:
		print('Taka akcja nie istnieje lub jest niemozliwa.')

