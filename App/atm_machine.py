import re
def get_input_user():
	print("User Details")
	global UserName,MobileNumber,EmailId,UserBalance
	UserName = input("Enter the User Name:")
	MobileNumber = input("Enter the Your Mobile Number:")
	if re.search(r'^(?:\+?44)?[07]\d{9,13}$',MobileNumber):
		print("correct")
	else:
		print("No")	
	EmailId = input("Enter the Your EmailId:")
	UserBalance = int(input("Enter the amount:"))

def instruct_account_list():	
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount\n3.Credit Amount\n4.Profile Details\n5.Exit")

def get_money(Debit):
	global UserBalance
	UserBalance = UserBalance - Debit  
	
def transfer_credit(Credit):
	global UserBalance
	UserBalance = Credit + UserBalance 
	
def manage_account():
	while True:
		ChoiceNumber = int(input("Enter Your Choice:"))
		if ChoiceNumber == 1:
			print("Currently Your Available Balance:",UserBalance)

		elif ChoiceNumber == 2:
			Debit = int(input("Enter the Debit Amount:"))
			if UserBalance >= Debit:						
				get_money(Debit)							
				print(UserBalance)
			else:
				print("No Available Balance")			
				
		elif ChoiceNumber == 3:
			Credit = int(input("Enter the Credit Amount:"))
			transfer_credit(Credit)		
			print(UserBalance)
		elif ChoiceNumber == 4:
			print("Profile Details\nUser Name : {}\nMobile Number : {}\nEmail Id : {}\nAvailable Balance : {}".format(UserName,MobileNumber,EmailId,UserBalance)) 				
		elif ChoiceNumber == 5:
			print("Your transcation cancel")
			exit()
		else:
			print("Doesn't exist")

def main():
	get_input_user()
	AccountBalance = instruct_account_list()
	Result = manage_account()
if __name__ == '__main__':
  main()  