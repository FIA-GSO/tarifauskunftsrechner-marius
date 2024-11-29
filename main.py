preis_erwachsene = 5.0
preis_erwachsene_ganz = 10.0

preis_kinder = 2.5
preis_kinder_ganz = 5.0

preis_premium = 3.0
preis_premium_ganz = 6.0

preis_basis = 4.0
preis_basis_ganz = 8.0

preis_ermaessigt = 3.5
preis_ermaessigt_ganz = 6.0

gesamtpreis = 0.0

language = "de"

messages = {
    "tarif_abfrage": {
        "de": "### Tarifauskunftsrechner Museum XXX ###",
        "en": "### Ticket Price Query Museum XXX ###"
    },
    "enter_age": {
        "de": "Hallo, geben Sie bitte Ihr Alter ein.",
        "en": "Hello, please enter your age."
    },
    "invalid_input": {
        "de": "Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.",
        "en": "Invalid input. Please enter a valid number."
    },
    "ticket_half_day": {
        "de": "Möchten Sie ein Ticket für den halben oder ganzen Tag? Halber Tag = 0 | Ganzer Tag = 1",
        "en": "Would you like a half-day or full-day ticket? Half day = 0 | Full day = 1"
    },
    "price_kinder_half": {
        "de": "### Eintritt Kinder Halber Tag ###",
        "en": "### Children's Admission Half Day ###"
    },
    "price_kinder_full": {
        "de": "### Eintritt Kinder Ganzer Tag ###",
        "en": "### Children's Admission Full Day ###"
    },
    "price_discounted_half": {
        "de": "### Eintritt Ermäßigte Jugendliche Halber Tag ###",
        "en": "### Discounted Youth Admission Half Day ###"
    },
    "price_discounted_full": {
        "de": "### Eintritt Ermäßigte Jugendliche Ganzer Tag ###",
        "en": "### Discounted Youth Admission Full Day ###"
    },
    "price_adult_half": {
        "de": "### Eintritt Erwachsene (voller Preis) Halber Tag ###",
        "en": "### Adult Admission Full Price Half Day ###"
    },
    "price_adult_full": {
        "de": "### Eintritt Erwachsene (voller Preis) Ganzer Tag ###",
        "en": "### Adult Admission Full Price Full Day ###"
    },
    "premium_member": {
        "de": "Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich)",
        "en": "Are you a member of the Duisburg Museum Club? (Proof required)"
    },
    "premium_member_choice": {
        "de": "Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein. Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein. Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste.",
        "en": "If you are a Premium member, enter 'p'. If you are a Basic member, enter 'b'. If you are not a member, press any other key."
    },
    "enjoy_message": {
        "de": "Viel Spaß!",
        "en": "Enjoy your visit!"
    },
    "continue_query": {
        "de": "Wollen Sie einen weiteren Tarif abfragen? j=Ja n=Nein",
        "en": "Would you like to query another ticket? y=Yes n=No"
    },
    "total_price": {
        "de": "Gesamtpreis: ",
        "en": "Total price: "
    },
    "total_price_query": {
        "de": "Soll das Ticket zum Gesamtpreis hinzugefügt werden? (Ja = 1 | Nein = 0)",
        "en": "Should the ticket be included to the total price? (Yes = 1 | No = 0)"
    }
}

def set_language():
    global language
    print("Möchten Sie Deutsch oder Englisch wählen? (de/en):")
    choice = input().lower()
    if choice == "en":
        language = "en"
    else:
        language = "de"

def print_message(msg):
    print(messages[msg][language])

