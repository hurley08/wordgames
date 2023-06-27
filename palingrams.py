'''
Derives paligramic sequences from every word contained in a dictionary input

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
import time,random 



def pal1(diction):
   pals2 = []
   for i in diction:
      h = i[1::][::-1]
      if h in diction:
         k = h,i
         print(k)
         pals2.append(k)
   return pals2


def forward(word):
   pals3 = []
   j = word
   for i in range(len(j)):
      prefix = j[0:i][::-1]
      if prefix in diction and j[i:] == j[i:][::-1]: #tests symmetry and membership 
         pals3.append(j+prefix)
   return pals3

def reverse(word):
   pals3 = []
   j = word
   for i in range(len(j)):
      prefix = j[0:-i:-1][::-1]
      if prefix in diction and j[:-i:-1] == prefix: #tests symmetry and membership 
         pals3.append(prefix+j) 
   return pals3


if __name__=='__main__':

   start = time.time()
   diction = load_dict.open_file('words2.txt')
   leftBound = random.choice(range(len(diction)))
   rightBound = leftBound + 10000 if ((leftBound + 10000) < len(diction)) else len(diction) 
   diction = diction[leftBound:rightBound]
   print("--- %s seconds to load dictionary ---" % (time.time() - start))
   start = time.time()
   palMain = {}
   for i in diction:
      forw = forward(i)
      reve = reverse(i)
      if len(forw+reve) > 0:
         palMain.update({i:sorted(forw+reve)})
         print(i,palMain[i])
   
   print("--- %s seconds to process ---" % (time.time() - start))
   print("--- dictionary size %i with %i matches --- " % (len(diction), len(palMain.keys())))