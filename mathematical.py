import argparse

parser = argparse.ArgumentParser()
parser.add_argument("alphabet_order")
parser.add_argument('arg1', type = int)
parser.add_argument('arg2', type = int)
args = parser.parse_args()

class Calculator:
	
	def __init__(self,arg1,arg2):

		self.arg1 = arg1
		self.arg2 = arg2

	def Additional(self):
		return self.arg1 + self.arg2

	def Multiplication(self):
		return self.arg1 * self.arg2

	def Division(self):
		return self.arg1 / self.arg2

	def Subtract(self):
		return self.arg1 - self.arg2

if __name__ == '__main__':

	calc = Calculator(arg1 = args.arg1, arg2 = args.arg2)

	if args.alphabet_order == "a":

		print "Add two Number is %d" % calc.Additional()
			
	elif args.alphabet_order == "m":
			
		print "Multiple two Number is %d" % calc.Multiplication()

	elif args.alphabet_order == "d":

		print "Divide two Number is %d" % calc.Division()

	elif args.alphabet_order == "s":
		
		print "Subtrct two Number is %d" % calc.Subtract()	

					
	else:
		print "Didn't Match" 

