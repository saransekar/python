import unittest

import word_match

class TestWord_Match(unittest.TestCase):


	def test_read_file_success(self):

		FileContent = word_match.read_file("abcd.txt")

		MatchedContent = 'ab ac ad af ag aah acab aac acad\n'

		self.assertEqual(FileContent,MatchedContent)



	def test_read_file_failed(self):

		FileContent = word_match.read_file("ab.txt")

		self.assertRaises(IOError, word_match.read_file("ab.txt"))

			
	def test_separate_words_success(self):

		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		MatchedWord =  ['ab', 'ac', 'ad', 'af', 'ag', 'aah', 'acab', 'aac', 'acad\n']

		self.assertEqual(MatchedWord,ContentList)


	def test_separate_words_failed(self):

		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		MatchedWord =  ['ab', 'ac', 'add', 'afdd', 'ag', 'aah', 'acab', 'aac', 'acad\n']

		self.assertNotEqual(MatchedWord,ContentList)

	
	def test_find_closest_match_success(self):

		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		ClosestMatch = word_match.find_closest_match(ContentList,'ac')

		Output = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2}	

		self.assertEqual(Output,ClosestMatch)
	

	def test_find_closest_match_failed(self):

		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		ClosestMatch = word_match.find_closest_match(ContentList,'ac')

		Output = {0: 1, 1: 11, 2: 11, 3: 1, 4: 11, 5: 2, 6: 2, 17: 2}	

		self.assertNotEqual(Output,ClosestMatch)
			

	def test_eliminate_words_success(self):

		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		ClosestMatch = word_match.find_closest_match(ContentList,'ac')

		ClosestMatch = word_match.eliminate_words(ClosestMatch)

		Output = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2}

		self.assertEqual(Output,ClosestMatch)
	

	def test_eliminate_words_failed(self):

		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		ClosestMatch = word_match.find_closest_match(ContentList,'ac')

		ClosestMatch = word_match.eliminate_words(ClosestMatch)

		Output = {0: 1, 0: 1, 0: 1, 3: 1, 4: 1, 5: 2, 6: 12, 7: 12}

		self.assertNotEqual(Output,ClosestMatch)


	def test_restrictive_word_success(self):


		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		ClosestMatch = word_match.find_closest_match(ContentList,'ac')

		ClosestMatch = word_match.eliminate_words(ClosestMatch)
	
		ClosestWords = word_match.restrictive_word(ClosestMatch,ContentList,2)

		Output = ['aah', 'acab']

		self.assertEqual(Output,ClosestWords)



	def test_restrictive_word_failed(self):


		FileContent = word_match.read_file("abcd.txt")

		ContentList = word_match.separate_words(FileContent)

		ClosestMatch = word_match.find_closest_match(ContentList,'ac')

		ClosestMatch = word_match.eliminate_words(ClosestMatch)
	
		ClosestWords = word_match.restrictive_word(ClosestMatch,ContentList,2)

		Output = ['aahaa', 'acaba']

		self.assertNotEqual(Output,ClosestWords)
	







if __name__ == '__main__':

	unittest.main()
