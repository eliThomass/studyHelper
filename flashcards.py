import json

class Flashcards:
	
	def __init__(self, filename):
		self.name = filename
		self.flashcards = {}
		try:
			with open(filename, 'r') as f:
				self.flashcards = json.load(f)
				print("File read successfully.")
		except FileNotFoundError:
			print("File not found.")
		except Exception as e:
			print(f"Unexpected error: {e}")
		
	def all_terms(self):
		all_cards_ = ''
		for term in self.flashcards:
			definition = self.flashcards[term]
			all_cards_ += f'\033[1;34m{term}\033[0m \n{definition}\n\n'
		return all_cards_

	def chapter_terms(self, chapter):
		chapter_terms = ''
		
