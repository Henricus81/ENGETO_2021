TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

USER_DATA = {

'bob': '123',
'ann': 'pass123',
'mike': 'password123',
'liz': 'pass123'

}

text_data = {

    'pocet_slov': 0,
    'pocet_slov_cap': 0,
    'pocet_upper': 0,
    'pocet_lower': 0,
    'nums': 0,
    'sum_nums': 0,
    'occurencies': {}

}

username = input('Zadej uzivatelske jmeno: ')
password = input('Zadej heslo: ')

if username not in USER_DATA.keys():
    print('Neregistrovany uzivatel!')
elif USER_DATA[username] != password:
    print('Spatne heslo!')
else:
    print(f'Vitej {username}!')

    textno = input('Vyber cislo textu: ')

    if not textno.isnumeric():
        print('Mozno zadavat pouze cisla!')
    else:
        textno = int(textno) - 1

        if textno < 0 or textno > 2:
            print('Mozna cisla textu jsou 1 - 3!')
        else:
            text = TEXTS[textno]
            print(f'Vybral jsi text c. {str(textno+1)}')

            slova_raw = text.split()
            slova = [slovo.strip(',.!?') for slovo in slova_raw]

            for slovo in slova:
                if len(slovo) not in text_data['occurencies'].keys():
                    text_data['occurencies'][len(slovo)] = 1
                else:
                    text_data['occurencies'][len(slovo)] += 1

                if slovo.isupper() and slovo.isalpha():
                    text_data['pocet_upper'] += 1
                elif slovo.islower():
                    text_data['pocet_lower'] += 1
                elif slovo.istitle():
                    text_data['pocet_slov_cap'] += 1
                elif slovo.isnumeric():
                    text_data['nums'] += 1
                    text_data['sum_nums'] += int(slovo)

            text_data['pocet_slov'] = len(slova)

            for key, value in sorted(text_data['occurencies'].items()):
                print('{:>3} {:1} {:<20} {:1} {:<3}'.format(str(key), '|', '*'*value, '|', str(value)))