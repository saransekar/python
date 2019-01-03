import argparse

parser = argparse.ArgumentParser()
parser.add_argument("calculation")
parser.add_argument('arg1', type = int)
parser.add_argument('arg2', type = int)

args = parser.parse_args()
a = args.arg1 
b = args.arg2

def Additional(a, b):
	return a + b

def Multiplication(a, b):
	return a * b

if args.calculation == "a":

	print Additional(a, b)
	


elif args.calculation == "b":
	
	print Multiplication(a, b)
	
	
else:
	print "Wrong"

