import argparse
import sys

def create_parser():

  """function to create argument parser and return inputs""" 

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help = "name of the words for searching")

  parser.add_argument("limit", type = int, metavar='limit', nargs='?', help = "enter the number")

  args = parser.parse_args()

  return args

def read_file(FileName):

  """read a file in function and return content"""  
  
  Content = ''

  try:

    with open(FileName,'r') as file:
   
      Content = file.read()

  except IOError as e:

    sys.tracebacklimit = 0

    raise(IOError("\033[91m {}\033[00m" .format("File not found in directory.")))

  return Content


def separate_words(ContentWord):

  """split the words and return the list in function"""

  ContentList =  ContentWord.split(" ")

  return ContentList


def find_closest_match(ContentList,FindWord):

  """function to find closest match and return in dictionary"""
 
  WordLengthList = []   

  Words = [Word if Word != FindWord else "0" for Word in ContentList]  

  ClosestWord = list(map(lambda Words : set(Words) & set(FindWord), Words))  
    
  ClosestMatch = { i : len(ClosestWord[i]) for i in range(0, len(ClosestWord) ) }  

  print(ClosestMatch)
  
  return ClosestMatch   


def eliminate_words(ClosestMatch):

  """eliminate the words in dictionay"""

  ClosestMatch = {key: value for key, value in ClosestMatch.items() if value != 0}

  print(ClosestMatch) 

  return ClosestMatch


def restrictive_word(ClosestMatch,ContentList,LimitNumber):

  """limit the words in function and return results"""

  ClosestWords = []

  ClosestList = sorted(ClosestMatch.items(), key = lambda x : x[1], reverse = True)

  ClosestMaxValue = ClosestList[0][1]
  
  if LimitNumber is None:

    for ClosestKey,ClosestValue in ClosestList:

      if ClosestMaxValue == ClosestValue:

        WordContentList = ContentList[ClosestKey]

        ClosestWords.append(WordContentList)  

  else:

    for ClosestKey,ClosestValue in ClosestList[:LimitNumber]:
            
      WordContentList = ContentList[ClosestKey]

      ClosestWords.append(WordContentList) 
     
  return ClosestWords


def main():

  ArgsInput = create_parser()

  FileName = ArgsInput.filename

  FindWord = ArgsInput.word

  LimitNumber = ArgsInput.limit

  Content = read_file(FileName)


  if Content != '':

    ContentList = separate_words(Content)  

    ClosestMatch = find_closest_match(ContentList,FindWord)

    ClosestMatch = eliminate_words(ClosestMatch)

    result = restrictive_word(ClosestMatch,ContentList,LimitNumber)

    print(result)

  elif Content == '':
  
    print("The File is empty")
    

if __name__ == '__main__':

  main()