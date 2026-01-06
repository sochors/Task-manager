ukoly = []

def pridat_ukol():
    nazev_ukolu = input("Zadejte název úkolu: ")
    popis_ukolu = input("Zadejte popis úkolu: ")
    ukoly.append(nazev_ukolu)
    print(f"\nÚkol '{nazev_ukolu}' byl přidán\n")
    print(ukoly)
    hlavni_menu()

def zobrazit_ukoly():
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol}")

    hlavni_menu()


def odstranit_ukol():
    task_number = int(input("Zadejte číslo úkolu, které chcete odstanit: "))

    # TO-DO Kontrola, že zadané číslo odpovídá počtu úkolů
    
    ukoly.remove(ukoly[task_number-1])
    print(f"\nÚkol {task_number} byl odstraněn.\n")
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
        quit
    else:
        print("Špatná volba.")
        hlavni_menu()

hlavni_menu()