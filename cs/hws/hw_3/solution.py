import math

# Question 1
def string2int(s):
    # ones
    num2words = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,'zero':0,
                 'ten':10,'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,
                 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty': 30, 'fourty':40, 'fifty':50, 
                 'sixty':60, 'seventy':70, 'eighty':80,'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000,}
    
    x = 0
    if (s == "zero"):
        x == num2words.get("zero")
    if(s.find("onemillion" or "million") != -1):
        x += num2words.get("million")
    if(s.find("onehundred" or "hundred") != -1):
        x += num2words.get("hundred")
    elif(s.find("one") != -1):
        x += num2words.get("one")
    if(s.find("two") != -1):
        x += num2words.get("two")
    if(s.find("seven") != -1):
        x += num2words.get("seven")
    if(s.find("twenty") != -1):
        x += num2words.get("twenty")
    print(x)
    return x

# Question 2
def permutation(s):
    newlist = []
    if (len(s) == 1): # if the string length is 1, return the string
        return s
    for i, perm in enumerate(s):
        newS = s[:i] + s[i+1:]
        l2 = permutation(newS)

        for perm in l2:
            newlist.append(s[i]+perm)

    l = list(set(newlist))
    return l


# Question 3
def sort_string(L):
    sorted_List = []
    if len(L) == 0:
        return L
    elif len(L) == 1:
        sorted_List.append(L[0])
        return sorted_List
    
    half = int(len(L)/2)

    L[:half] = sort_string(L[:half])
    L[half:] = sort_string(L[half:])

    i = 0
    a = 0
    b = 0

    #merge sort
    copy = L.copy()
    for i in range(len(L)):
        if a < half and (b == len(L) - half or (copy[a] <= copy [b + half])):
            sorted_List.append(copy[a])
            i = i + 1
            a = a + 1
        else:
            sorted_List.append(copy[b + half])
            i += 1
            b += 1
    return sorted_List

# Question 4
def longest_increasing_subseq(L):
    length = len(L)
    i = 0
    max = 1
    start = 0
    end = 0

    optstart = 0  # init optstart
    optend = 0  #init optend

    while i < length:
        if i + 1 < length and L[i+1] > L[i]:
            end = end + 1  #increment end because there's a longer array
            if (end - start + 1) > max:
                max = (end - start + 1)  #update max
                optstart = start  #update optstart because longest array until this point
                optend = end  #update optend because longest array until this point
        else:
            start = i+1  #re-initialize start
            end = i+1  #re-initialize end
        i = i + 1
    Linc = (L[optstart:optend+1])  #longest array
    return Linc


# Question 5
def rank_in_sorted_list(L, x):
    rank = 0
    min = 0             # min = start of list
    maximum = len(L) - 1    # maximum = end of list

    while min <= maximum:                   
        mid = int((min + maximum) / 2)      
        if(L[mid] > x):          
            rank = mid            
            maximum = mid - 1  
        else:
            min = mid + 1      
    if rank == 0:                
        return rank
    else:                        
        rank = len(L) - rank
        return rank

# Question 6
def search_sorted_matrix(L,x):
    ix = []

    #nested for loops to find indices
    for i, j in enumerate(L):       # i = index of the list; j = values of the index    (j == L[i])
        if x in j:                  #if x is in j, append to empty list
            ix.append(i)
            for j, h in enumerate(j): #at index i
                if x == h:
                    ix.append(j)
                    return ix

    return [-1,-1]

# Question 7
def closest_k_points(L,k):

    # Quick Select
    n = len(L)        
    min = 0      
    max = n - 1  

    while (min <= max):                     # while min is less than or equal to max
        mid = sections(L, min, max)         # use sections function until k is equal to the middle of the list
        if mid == k:        # if mid is equal to k, then break loop
            break
        if (mid < k):           # if mid is less than k, then increase min, run section function again 
            min = mid + 1   # until mid is equal to k
        else :
            max = mid - 1   # if mid is greater than k, then decrease max, run section function again
                                # until mid is equal to k
    Lclose = L[:k]
    return Lclose

def sections(L, min, max):
    pivot = L[min]
    while (min < max):
        while min < max and compare(L[max], pivot) >= 0:
            max -= 1
        L[min] = L[max]
        while min < max and compare(L[min], pivot) <= 0: 
            min += 1
        L[max] = L[min]
    L[min] = pivot
    return min

def compare(a,b):
    return (a[0]*a[0] + a[1]*a[1] - (b[0]*b[0] + b[1]*b[1]))



# Question 8
def h_index(L):

    L.sort()

    for i, j in enumerate(L):

        h = len(L) - i
        #if num(h) <= j
        #returns number of h occurences
        if h <= j:
            return h

    return 0