# Biglietti al cinema
# Scrivi un programma che calcola l'importo per l'acquisto di biglietti al cinema.
#
# Come primo passo, il programma chiede che venga inserito il numero di spettatori. Fatto questo, per ogni spettatore,
# il programma chiede l'età e se lo spettatore desidera un posto "VIP".
#
# Una volta inseriti i dati di tutti gli spettatori, il programma calcola il prezzo totale secondo la seguente logica:
#
# il prezzo base del biglietto è 8 EUR. Il prezzo extra della poltrona VIP è 1 EUR.
# gli spettatori con meno di 12 anni hanno il 50% di sconto sul prezzo base.
# gli spettatori con più di 65 anni hanno il 50% di sconto sul prezzo base, e hanno gratis la poltrona VIP.
# se il gruppo di spettatori è composta da due adulti (di età maggiore o uguale a 18 anni) e
#   da almeno due bambini (di età minore o uguale a 12 anni), allora si applica un ulteriore "sconto famiglia" del 20% sul totale.
# se tutti gli spettatori sono over-65, e il gruppo contiene almeno 4 spettatori, allora si applica un ulteriore sconto del 20% sul totale.
# Il programma deve terminare stampando il prezzo complessivo dei biglietti.#

viewers_num = input("Inserisci il numero di spettatori: ")
base_price = 8
vip_armchair = 1
discount = 20
viewers_count = 0
prezzo_finale = 0
viewers_group = []
flag_is_adult = 0
flag_is_young = 0
flag_is_over_65 = 0

for viewers in range(0, int(viewers_num)):
    viewers_count = viewers_count + 1
    age = input(f"Inserisci l'età dello spettatore n. {viewers_count}: ")
    age_int = int(age)
    vip_chair = input(f"Lo pessatore {viewers_count} desidera poltrona VIP? [s = si] [n = no]: ")
    if age_int < 12 or age_int > 65:
        prezzo_finale = prezzo_finale + (base_price * 0.5)
    elif vip_chair == 's' and age_int < 65:
        prezzo_finale = prezzo_finale + base_price + vip_armchair
    else:
        prezzo_finale = prezzo_finale + base_price
    id = viewers_count
    spettatore = [id, age, vip_chair]
    viewers_group.append(spettatore)
    print(f"Prezzo finale intermedio: {prezzo_finale}")
    # if is adult
    if age_int >= 18:
        flag_is_adult += 1
    # if is young
    if age_int <= 12:
        flag_is_young += 1
    # if is over 65
    if age_int > 65:
        flag_is_over_65 += 1

if flag_is_adult == 2 and flag_is_young >= 2:
    prezzo_finale = prezzo_finale - ((prezzo_finale * discount) / 100)
if viewers_count == flag_is_over_65 and viewers_count >= 4:
    prezzo_finale = prezzo_finale - ((prezzo_finale * discount) / 100)

print(f"Spettatori: {viewers_group}",)
print(f"Prezzo finale totale: {prezzo_finale}")




