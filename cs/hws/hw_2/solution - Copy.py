

# 1 
def string2int(s):
  nums_sing = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
          'eight': 8, 'nine': 9}
          
  nums_tens = {'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 
          'sixteen': 16, 'seventeen': 17, 'eightteen': 18, 'nineteen': 19}
           
  nums_places = {'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60,
          'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000}

  

  return x

"""Write a Python program that takes an English phrasing of a number as a string
s and outputs the corresponding integer
x. You can assume the number is positive and less than 1,000,000. Also s does not
contain any spaces
"""

# Finding all permutation
def permutation(s):
    if len(s) == 1:
        return[s]
    else:
        L = []
        for i in permutation(s[:-1]):
            for j in range(len(i)+1):
                arrangement = i[:j] + s[-1] + i[j:]
                L.append(arrangement)
    L.sort()
    return L

string = 'UCWA'
print(permutation(string))

"""Given a string
s
, write a Python program that returns all unique permutations of
s
as a list.
Example 1:
If
s=’UCR’
, then
L=[’UCR’, ’URC’, ’CUR’, ’CRU’, ’RCU’, ’RUC’,]
.
Example 2:
If
s=’UUC’
, then
L=[’UUC’, ’UCU’, ’CUU’]
.

"""

# 3
mylist = ["world", "LearnPython.com", "pineapple", "bicycle"]
def sort_string(L):
  Lsorted =  sorted(L)
  return Lsorted
  
print(sort_string(mylist))

"""Suppose L is a list of strings. Write a Python program to sort L alphabetically. You have to compare strings yourself, no built-in function is allowed.
Modify mergesort to allow strings to be inputted
"""

# 4
def longest_increasing_subseq(L):
  length = len(L)
  i = 0
  start = 0
  end = 0
  max = 1

  optstart = 0
  optend = 0

  while i  < length:
    if i + 1 < length and L[i+1] > L[i]:
      end = end +1
      if (end - start + 1) > max:
        max = (end - start + 1)
        optstart = start
        optend = end

    else:
        start =  i + 1
        end = i + 1

    i = i + 1

  Linc = (L[optstart:optend + 1])

  return Linc

"""Suppose
L
is a list of integers. Return the longest contiguous subsequence in
L
whose elements
are strictly increasing.
"""

# 5 
def rank_in_sortedlist(L,x):
  return rank

"""Suppose
L
is a sorted list in non-decreasing order. Your task is to program an algorithm that
given a value
x
, it computes the rank of
x
within
L
. Here, rank is defined as the number of list elements
strictly larger than
x

"""

# 6
def search_sorted_matrix(L,x):
  L = []
  ix_hold = 0
  for small_list in range(len(L))
    for ix_hold in range(len(small_list))
        
  return ix

"""Suppose
L
is a list of lists with length
n
. Each element of
L
is a sorted list of length
m
in increasing
order. Additionally, elements of
L
are also sorted increasingly. This means that
L[i1][i2]
≤
L[j1][j2]
for
j1
≥
i1
and
j2
≥
i2
. Write an algorithm to find the index (i.e. (x,y) coordinates) of a value
val
within
L
. If
val
does not exist, return
[-1,-1]
.
Example:
L=[ [1,3,5], [3,5,7] ]
and
x=5
. Since
5
appears in two coordinates, you can return either
ix=[0,2]
or
ix=[1,1]
. If
x=2
, you would return
[-1,-1]
.
"""

# 7
def closest_k_point(L, k):
  Lclose = []
  point = []
  for k in L:
    
    append 
  return Lclose

"""Let L be a list of points in plane. Each point is represented as a list with 2 elements: x and y coordinates of the point. Find the k points closest to the origin point (0,0). Here, we consider Euclidean distance so it is given by
dist(x,y),(0,0)) = sqrt(x^2+y^2)
"""

# 8
def h_index(L):
    L.sort()
    for i, j in enumerate(L):
        h = len(L) - i
        if h <= j:
            return h
    return 0

"""Suppose L is a list with unsorted integers. Given L as input, your goal is to identify the largest integer h
that satisfies the following condition: L contains at least h elements that are greater than or equal to h itself.
"""