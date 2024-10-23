import flashcards

endProgram = False
chapters = False

print("Welcome to studyHelper!")
filename = input("Enter JSON filename to read: ")
flashcards = flashcards.Flashcards(filename)
chapters = flashcards.test_for_chapters()
print(chapters)


while not endProgram:
	print("\n1. Flashcards")
	print("2. List all terms")
	print("3. List all terms (timed)")
	print("4. List terms by chapter")
	print("5. List terms by chapter (timed)")
	print("6. Help")
	print("7. Quit program")
	choice = input("\nEnter menu choice: ")
	
	if choice == '1':
		print("Q and E cycles through cards, use spacebar to flip.")
	elif choice == '2':
		if chapters:
			print(flashcards.all_terms_c())
		else:
			print(flashcards.all_terms())
	elif choice == '3':
		if chapters:
			flashcards.all_terms_timed_c()
		else:
			flashcards.all_terms_timed()
	elif choice == '4':
		chapter = input("Select chapter to list: ")
		print(flashcards.chapter_terms(chapter))
	elif choice == '5':
		chapter = input("Select chapter to list: ")
		flashcards.chapter_terms_timed(chapter)
	elif choice == '6':
		f = open('help.txt', 'r')
		information = f.read()
		print(f"\n{information}")
		f.close()
	elif choice == '7' or choice == 'quit':
		endProgram = True
	else:
		print("Invalid input.")
