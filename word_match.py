import argparse

def create_parser(): 

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help = "word help for searching in a file")

  args = parser.parse_args()

  return args


def read_file(FileName):  

  with open(FileName,'r') as file:

    Content = file.read()
   
    ContentList =  Content.split(" ")

  return ContentList


def find_match(GetContent,FindWord):

  CreateList = []

  for Word in GetContent:    

    if Word != FindWord:

      StringMatch = set(Word) & set(FindWord)
      
      StringList = list(StringMatch)
      
      CreateList.append(len(StringList))
      
    else:

      CreateList.append(0)
      
  MaxValue = max(CreateList)

  IndexValue = CreateList.index(MaxValue)

  MaxWord = GetContent[IndexValue]

  return MaxWord


def main():

  ArgsInput = create_parser()

  FileName = ArgsInput.filename

  FindWord = ArgsInput.word

  GetContent = read_file(FileName)

  result = find_match(GetContent,FindWord)

  print result


if __name__ == '__main__':

  main()
