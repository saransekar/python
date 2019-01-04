list1 = ["saran", "bala", "raja", "venkat", "ram"]

another_list = raw_input("Enter the input string:")

list2 = another_list.split()

list1.append(list2)

print list1


num = int(input("Enter the number:"))

if(num > 0 and num < len(list1)):

		user_output = num - 1

		print list1[user_output]

else:

	print "Please Correct input start from 1 to n..."


my_list = ["saran", "bala", "raja", "venkat", "ram"]

list2 = another_list.split()

my_list.append(list2)

print my_list

if num < len(my_list):

	user_output = num - 1

	del my_list[user_output]

print my_list
