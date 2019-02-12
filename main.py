import argparse
import requests	
from requests import ConnectionError
import json
import sys

BASE_URL = 'http://api.icndb.com/'

class API_Request:

	def create_parser():

		parser = argparse.ArgumentParser()

		parser.add_argument("limit", type = int, metavar='limit', nargs='?', help = "enter the number")

		args = parser.parse_args()

		return args

	def make_connection(BASE_URL,LimitNumber):
			
		try:

			ResponseData = requests.get(BASE_URL + 'jokes/' + 'random/' + str(LimitNumber))

		except requests.ConnectionError as e:

			sys.tracebacklimit = 0

			raise(requests.ConnectionError("No Internet Connection"))		

		return ResponseData 

		
		

if __name__ == '__main__':

	api = API_Request

	ArgsInput = create_parser()

	LimitNumber = ArgsInput.limit

	LimitNumber = (1,LimitNumber)[LimitNumber != None]

	ResponseData = make_connection(BASE_URL,LimitNumber)

	print ResponseData