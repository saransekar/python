import unittest
import main
import requests

class TestMethod(unittest.TestCase):

	def test_get_response_error(self):

		Response = main.get_response('http://api.icndb.com/jokes/random',3)

		self.assertRaises(requests.ConnectionError,main.get_response("ConnectionError"))

	def test_get_response_success(self):

		Response = main.get_response('http://api.icndb.com/',5)

		ExpectedOutput = 200

		self.assertEqual(Response,ExpectedOutput)

	def test_get_response_failed(self):

		Response = main.get_response('http://api.icndb.com/',5)

		ExpectedOutput = [200]

		self.assertNotEqual(Response,ExpectedOutput)

	def test_get_data_success(self):

		Response = main.get_response('http://api.icndb.com/',5)
		
		ResponseJson = main.get_data(Response,5)

		ExpectedOutput = 5

		self.assertEqual(ResponseJson,ExpectedOutput)	

	def test_get_data_failed(self):

		Response = main.get_response('http://api.icndb.com/',5)
		
		ResponseJson = main.get_data(Response,5)

		ExpectedOutput = 15

		self.assertNotEqual(ResponseJson,ExpectedOutput)	
		
if __name__ == '__main__':

	unittest.main()
