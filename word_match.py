import argparse

def create_parser(): 

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help = "word help for searching in a file")

  parser.add_argument("number", type = int)

  args = parser.parse_args()

  return args


def read_file(FileName):  

  with open(FileName,'r') as file:

    ContentWord = file.read()
   
    ContentList =  ContentWord.split(" ")

  return ContentList


def find_match(Content,FindWord,LimitNumber):

  AddList = []

  for Word in Content:    

    if Word != FindWord:

      MatchWord = set(Word) & set(FindWord)
      
      WordList = list(MatchWord)
      
      AddList.append(len(WordList))

      
    else:

      AddList.append(0)

  AddList.sort()

  print AddList 

  AddListCopy = AddList[-LimitNumber:]

  print AddListCopy

  for number in AddListCopy:

    print number


    IndexValue = AddListCopy.index(number)

    print IndexValue

    WordName = Content[IndexValue]

  return WordName


def main():

  ArgsInput = create_parser()

  FileName = ArgsInput.filename

  FindWord = ArgsInput.word

  LimitNumber = ArgsInput.number

  Content = read_file(FileName)

  result = find_match(Content,FindWord,LimitNumber)

  print result


if __name__ == '__main__':

  main()
