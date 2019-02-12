import unittest
import main
import requests

class TestMethod(unittest.TestCase):

	def test_make_connection_error(self):

		Response = main.make_connection('http://api.icndb.com/jokes/random',3)

		self.assertRaises(requests.ConnectionError,main.make_connection("ConnectionError"))


	def test_make_connection_success(self):

		Response = main.make_connection('http://api.icndb.com/',5)

		ExpectedOutput = 200

		self.assertEqual(Response,ExpectedOutput)


	def test_make_connection_failed(self):

		Response = main.make_connection('http://api.icndb.com/',5)

		ExpectedOutput = [200]

		self.assertNotEqual(Response,ExpectedOutput)


	def test_get_data_success(self):

		Response = main.make_connection('http://api.icndb.com/',5)
		
		ResponseJson = main.get_data(Response,5)

		ExpectedOutput = 5

		self.assertEqual(ResponseJson,ExpectedOutput)
	

	def test_get_data_failed(self):

		Response = main.make_connection('http://api.icndb.com/',5)
		
		ResponseJson = main.get_data(Response,5)

		ExpectedOutput = 15

		self.assertNotEqual(ResponseJson,ExpectedOutput)	
		
if __name__ == '__main__':

	unittest.main()
