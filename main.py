import flashcards

endProgram = False

print("Welcome to studyHelper!")
filename = input("Enter JSON filename to read: ")
flashcards = flashcards.Flashcards(filename)


while not endProgram:
	print("\n1. Flashcards")
	print("2. List all terms")
	print("3. List all terms (timed)")
	print("4. List terms by chapter")
	print("5. Help")
	print("6. Quit program")
	choice = input("\nEnter menu choice: ")
	
	if choice == '1':
		print("Q and E cycles through cards, use spacebar to flip.")
	elif choice == '2':
		print(flashcards.all_terms())
	elif choice == '3':
		flashcards.all_terms_timed()
	elif choice == '4':
		chapter = input("Select chapter to list: ")
		print(flashcards.chapter_terms(chapter))
	elif choice == '5':
		f = open('help.txt', 'r')
		information = f.read()
		print(f"\n{information}")
		f.close()
	elif choice == '6' or 'quit':
		endProgram = True
	else:
		print("Invalid input.")
