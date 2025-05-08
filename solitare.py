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
kolumna_1 = []

for i in range(LICZBA_KOLUMN):
	kolor = random.randint(0, 3)
	karta = random.choice(stos)
	kolumna_1.append(karta)
	stos.remove(karta)


print('##', end='\n'*2)

while True:
	for i in range(len(kolumna_1)-1):
		print('##')

	print(kolumna_1[-1])
	user_input = input()
	print()
	if user_input == ' ':
		stos.append(stos[0])
		stos.remove(stos[0])
		print()
	elif user_input == '1':
		kolumna_1.append(stos[-1])
		stos.remove(stos[-1])
	elif user_input == '1 2':
		kolumna_1.remove(kolumna_1[-1])
	else:
		print('Taka akcja nie istnieje')
	print('------------------------')
	print(stos[-1], end='\n'*2)



