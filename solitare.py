import random

LICZBA_KOLUMN = 7

# symbole do tworzenia kart
symbole = ['♥', '♦', '♠', '♣']
symbole_emojis = ['♥️', '♦️', '♠️', '♣️']

# słowniki kart i ich wartości
karty_kier = {}
karty_karo = {}
karty_pik = {}
karty_trefl = {}

# lista słowników kart
karty = [karty_kier, karty_karo, karty_pik, karty_trefl]


# funkcja do sprawdzania, czy daną kartę można przełożyć
def mozna_polozyc(a, b, how_many, lista):
	if lista == 'stos':
		karta_a = stos[-1]
	else:
		karta_a = str(kolumny[a][-how_many][0])
	if not len(kolumny[b-1]) == 0:
		karta_b = kolumny[b-1][-1][0]
	else:
		karta_b = '0'
	if not karta_b == '0':
		if (symbole.index(karta_a[0]) in [0, 1] and symbole.index(karta_b[0]) in [2, 3]) or (symbole.index(karta_a[0]) in [2, 3] and symbole.index(karta_b[0]) in [0, 1]):
			if karty[symbole.index(karta_b[0])][karta_b] == karty[symbole.index(karta_a[0])][karta_a] + 1:
				return True
			else:
				print('Zła kolejność')
				return False
		else:
			print('Kolory kart nie pasują')
			return False
	# jeżeli karta jest królem może pójść na puste miejsce
	elif karta_a[-1] == 'K':
		return True
	else:
		return False


stosy_posortowane = []
# tworzenie stosów do przenoszenia kart w kolejności
for i in range(4):
	stosy_posortowane.append([])
	stosy_posortowane[i].append('')

# tworzenie i dodawanie kart do odpowiednich grup
for k in karty:
	k[(symbole_emojis[karty.index(k)] + 'A')] = 1
	for i in range(2, 11):
		k[(symbole_emojis[karty.index(k)] + str(i))] = i
	k[(symbole_emojis[karty.index(k)] + 'J')] = 11
	k[(symbole_emojis[karty.index(k)] + 'Q')] = 12
	k[(symbole_emojis[karty.index(k)] + 'K')] = 13

# tworzenie stosu
stos = []
for g in karty:
	for k in g:
		stos.append(k)

# tasowanie kart
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


print('''Przenoszenie kart:
Z kolumny na kolumnę: x y z albo y z
- x liczba kart,
- y z której kolumny,
- z na którą kolumnę

Ze stosu na kolumnę: x
- x na którą kolumnę

Z kolumny na stos końcowy: x y*
- x z której kolumny,
- y na który stos końcowy

Ze stosu na stos końcowy: x*
- x na który stos końcowy''')



