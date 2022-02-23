# Sa Murra
# Scrivi un programma che implementa un gioco a due giocatori: un umano contro il computer.
# Prima di iniziare il gioco, il programma chiede il nome del giocatore umano, e inizializza il punteggio dei due giocatoria 0.
# Il gioco è suddiviso in turni. Ad ogni turno:
# il programma genera due numeri pseudocasuali per il computer:
# la mano (un valore da 1 a 5) e la giocata (un valore da 2 a 10),
# in modo che il valore della giocata sia maggiore di quello della mano; questi valori vengono
# rivelati all'utente soltanto dopo aver completato il passo 2;
#
# il programma chiede all'utente di inserire la propria mano e la propria giocata;
# il programma stampa la mano e la giocata del computer;
# se la giocata di un giocatore è uguale alla somma delle due mani,
# allora il punteggio di quel giocatore (umano o computer) viene incrementato.
# Il gioco termina quando uno dei due giocatori ha raggiunto 3 punti, oppure quando sono state giocate 16 mani.

# Al termine del gioco, il programma deve stampare:
# il punteggio del giocatore umano e quello del computer;
# il nome del vincitore: quello del giocatore umano (inserito all'inizio del gioco),
# oppure "computer", oppure "parità" se entrambi i giocatori hanno lo stesso punteggio al termine del gioco.#
import random

bot_player = "computer"
human_player = input("Ilserisci il tuo nome: ")
human_score = 0
bot_score = 0
max_hands = 4
max_score = 3
hands_count = 0
while hands_count < max_hands or bot_score <= max_score or human_score <= max_score:
    hands_count += 1
    print(f"Partita [{hands_count}]")
    bot_hand = random.randint(1, 5)  # mano
    bot_bet = random.randint(2, 10)  # giocata
    human_hand = int(input("Inserisci la mano: "))
    human_bet = int(input("Inserisci la giocata: "))
    hands_sum = human_hand + bot_hand
    # Print Hands
    print(f"La mano di {bot_player} è: {bot_hand}")
    print(f"La giocata di {bot_player} è: {bot_bet}")

    if hands_sum == bot_bet:
        bot_score += 1
    if hands_sum == human_bet:
        human_score += 1


print(f"Il punteggio di {bot_player} è: {bot_score}")
print(f"Il punteggio di {human_player} è: {human_score}")
if human_score == bot_score:
    final_score = "Parità!"
    print(final_score)
elif human_score > bot_score:
    print(f"Il vincitore è {human_player}")
else:
    print(f"Il vincitore è {bot_player}")