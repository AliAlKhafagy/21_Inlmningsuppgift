
# Konkatenering (sammanfogning) av två strängar
"""str1 = "Hej"
str2 = "världen"
str3 = str1 + " " + str2 + "!"
print(str3)
print("Längden på strängen är: ", len(str3))
#len räknar längden på strängen
print("lite text o annat smått och gott.\n")
"""

#escape sekvens exempel
#indexering
"""str1 = "ABC"
print("första tecknet :", str0)
"""

"""letters = 'ABC'
i = 0
for i in range(1):
    print(letters[0])
i += 1

for letter in letters:
    print(letter)
"""

#ui_width betyder user interface width
import os
ui_width = 30

while True:
    print(ui_width * '*')#*'*' betyder att man multiplicerar stjärnor : * 30ggr
    print('FÄRG-GISSAREN 2.0'.center(ui_width))
    print(ui_width * '-')
    print(':: REGLER ::'.center(ui_width))
    print('Gissa en färg!'.center(ui_width))
    print('Gissar du rätt färg'.center(ui_width))
    print('vinner du spelet!'.center(ui_width))
    print('-' * ui_width)
    times = 1
    color = input('Gissa färg > ').lower()

while color != 'gul': # != betyder INTE lika med
    print('Fel gissning , försök igen... ')
    times += 1 #betyder dom får ett försök till
    color = input('Gissa färg > ').lower()
    print('-' * 23)
    print('Korrekt gissat efter', times,'försök!')
    input('Tryck på retur för att starta igen')

#rensa terminal fönster kör import os sedan os.system('cls')
if os.name == 'nt':
    os.system('cls')
    print('Du kör windows')
elif os.name == 'posix':
    os.system('clear')
    input('Du kör Mac eller Linux')
