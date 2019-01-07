
a = []

input_string = raw_input("Enter the input string:")

string_list = input_string.split()

print string_list


input_user = int(input("Enter the number:"))

if(input_user > 0 and input_user  <= len(string_list)):

		output_user = input_user - 1

		my_list = string_list[output_user]

		print my_list 

		del string_list[output_user]

		print string_list


else:

	print "Please Correct input start from 1 to n..."


for k in range(0, len(string_list)):

	set_list = set(string_list[k]) & set(my_list)

	another_list = list(set_list)

	print another_list

	print len(another_list)

	a.append(another_list)

 	a.append(len(another_list))
 	
max_string = max(a)

string = ''

string = ''.join(map(str,max_string)) 

print "Maximum letter of string:", string
