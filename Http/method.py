
import argparse

import requests 

import json

BASE_URL = 'http://api.icndb.com/'


def create_parser():

	parser = argparse.ArgumentParser()

	parser.add_argument("limit", type = int, metavar='limit', nargs='?', help = "enter the number")

	args = parser.parse_args()

	return args


def make_connection(BASE_URL,LimitNumber):

	ResJsonDataList = []

	ResponseData = requests.get(BASE_URL + 'jokes/' + 'random/' + str(LimitNumber))	 

	ResponseJson = json.loads(ResponseData.content)


	for Number in range(LimitNumber):

		ResJsonData = (ResponseJson["value"][Number]["joke"])

		ResJsonDataList.append(ResJsonData)

	return ResJsonDataList


def main():

	ArgsInput = create_parser()

	LimitNumber = ArgsInput.limit

	LimitNumber = (1,LimitNumber)[LimitNumber != None]

	ResJsonDataList = make_connection(BASE_URL,LimitNumber)

	for joke_idx, joke_val in enumerate(ResJsonDataList):

		print joke_idx + 1., joke_val



if __name__ == '__main__':

  main()