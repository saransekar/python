list = ['saran' , 'shali', 'darsa', 'rajae', 'kaviy', 'kumar']
num = int(input("Enter the number:"))
if(num < 6):
   for i in range(0, len(list)):
       if(num == i):
           print(list[i])
           list1 = ['saran' , 'shali', 'darsa', 'rajae', 'kaviy', 'kumar']
           for j in range(0, len(list1)):
               if(num == j):
                   del  list1[j]
                   print("Output", list1)
                   k = 0
                   c = 0
                   for l in range(0, 5):                                        
                       if k != 5:
                           
                           if(list1[k][0] == list[i][0] or list1[k][1] == list[i][0] or list1[k][2] == list[i][0] or list1[k][3] == list[i][0] or list1[k][4] == list[i][0]):
                               print(list[i][0])
                               
                               
                           if(list1[k][0] == list[i][1] or list1[k][1] == list[i][1] or list1[k][2] == list[i][1] or list1[k][3] == list[i][1] or list1[k][4] == list[i][1]):
                               print(list[i][1])            
                                   
                               
                           if(list1[k][0] == list[i][2] or list1[k][1] == list[i][2] or list1[k][2] == list[i][2] or list1[k][3] == list[i][2] or list1[k][4] == list[i][2]):
                               print(list[i][2])

                               
                           if(list1[k][0] == list[i][3] or list1[k][1] == list[i][3] or list1[k][2] == list[i][3] or list1[k][3] == list[i][3] or list1[k][4] == list[i][3]):
                               print(list[i][3])

                               
                           if(list1[k][0] == list[i][4] or list1[k][1] == list[i][4] or list1[k][2] == list[i][4] or list1[k][3] == list[i][4] or list1[k][4] == list[i][4]):
                               print(list[i][4])
                           
                             
                                               
                           if c != 5:
                               c = c + 1
                               k = k + 1
                               print("hello", c, k)
             
                           
else:
   print("Try again Input")
