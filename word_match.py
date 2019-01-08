import argparse


class ReadFile():

  def __init__(self, filename, word):

    self.filename = filename

    self.word = word


  def read_data(self):  

    a = []
   
    with open(self.filename,'r') as file:

      lines = file.read()
     
      lines_1 = lines.split(" ")

      print lines_1

      print self.word


      for name in lines_1:

        if name != self.word:


          output = set(name) & set(self.word)

          #print output

          list_string = list(output)

          #print len(list_string)

          a.append(len(list_string))

        else:
        	
          a.append(0)
          

      #print a

      max_string = max(a)

      #print max_string

      name_list = a.index(max_string)

      #print name_list

      string_name = lines_1[name_list]

      print string_name
                  

        

if __name__ == '__main__':

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help="name of the word")

  args = parser.parse_args()


  obj = ReadFile(filename = args.filename, word = args.word)

  obj.read_data()
