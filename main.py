ukoly = []

def pridat_ukol():
    nazev_ukolu = input("Zadej název úkolu (pole nesmí být prázdné): ")
    while True:
        if not nazev_ukolu:
            nazev_ukolu = input("Nezadal/a jsi název úkolu, doplň název: ")
        else:
            break
    
    popis_ukolu = input("Zadej název úkolu (pole nesmí být prázdné): ")
    while True:
        if popis_ukolu == "":
            popis_ukolu = input("Nezadal/a jsi název úkolu, doplň název: ")
        else:
            ukoly.append(f"{nazev_ukolu} – {popis_ukolu}")
            print(f"\nÚkol '{nazev_ukolu}' byl přidán\n")
            hlavni_menu()
            break
            

def zobrazit_ukoly():
    if ukoly:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol}")

        print("")
        hlavni_menu()
    else:
        print(f"\nMomentálně nemáš žádné přidané úkoly:)\n")
        hlavni_menu()


def odstranit_ukol():
    if ukoly:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol}")
            
        task_number = int(input(f"\nZadej číslo úkolu, které chceš odstranit: "))
        
        while True:
            if task_number in range(1, len(ukoly) + 1):
                ukoly.remove(ukoly[task_number-1])
                print(f"\nÚkol {task_number} byl odstraněn.\n")
                hlavni_menu()
                break
            else:
                task_number = int(input(f"\nNeplatná hodnota. Zadejte číslo úkolu, které chcete odstranit: "))
    else:
        print(f"\nMomentálně nemáš žádné přidané úkoly:)\n")
        hlavni_menu()


def hlavni_menu():
    user_choice = input(f"Správce úkolů - Hlavní menu\n1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu\nVyberte možnost(1-4) ")

    if user_choice == "1":
        pridat_ukol()
    elif user_choice == "2":
        zobrazit_ukoly()
    elif user_choice == "3":
        odstranit_ukol()
    elif user_choice == "4":
        print(f"\nKonec programu.\n")
        quit()
    else:
        print(f"\nZvolil/a jsi neplatnou možnost. Prosím, opakuj volbu.\n")
        hlavni_menu()


hlavni_menu()