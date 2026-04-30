import os

# simple dictionary to store cards:
study_deck = {}

def add_card():
    print("\n--- ADD A NEW FLASHCARD ---")
    print("Benefit: Adding your own terms helps personalize your learning") # IH#1 (benefits)

    term = input("Step 1: Enter the term: ").strip()
    definition = input("Step 2: Enter the definition: ").strip()

    # IH#8 (tinkering/error prevention)
    if not term or not definition:
        print("\n[!] ERROR: Both fields are required, card not saved")
        return

    study_deck[term] = definition
    print(f"\n[S] SUCCESS: Card '{term}' added to your local deck") # IH#2 (privacy/cost info)

def view_deck():
    print("\n--- DECK LIBRARY ---")
    print("Benefit: Reviewing your list helps you see your overall progress ") # IH#1

    if not study_deck:
        print("[!] Your deck is currently empty, try adding a card first")
        return

    print(f"You have {len(study_deck)} cards in this deck.") # IH#2 (cost)

    # simple list of terms
    for i, term in enumerate(study_deck.keys(), 1):
        print(f"{i}. {term}")

    # IH#3 information flow (don't show definitions until asked)
    choice = input("\nEnter a number to see a definition, or [M] for Main Menu: ").strip()

    if choice.lower() == 'm':
        return

    try:
        index = int(choice) - 1
        term = list(study_deck.keys())[index]
        print(f"\n>>> DEFINITION of '{term}':")
        print(f"--- {study_deck[term]} ---")
        input("\nPress enter to return to the library...")
        view_deck() # loop back so they can see more definitions
    except (ValueError, IndexError):
        print("[!] Invalid selection, returning to menu")

def start_quiz():
    if not study_deck:
        print("\n[!] Your deck is empty, add some cards before starting a quiz")
        return

    print("\n--- QUIZ MODE ---")
    print("Benefit: Active recall is the fastest way to memorize new info") # IH#1

    cards = list(study_deck.items())
    total = len(cards)
    score = 0

    for i, (term, definition) in enumerate(cards, 1):
        print(f"\n--- Card {i} of {total} ---") # IH#2 (scope/progress)
        print(f"QUESTION: {term}")

        # IH#7 (different approaches)
        choice = input("Press [enter] to flip or type [H] for a hint: ").strip().lower()

        if choice == 'h':
            # IH#8 tinkering (safety)
            print(f"Hint: the answer starts with '{definition[0]}' and has {len(definition)} characters")
            input("Ready? Press [enter] to see the full answer...")

        print(f"ANSWER: {definition}")

        feedback = input("Did you get it right? (y/n) or [Q] to Quit: ").strip().lower()
        if feedback == 'y':
            score += 1
        elif feedback == 'q':
            # IH#8 confirmation prompt
            if input("Quit quiz? Progress will not be saved (y/n): ").lower() == 'y':
                return

    print(f"\n--- QUIZ COMPLETE ---")
    print(f"Final Score: {score}/{total}")
    print("Great job!") # IH#1 (encouragement)
    input("\nPress enter to return to the menu...")

def main_menu():
    while True:
        print("\n=== FLASHCARD STUDY TOOL ===")
        print("[1] Start Study Session (Strengthen your memory)")
        print("[2] View Deck Library (Review terms at your own pace)")
        print("[3] Add New Card (Customize your deck)")
        print("[Q] Quit")

        choice = input("\nChoose an option: ").lower()

        if choice == '1':
            start_quiz()
        elif choice == '2':
            print(f"Current Deck: {study_deck}")
        elif choice == '3':
            add_card()
        elif choice == 'q':
            #IH#8 - confirmation prompt for tinkerers
            confirm = input("Are you sure you want to quit? Unsaved changes will be lost (y/n): ")
            if confirm.lower() == 'y':
                print("Goodbye!")
                break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main_menu()