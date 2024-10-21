import flashcards

endProgram = False

print("Welcome to studyHelper!")
filename = input("Enter JSON filename to read: ")
flashcards = flashcards.Flashcards(filename)


while not endProgram:
	print("\n1. Flashcards")
	print("2. List all terms")
	print("3. List terms by chapter")
	print("4. Help")
	print("5. Quit program")
	choice = input("\nEnter menu choice: ")
	
	if choice == '1':
		print("Q and E cycles through cards, use spacebar to flip.")
	elif choice == '2':
		print(flashcards.all_terms())
	elif choice == '3':
		print("Select chapter to list: ")
	elif choice == '5' or 'quit':
		endProgram = True
	else:
		print("Invalid input.")
