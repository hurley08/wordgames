'''
Self contained class that accepts a dictionary and creates an object to store palingrams

Arguments:
list of words 

Exceptions:
NA

Returns:
a list containing all paligramic sequences detected

Requires:
load_dict
time
'''

import load_dict
import time, random


n = 0 #0 for entire dictionary or integer to select a random slice n length from source dictionary

class palinSeq:
   def __init__(self, diction):
      self.dictionary = diction
      self.length =  len(diction)
      self.palinSequences = {}
      self.processed = False
      
   def __call__(self,word=None):                      #returns palinsequences if dictionary has been processed and includes the word   
      if self.processed:                              #returns None if word exists in dictionary but has either not been processed or contains no palinsequences  
         if word in self.palinSequences.keys():       #return False if no word given or doesn't exist in source dictionaryy
            return self.palinSequences[word]
         if word in self.dictionary:
            return "%s contains no paligrams" % word
         else:
            return "{%s is not a member of the source dictionary or is None" % word
      elif self.processed == False:
         print("\tA dictionary has been loaded but has not be processed for palinsequences")
         if word in diction:
            return "%s exists in the source dictionary" % word
         if word not in diction or word == None:
            return "%s does not exist in the source dictionary"% word

   def __repr__(self):
      print('\n')
      self.info()
      return "\n"


   def begin(self):
      self.info()
      print("Processing dictionary for palinsequences")
      count = 0 
      diction = self.dictionary
      try:
         for i in diction:
            print("\t%s words read \r" %str(count), end = "")
               #Processing dictionary for palinsequences [%s]"%i)
            count += 1
            self.process(i)
         self.processed = True
         self.info()
         return True
      except Exception as err:
         print(f"Unexpected {err=}, {type(err)=}")
         raise

   def process(self,word):
      sequences = []
      forw = self.forward(word)
      reve = self.reverse(word)
      if len(forw+reve)>0:
         self.palinSequences.update({word:sorted(forw+reve)})
      else:
         return None 

   def show(self, word=None):
      palinRoots = list(self.palinSequences.keys())
      if word != None and word in palinRoots:
         print(self.palinSequences[word])
         return self.palinSequences[word]
      elif word != None:
         return self.__call__(word)
      else:
         #print(sorted(palinRoots))
         return self.palinSequences

   def info(self):
      if type(self.dictionary)== list:
         print(f"Dictionary of length {len(self.dictionary):} is loaded")
      if self.processed == True:
         print(f"Dictionary of {self.length:} found at least one palingram for {len(list(self.show().keys())):} word/s")
      else:
         print("Dictionary must be processed with the begin() method")

   def pal1(self, diction):
      pals2 = []
      for i in diction:
         h = i[1::][::-1]
         if h in diction:
            k = h,i
            print(k)
            pals2.append(k)
      return pals2


   def forward(self, word):
      pals3 = []
      j = word
      if j == j[::-1]:
         print(j+j[::-1])
         pals3.append(j+j[::-1])
      for i in range(len(j)):
         prefix = j[0:i][::-1]
         if prefix in diction and j[i:] == j[i:][::-1]: #tests symmetry and membership 
            print(j+prefix)
            pals3.append(j+prefix)
      return pals3

   def reverse(self, word):
      pals3 = []
      j = word
      for i in range(len(j)):
         prefix = j[0:-i:-1][::-1]
         if prefix in diction and j[:-i:-1] == prefix: #tests symmetry and membership 
            print(prefix+j)
            pals3.append(prefix+j) 
      return pals3


if __name__=='__main__':

   start = time.time()
   diction = load_dict.open_file('words2.txt')
   if n > 0:
      leftBound = random.choice(range(len(diction)))
      rightBound = leftBound + n if ((leftBound + n) < len(diction)) else len(diction) 
      diction = diction[leftBound:rightBound]
   
   print("--- %s seconds to load dictionary ---" % (time.time() - start))
   start = time.time()
   ps = palinSeq(diction)
   ps.begin()
   results = ps.show()
   print(results)
   print("--- %s seconds to process ---" % (time.time() - start))
  