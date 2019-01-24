import argparse

def create_parser(): 

  parser = argparse.ArgumentParser()

  parser.add_argument("filename")

  parser.add_argument("word", help = "word help for searching in a file")

  parser.add_argument("limit", type = int, metavar='limit', nargs='?')

  args = parser.parse_args()

  return args


def read_file(FileName):  

  ContentWord = ""

  try:

    with open(FileName,'r') as file:
   
      ContentWord = file.read()

  except IOError as e:

    #print FileName,"No Such directory file not found."

    print("\033[91m {}\033[00m" .format(FileName)),("\033[91m {}\033[00m" .format("No Such directory file not found.")) 

  return ContentWord


def seprate_word(ContentWord):

  ContentList =  ContentWord.split(" ")

  return ContentList


def find_closest_match(ContentList,FindWord):
  
  WordLengthList = []

  for Word in ContentList:    

    if Word != FindWord:

      ClosestWord = set(Word) & set(FindWord)
      
      WordList = list(ClosestWord)
      
      WordLengthList.append(len(WordList))
    
    else:

      WordLengthList.append(0)

  ClosestMatch = { i : WordLengthList[i] for i in range(0, len(WordLengthList) ) }  

  return ClosestMatch   


def remove_items(ClosestMatch):

  ClosestMatch = {key: value for key, value in ClosestMatch.items() if value != 0}

  return ClosestMatch


def restrictive_word(ClosestMatch,ContentList,LimitNumber):

  ClosestWords = []
  
  ClosestList = sorted(ClosestMatch.iteritems(), key = lambda x : x[1], reverse = True)

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

  #import pdb; pdb.set_trace()

  if Content is not '':

    ContentList = seprate_word(Content)  

    ClosestMatch = find_closest_match(ContentList,FindWord)

    ClosestMatch = remove_items(ClosestMatch)

    result = restrictive_word(ClosestMatch,ContentList,LimitNumber)

    print result

if __name__ == '__main__':

  main()