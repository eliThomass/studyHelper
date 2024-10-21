import json

class Flashcards:
	
	def __init__(self, filename):
		self.name = filename
		self.flashcards = {}
		try:
			with open(filename, 'r') as f:
				self.flashcards = json.load(f)
		except FileNotFoundError:
			print("File not found.")
		except Exception as e:
			print(f"Unexpected error: {e}")
		
	def all_cards(self):
		all_cards_ = ''
		for term in self.flashcards:
			definition = self.flashcards[term]
			all_cards_ += f'{term}: \n{definition}\n\n'
		return all_cards_
