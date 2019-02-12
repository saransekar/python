
import argparse
import requests	
from requests import ConnectionError
import json
import sys

BASE_URL = 'http://api.icndb.com/'

class API_Request:

	def get_response(self,BASE_URL,LimitNumber,Word):

		sys.tracebacklimit = 0

		URL = BASE_URL + 'jokes/' + 'random/' + str(LimitNumber)

		try:
			ResponseData = (requests.get(URL) if Word is None else requests.get(URL +  Word))	

		except requests.ConnectionError as e:

			raise(requests.ConnectionError("No Internet Connection"))		

		return ResponseData 


	def get_data(self,ResponseData,LimitNumber):

		ResJsonDataList = []

		ResponseJson = json.loads(ResponseData.content.decode('utf-8'))

		for Number in range(LimitNumber):

			ResJsonData = (ResponseJson["value"][Number]["joke"])

			ResJsonDataList.append(ResJsonData)

		return ResJsonDataList