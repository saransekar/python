import unittest

import method

class TestMethod(unittest.TestCase):


	def test_make_connection_success(self):

		Response = method.make_connection('http://api.icndb.com/',5)

		ExpectedOutput = 5 

		self.assertEqual(Response,ExpectedOutput)



	def test_make_connection_failed(self):

		Response = method.make_connection('http://api.icndb.com/',5)

		ExpectedOutput = 5

		self.assertNotEqual(Response,ExpectedOutput)


			
if __name__ == '__main__':

	unittest.main()
