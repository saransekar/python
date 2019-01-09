import argparse

def create_parser(): 

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help = "name of the word")

  args = parser.parse_args()

  return args


def file_read(FileName):  

  with open(FileName,'r') as file:

    content = file.read()
   
    MyList =  content.split(" ")


  return MyList


def find_string(MyList,FindWord):

  EmptyList = []


  for Word in MyList:

    if Word != FindWord:

      StringMatch = set(Word) & set(FindWord)
      
      StringList = list(StringMatch)
      
      EmptyList.append(len(StringList))

    else:

      EmptyList.append(0)
      

  MaxNumber = max(EmptyList)

  IndexList = EmptyList.index(MaxNumber)

  MaxName = MyList[IndexList]

  return MaxName

def main():

  get_data1 = create_parser()

  FileName = get_data1.filename

  FindWord = get_data1.word

  get_data  = file_read(FileName)

  result = find_string(get_data,FindWord)

  print result


if __name__ == '__main__':

  main()
