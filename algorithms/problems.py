

def sort_one(li): 
  for i in range(len(li)-1):
    current_val = li[i]
    next_val = li[i+1]
    if current_val <= next_val:
      pass
    else:
      li[i] = next_val
      li[i+1] = current_val
      return sort_one(li)
  
# li = [4,5,2,7,10,1,0,-10]
# sort_one(li)
# print(li)


def rev(l):  # not in place
  if len(l) == 0:
    return []
  else:
    return [l[-1]] + rev(l[:-1])

# li = ['h', 'e', 'l', 'l', 'o']
# print(rev(li))

def reverse_string(s, offset=0):  # this is inplace
  if len(s) > offset * 2:
    s[offset], s[-offset - 1] = s[-offset - 1], s[offset]
    reverse_string(s, offset + 1)


# Function for the fib-sequence
def fib_sequence(n):
  if n == 0:
    return 0 
  elif n == 1:
    return 1
  else: 
    return fib_sequence(n-1) + fib_sequence(n-2)
    
# print(fib_sequence(6))



#TODO: Merge 2 lists 



