import os

# simple dictionary to store cards:
study_deck = {}

def add_card():
    print("\n--- ADD A NEW FLASHCARD ---")
    print("Benefit: Adding your own terms helps personalize your learning") # IH#1 (benefits)

    # IH#5 (undo/backtracking)
    print("Note: Leave a field blank and press Enter to safely cancel and backtrack.")

    term = input("Step 1: Enter the term: ").strip()
    if not term:
        print("\n[C] Cancelled: Backtracking to Main Menu without saving.")
        return

    definition = input("Step 2: Enter the definition: ").strip()
    if not definition:
        print("\n[C] Cancelled: Backtracking to Main Menu without saving.")
        return

    study_deck[term] = definition
    print(f"\n[S] SUCCESS: Card '{term}' added to your local deck")

def view_deck():
    print("\n--- DECK LIBRARY ---")
    print("Benefit: Reviewing your list helps you see your overall progress ") # IH#1
    print(f"You have {len(study_deck)} cards in this deck.") # IH#2 (cost)

    if not study_deck:
        print("[!] Your deck is currently empty, try adding a card first")
        return

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
        print("[!] Your deck is empty, add some cards first!")
        return

    total = len(study_deck)
    score = 0

    # enumerate() automatically counts which card you are on (1, 2, 3...)
    for current_card_number, (term, definition) in enumerate(study_deck.items(), 1):

        # IH#2: Calculate time remaining and print it (Updates every loop!)
        time_remaining = (total - current_card_number + 1) * 0.5
        print(f"\nCard {current_card_number} out of {total} (Approx. {time_remaining} minutes remaining)")

        print(f"QUESTION: {term}")
        choice = input("Press enter to flip or [Q] to quit... ")

        if choice.lower() == 'q':
            # IH#8 confirmation prompt
            if input("Quit quiz? Progress will not be saved (y/n): ").lower() == 'y':
                return

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
            view_deck()
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