def tarif_abfrage():
    global gesamtpreis
    while True:
        try:
            print_message("tarif_abfrage")
            print_message("enter_age")
            alter_gast = int(input())
            if alter_gast < 0:
                raise ValueError("Das Alter kann nicht negativ sein.")
            break
        except ValueError as e:
            print(f"{messages['invalid_input'][language]} Fehler: {e}")
    
    if alter_gast < 14:
        while True:
            try:
                print_message("ticket_half_day")
                ticket = int(input())
                if ticket not in [0, 1]:
                    raise ValueError("Bitte geben Sie 0 für halben Tag oder 1 für ganzen Tag ein.")
                break
            except ValueError as e:
                print(f"{messages['invalid_input'][language]} Fehler: {e}")
        
        if ticket == 0:
            print_message("price_kinder_half")
            print(f" Preis: {preis_kinder} Euro")
            print_message("total_price_query")
            price_included = int(input())
            if (price_included == 1): 
                gesamtpreis += preis_kinder

        elif ticket == 1:
            print_message("price_kinder_full")
            print(f" Preis: {preis_kinder_ganz} Euro")
            print_message("total_price_query")
            price_included = int(input())
            if (price_included == 1): 
                gesamtpreis += preis_kinder_ganz

    elif 14 <= alter_gast <= 17:
        while True:
            try:
                print_message("ticket_half_day")
                ticket = int(input())
                if ticket not in [0, 1]:
                    raise ValueError("Bitte geben Sie 0 für halben Tag oder 1 für ganzen Tag ein.")
                break
            except ValueError as e:
                print(f"{messages['invalid_input'][language]} Fehler: {e}")
        
        if ticket == 0:
            print_message("price_discounted_half")
            print(f" Preis: {preis_ermaessigt} Euro")
            print_message("total_price_query")
            price_included = int(input())
            if (price_included == 1): 
                gesamtpreis += preis_ermaessigt

        elif ticket == 1:
            print_message("price_discounted_full")
            print(f" Preis: {preis_ermaessigt_ganz} Euro")
            print_message("total_price_query")
            price_included = int(input())
            if (price_included == 1): 
                gesamtpreis += preis_ermaessigt_ganz

    else:
        while True:
            try:
                print_message("premium_member")
                print_message("premium_member_choice")
                antwort_rabatt = input().lower()
                if antwort_rabatt not in ["p", "b", ""]:
                    raise ValueError("Bitte geben Sie 'p' für Premium, 'b' für Basis oder eine beliebige andere Taste ein.")
                break
            except ValueError as e:
                print(f"{messages['invalid_input'][language]} Fehler: {e}")

        if antwort_rabatt == "p":
            print_message("ticket_half_day")
            while True:
                try:
                    sekt = input(f"{messages['premium_member_choice'][language]} Möchten Sie für 0,75€ Aufpreis ein Glas Sekt trinken? j=Ja n=Nein: ").lower()
                    if sekt not in ["j", "n"]:
                        raise ValueError("Bitte geben Sie 'j' für Ja oder 'n' für Nein ein.")
                    break
                except ValueError as e:
                    print(f"{messages['invalid_input'][language]} Fehler: {e}")
            
            if sekt == "j":
                while True:
                    try:
                        print_message("ticket_half_day")
                        ticket = int(input())
                        if ticket not in [0, 1]:
                            raise ValueError("Bitte geben Sie 0 für halben Tag oder 1 für ganzen Tag ein.")
                        break
                    except ValueError as e:
                        print(f"{messages['invalid_input'][language]} Fehler: {e}")

                if ticket == 0:
                    print_message("price_adult_half")
                    print(f" Preis: {preis_premium + 0.75} Euro")
                    print_message("total_price_query")
                    price_included = int(input())
                    if (price_included == 1): 
                        gesamtpreis += preis_premium + 0.75

                elif ticket == 1:
                    print_message("price_adult_full")
                    print(f" Preis: {preis_premium_ganz + 0.75} Euro")
                    print_message("total_price_query")
                    price_included = int(input())
                    if (price_included == 1): 
                        gesamtpreis += preis_premium_ganz + 0.75

            else:
                print_message("price_adult_half")
                print(f" Preis: {preis_premium} Euro")
                print_message("total_price_query")
                price_included = int(input())
                if (price_included == 1): 
                    gesamtpreis += preis_premium

        elif antwort_rabatt == "b":
            while True:
                try:
                    print_message("ticket_half_day")
                    ticket = int(input())
                    if ticket not in [0, 1]:
                        raise ValueError("Bitte geben Sie 0 für halben Tag oder 1 für ganzen Tag ein.")
                    break
                except ValueError as e:
                    print(f"{messages['invalid_input'][language]} Fehler: {e}")

            if ticket == 0:
                print_message("price_adult_half")
                print(f" Preis: {preis_basis} Euro")
                print_message("total_price_query")
                price_included = int(input())
                if (price_included == 1): 
                    gesamtpreis += preis_basis

            elif ticket == 1:
                print_message("price_adult_full")
                print(f" Preis: {preis_basis_ganz} Euro")
                print_message("total_price_query")
                price_included = int(input())
                if (price_included == 1): 
                    gesamtpreis += preis_basis_ganz

        else:
            while True:
                try:
                    print_message("ticket_half_day")
                    ticket = int(input())
                    if ticket not in [0, 1]:
                        raise ValueError("Bitte geben Sie 0 für halben Tag oder 1 für ganzen Tag ein.")
                    break
                except ValueError as e:
                    print(f"{messages['invalid_input'][language]} Fehler: {e}")

            if ticket == 0:
                print_message("price_adult_half")
                print(f" Preis: {preis_erwachsene} Euro")
                print_message("total_price_query")
                price_included = int(input())
                if (price_included == 1): 
                    gesamtpreis += preis_erwachsene

            elif ticket == 1:
                print_message("price_adult_full")
                print(f" Preis: {preis_erwachsene_ganz} Euro")
                print_message("total_price_query")
                price_included = int(input())
                if (price_included == 1): 
                    gesamtpreis += preis_erwachsene_ganz

    print_message("enjoy_message")

    print_message("continue_query")
    abfrage = input().lower()
    if abfrage == "n":
        print(f"{messages['total_price'][language]} {gesamtpreis} Euro")
        return False
    return True

set_language()
while True:
    if not tarif_abfrage():
        break
