import json
import time

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
		
	def all_terms_c(self):
		all_cards_ = ''
		print("\n")
		for chapters, terms in self.flashcards.items():
			for term, definition in terms.items():
				all_cards_ += f'\033[1;34m{term}\033[0m \n{definition}\n\n'
		return all_cards_
		
	def all_terms(self):
		all_cards_ = ''
		print("\n")
		for term, definition in self.flashcards.items():
			all_cards_ += f'\033[1;34m{term}\033[0m \n{definition}\n\n'
		return all_cards_

	def chapter_terms(self, chapter):
		try:
			chapter_terms = ''
			print("\n")
			for term in self.flashcards[chapter]:
				definition = self.flashcards[chapter][term]
				chapter_terms += f'\033[1;34m{term}\033[0m \n{definition}\n\n'
		except KeyError as e:
			print(f'KeyError: No chapter called {chapter} found in data')
			print(f'Be sure to use the exact name which is in the data file.')
		return chapter_terms
		
	def all_terms_timed_c(self):
		try:
			seconds = float(input("How many seconds between each term?: "))
			print("\n")
			if seconds < 0:
				time.sleep(seconds)
			count = 0
			for chapters, terms in self.flashcards.items():
				for term, definition in terms.items():
					count += 1
			total_time = count * seconds
			print(f"With {count} terms at {1/seconds:.2f} terms/sec,") 
			print(f"it will take {total_time} seconds ({(total_time / 60):.2f} minutes) to finish.")
			option = input("Continue? (Y/N): ").lower()
			while option != 'y' and option != 'n':
				option = input("Please type Y/N: ")
			if(option == 'n'):
				return
			print("\n")
		except Exception as e:
			print(f"Invalid input: {e}")
			return
		time.sleep(0.75)
		for chapters, terms in self.flashcards.items():
			for term, definition in terms.items():
				print(f'\033[1;34m{term}\033[0m \n{definition}\n')
				time.sleep(seconds)
			
	def all_terms_timed(self):
		try:
			seconds = float(input("How many seconds between each term?: "))
			print("\n")
			if seconds < 0:
				time.sleep(seconds)
			total_time = len(self.flashcards) * seconds
			print(f"With {len(self.flashcards)} terms at {1/seconds:.2f} terms/sec,") 
			print(f"it will take {total_time} seconds ({(total_time / 60):.2f} minutes) to finish.")
			option = input("Continue? (Y/N): ").lower()
			while option != 'y' and option != 'n':
				option = input("Please type Y/N: ")
			if(option == 'n'):
				return
			print("\n")
		except Exception as e:
			print(f"Invalid input: {e}")
			return
		time.sleep(0.75)
		for term in self.flashcards:
			definition = self.flashcards[term]
			print(f"\033[1;34m{term}\033[0m \n{definition}\n")
			time.sleep(seconds)
			
	def chapter_terms_timed(self, chapter):
		try:
			seconds = float(input("How many seconds between each term?: "))
			print("\n")
			if seconds < 0:
				time.sleep(seconds)
			total_time = len(self.flashcards[chapter]) * seconds
			print(f"With {len(self.flashcards[chapter])} terms at {1/seconds:.2f} terms/sec,") 
			print(f"it will take {total_time} seconds ({(total_time / 60):.2f} minutes) to finish.")
			option = input("Continue? (Y/N): ").lower()
			while option != 'y' and option != 'n':
				option = input("Please type Y/N: ")
			if(option == 'n'):
				return
			print("\n")
		except Exception as e:
			print(f"Invalid input: {e}")
			return
		time.sleep(0.75)
		for term in self.flashcards[chapter]:
			definition = self.flashcards[chapter][term]
			print(f'\033[1;34m{term}\033[0m \n{definition}\n\n')
			time.sleep(seconds)
			
	def test_for_chapters(self):
		try:
			for chapters, terms in self.flashcards.items():
				for term, definition in terms.items():
					break
			return True
		except:
			return False