# pętla główna
gameOn = True
while gameOn:
	print('------------------------')
	# wypisanie stosów
	if not len(stos) == 0:
		print(stos[-1], end=' | ')
	else:
		print('    | ', end='')
	for i in stosy_posortowane:
		if not i[-1] == '':
			print(i[-1], end=' '*(3-len(i[-1][0])))
		else:
			print(end=' '*2)
	print('\n')
	# wypisywanie kolumn
	for i in range(LICZBA_KOLUMN):
		print(i+1, end=5*' ')
	print()
	for i in range(len(max(kolumny, key=len))):
		for k in kolumny:
			if len(k) > i:
				karta = k[i][0]
				face_up = k[i][1]
				if not face_up:
					print('####', end=2*' ')
				else:
					if len(str(karta)) == 3:
						print(karta, end=3*' ')
					else:
						print(karta, end=2*' ')
			else:
				print(6*' ', end='')
		print()

	print('------------------------')
	user_input = input("Co teraz?: ")

	# wykonywanie komend
	if user_input == ' ':
		stos.append(stos[0])
		stos.remove(stos[0])
	# wyjście z gry
	elif user_input == 'Q' or user_input == 'q':
		gameOn = False
	# przekładanie ze stosu na jedną z kolumn
	elif len(user_input) == 1 and user_input.isdigit() and LICZBA_KOLUMN+1 > int(user_input) > -1 and len(stos) > 0:
		if mozna_polozyc(stos[-1], int(user_input), 1, 'stos'):
			kolumny[int(user_input)-1].append((stos[-1], True))
			if not len(stos) == 0:
				stos.remove(stos[-1])
	# przekładanie kart z kolumny na kolumnę
	elif len(user_input) in [6, 5, 3]:
		try:
			if len(user_input) in [5, 6]:
				a, b, c = user_input.split()
				a = int(a)
				b = int(b)
				c = int(c)
			else:
				b, c = user_input.split()
				a = 1
				b = int(b)
				c = int(c)
			# sprawdzenie, czy dół stosu kart, który chcemy przełożyć, jest odsłonięty oraz czy zgadza się z kartą na górze drugiego stosu
			if len(kolumny[b-1]) >= a and kolumny[b-1][-a][1]:
				if mozna_polozyc(b-1, c, a, 'kolumny'):
					for i in range(-a, 0, 1):
						kolumny[c-1].append(kolumny[b-1][i])
					for i in range(-a, 0, 1):
						kolumny[b-1].remove(kolumny[b-1][i])
					if not len(kolumny[b-1]) == 0:
						kolumny[b - 1][-1] = (kolumny[b - 1][-1][0], True)
			else:
				print('Nie można położyć grupy kart, gdy jedna z nich jest zakryta.')
		except ValueError:
			print('W komendzie popełniono błąd')
	# Przenoszenie z kolumny na jeden ze stosów końcowych
	elif len(user_input) == 4:
		try:
			a, b = user_input.split()
			a = int(a)
			b = int(b[0])
			karta_a = kolumny[a-1][-1][0]
			karta_a_value = karty[symbole.index(karta_a[0])][karta_a]
			pile_last_card = stosy_posortowane[b-1][-1]
			# Jeżeli stos końcowy nie jest pusty ustaw wartość jego góry na wartość najwyższej karty, w przeciwnym wypadku ustaw na 0
			if not pile_last_card == '':
				pile_last_card_value = karty[symbole.index(pile_last_card[0])][pile_last_card]
			else:
				pile_last_card_value = 0
			# sprawdzanie, czy symbole kart się zgadzają
			if pile_last_card == '' or symbole.index(karta_a[0]) == symbole.index(stosy_posortowane[b-1][-1][0][0]):
				# sprowadzanie czy kolejność kart jest poprawna
				if (pile_last_card == '' and karta_a_value == 1) or (pile_last_card_value + 1 == karta_a_value):
					stosy_posortowane[b-1].append(karta_a)
					kolumny[a-1].remove(kolumny[a-1][-1])
					if not len(kolumny[a-1]) == 0:
						kolumny[a-1][-1] = (kolumny[a-1][-1][0], True)
		except:
			print('W komendzie popełniono błąd')
	# Przenoszenie ze stosu głównego na jeden ze stosów końcowych
	elif len(user_input) == 2 and not len(stos) == 0:
		try:
			user_input = int(user_input[0])
			karta_a = stos[-1]
			karta_a_value = karty[symbole.index(karta_a[0])][karta_a]
			pile_last_card = stosy_posortowane[user_input-1][-1]
			# Jeżeli stos końcowy nie jest pusty ustaw wartość jego góry na wartość najwyższej karty, w przeciwnym wypadku ustaw na 0
			if not pile_last_card == '':
				pile_last_card_value = karty[symbole.index(pile_last_card[0][0])][pile_last_card]
			else:
				pile_last_card_value = 0
			# sprawdzanie, czy symbole kart się zgadzają
			if pile_last_card == '' or symbole.index(karta_a[0]) == symbole.index(stosy_posortowane[user_input-1][-1][0][0]):
				# sprowadzanie czy kolejność kart jest poprawna
				if (pile_last_card == '' and karta_a_value == 1) or (pile_last_card_value + 1 == karta_a_value):
					stosy_posortowane[user_input-1].append(karta_a)
					stos.remove(karta_a)
		except:
			print('W komendzie popełniono błąd')
	else:
		print('Taka komenda nie istnieje lub jest niemożliwa.')

	# przechodzenie przez każdy stos końcowy, by sprawdzić, czy są pełne
	droga_do_wygranej = True
	for i in stosy_posortowane:
		if not len(i) == 14:
			droga_do_wygranej = False
	if droga_do_wygranej:
		print('\n'*100)
		print(stosy_posortowane[0], stosy_posortowane[1], stosy_posortowane[2], stosy_posortowane[3], end=2*'\n')
		gameOn = False

print('''WYGRYWASZ''')
