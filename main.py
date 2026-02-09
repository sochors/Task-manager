ukoly = []

def pridat_ukol():
    nazev_ukolu = input("Zadejte název úkolu: ")
    while True:
        if not nazev_ukolu:
            nazev_ukolu = input("Zadejte název úkolu: ")
        else:
            break
    
    popis_ukolu = input("Zadejte popis úkolu: ")
    while True:
        if popis_ukolu == "":
            popis_ukolu = input("Zadejte popis úkolu: ")
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
        task_number = int(input(f"\nZadejte číslo úkolu, které chcete odstranit: "))
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
        print(f"\nZvolili jste neplatnou možnost. Prosím, opakujte volbu.\n")
        hlavni_menu()


hlavni_menu()