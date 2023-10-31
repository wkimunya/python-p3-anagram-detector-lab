# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = []
        for candidate in word_list:
            # Convert the candidate word to lowercase for case-insensitive comparison
            candidate_lower = candidate.lower()
            
            # Check if the candidate word is not the same as the original word and has the same sorted letters
            if candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word):
                anagrams.append(candidate)
        
        return anagrams
