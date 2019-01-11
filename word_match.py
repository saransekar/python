import argparse

import heapq

from heapq import nlargest

def create_parser(): 

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help = "word help for searching in a file")

  parser.add_argument("number", metavar='number', nargs='?', default='')

  args = parser.parse_args()

  return args


def read_file(FileName):  

  with open(FileName,'r') as file:

    ContentWord = file.read()
   
    ContentList =  ContentWord.split(" ")



  return ContentList


def find_match(Content,FindWord,LimitNumber):
  
  AddList = []

  AddList1 = []

  for Word in Content:    

    if Word != FindWord:

      MatchWord = set(Word) & set(FindWord)
      
      WordList = list(MatchWord)
      
      AddList.append(len(WordList))

      
    else:

      AddList.append(0)

  words1 = { i : AddList[i] for i in range(0, len(AddList) ) }  

  

  z = words1.values()

  demo = max(z)

  for num, number in words1.items():

    if demo == number:

      WordName = Content[num]

      AddList1.append(WordName)
        
  return AddList1    



  """LargerNum = heapq.nlargest(len(AddList),words1.values())

  print LargerNum

  three_largest = nlargest(len(AddList), words1, key=words1.get)

  print three_largest

  for demo1 in three_largest:

    WordName = Content[demo1]

    print WordName


  return WordName"""



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
