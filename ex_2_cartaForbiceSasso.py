# Carta, forbice, sasso
# Scrivi un programma che implementa un gioco a due giocatori: un umano contro il computer.
# Prima di iniziare il gioco, il programma chiede il nome del giocatore umano, e inizializza il punteggio dei due giocatoria 0.
#
# Il gioco è suddiviso in 10 turni. Ad ogni turno:
# il programma genera la "giocata" per il computer, ovvero una scelta tra "carta", "forbice" o "sasso". La giocata può essere
# rappresentata come un numero, generato in modo pseudo-casuale.
#
# il programma chiede all'utente di inserire la propria giocata (ovvero, una rappresentazione di "carta" o "forbice" o "sasso");
#
# al vincitore della mano, determinato secondo le regole del gioco "carta, forbice, sasso", viene incrementato il punteggio.
#
# Al termine del gioco (dopo 10 turni), il programma deve stampare:
#
# il punteggio del giocatore umano e quello del computer;
#
# il nome del vincitore: quello del giocatore umano (inserito all'inizio del gioco), oppure "computer", oppure "parità" se
# entrambi i giocatori hanno lo stesso punteggio al termine del gioco.
import random

player1_name = input("Come ti chiami?")
score_player1 = 0
score_bot = 0
# bet_types = [0="carta", 1="forbice", 2="sasso"]


for turn in range(0, 4):
    print("Game legend: 0=carta, 1=forbice, 2=sasso")
    bot_bet_type = random.randint(0, 2)
    print(f"Il bot ha giocato: {bot_bet_type}")
    player1_bet_type = int(input("Inserisci la tua mossa: "))
    if player1_bet_type == 2 and bot_bet_type == 1 or player1_bet_type == 1 and bot_bet_type == 0 or\
            player1_bet_type == 0 and bot_bet_type == 2:
        score_player1 = score_player1 + 1
    elif player1_bet_type == bot_bet_type:
        score_player1 = score_player1 + 1
        score_bot = score_bot + 1
    else:
        score_bot = score_bot + 1

print(f"Score bot: {score_bot}")
print(f"Score player {player1_name}: {score_player1}")

if score_bot == score_player1:
    print("Parità!")
elif score_bot > score_player1:
    print("Il vincitore è il computer")
else:
    print(f"Il vincitore è {player1_name}")


