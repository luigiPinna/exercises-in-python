# Scrivere un programma per verificare la conoscenza delle tabelline.

# Il programma chiede innanzitutto di inserire il livello di difficoltà (F=facile, D=difficile). Se l'utente inserisce un valore sbagliato, selezionare il livello facile.

# Una volta definito il livello di difficoltà, propone 10 domande (usando un ciclo for). Ogni domanda chiede:

# quanto fa n per m?
# dove n ed m sono numeri pseudocasuali nell'intervallo:
#
# [1,10] per il livello facile
# [1,15] per il livello difficile
# Al termine delle domande, il programma stampa il numero delle risposte corrette.

import random

difficulty_level = input('Inserisci il livello di difficoltà [F=facile][D=difficile]:')

if difficulty_level != 'F' or difficulty_level != 'D':
    difficulty_level = 'F'

print(difficulty_level)
count = 0

for index in range(0, 3):
    if difficulty_level == "F":
        n = random.randint(1, 10)
        m = random.randint(1, 10)
        correct_result = n * m
        user_result = int(input(f"Quanto fa {n} per {m} ?"))
        if correct_result == user_result:
            count = count + 1
    else:
        n = random.randint(1, 15)
        m = random.randint(1, 15)
        correct_result = n * m
        user_result = int(input(f"Quanto fa {n} per {m} ?"))
        if correct_result == user_result:
            count = count + 1

print(f"Le risposte corrette sono: {count}")
