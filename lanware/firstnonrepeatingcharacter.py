# def firstNonRepeatingChar(str1):
#    char_order = []
#    counts = {}
#    for c in str1:
#       if c in counts:
#          counts[c] += 1
#       else:
#          counts[c] = 1
#          char_order.append(c)
#    for c in char_order:
#       if counts[c] == 1:
#         return c
#    return None
#
# print(firstNonRepeatingChar('sreelakshmi'))

from collections import Counter
def nonrepeatchar(string):
   a=Counter(string)
   for i in string:
      if(a[i]==1):
         print(i)
         break
string="geeksforgeeks"
nonrepeatchar(string)
