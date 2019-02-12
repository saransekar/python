import http_method
import argparse

def create_parser():

	parser = argparse.ArgumentParser()

	parser.add_argument("-l", type = int, metavar = 'limit', nargs = '?', help = "enter the number")

	parser.add_argument("-word", choices = ['nerdy', 'explicit', ('nerdy,explicit')], metavar ='word', nargs = '?', help = "enter the word")

	args = parser.parse_args()

	return args



if __name__ == '__main__':
	
	api = http_method.API_Request()

	ArgsInput = create_parser()

	LimitNumber = ArgsInput.l

	Word = ArgsInput.word

	LimitNumber = (1,LimitNumber)[LimitNumber != None]

	ResponseData = api.get_response(http_method.BASE_URL,LimitNumber,Word)

	ResJsonDataList = api.get_data(ResponseData, LimitNumber)

	for joke_idx, joke_val in enumerate(ResJsonDataList):

		print("{} {}".format(joke_idx + 1, joke_val))

