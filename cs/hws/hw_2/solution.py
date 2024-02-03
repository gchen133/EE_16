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

# 8
def h_index(L):
    L.sort()
    for i, j in enumerate(L):
        h = len(L) - i
        if h <= j:
            return h
    return 0
