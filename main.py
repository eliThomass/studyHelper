import flashcards

endProgram = False
filename = ''

while not endProgram:
	print("Welcome to studyHelper!")
	
	filename = input("Enter JSON filename to read: ")
	
	flashcards = flashcards.Flashcards(filename)
	
	print(flashcards.all_cards())
	
	if(filename == '9'):
		endProgram = True
