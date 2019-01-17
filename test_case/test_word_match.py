
import unittest

import word_match


class TestWord_Match(unittest.TestCase):


	def test_read_file(self):

		FileContent = word_match.read_file("abcd.txt")

		MatchedContent = ['ab', 'ac', 'ad', 'af', 'ag', 'aah', 'acab', 'aac', 'acad\n']

		self.assertEqual(FileContent,MatchedContent)	

             
        
	def test_find_match(self):


		FileContent = word_match.read_file("abcd.txt")

		Results = word_match.find_match(FileContent,'ac',12)

		MatchedWord = ['acab', 'aac', 'acad\n']

		self.assertEqual(MatchedWord,Results)

		#with self.assertRaises(TypeError):


			

if __name__ == '__main__':

    unittest.main()