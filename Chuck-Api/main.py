import argparse
import requests	
from requests import ConnectionError
import json
import sys

BASE_URL = 'http://api.icndb.com/'

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

def get_data(ResponseData,LimitNumber):

	ResJsonDataList = []

	ResponseJson = json.loads(ResponseData.content)

	for Number in range(LimitNumber):

		ResJsonData = (ResponseJson["value"][Number]["joke"])

		ResJsonDataList.append(ResJsonData)

	return ResJsonDataList

def main():

	ArgsInput = create_parser()

	LimitNumber = ArgsInput.limit

	LimitNumber = (1,LimitNumber)[LimitNumber != None]

	ResponseData = make_connection(BASE_URL,LimitNumber)

	ResJsonDataList = get_data(ResponseData, LimitNumber)

	for joke_idx, joke_val in enumerate(ResJsonDataList):

		print joke_idx + 1, joke_val


if __name__ == '__main__':

  main()