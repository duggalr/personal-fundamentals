import math


# implement python-split with 'whitespace' only
def split_implm(st):
  rv = []
  current_string = ''
  for idx in range(0, len(st)):
    s = st[idx]
    # print('current-string:', current_string)
    if s != ' ':  # whitespace-identification      
      current_string += s
    else: # encountered whitespace
      rv.append(current_string)
      current_string = ''

  if current_string != '':
    rv.append(current_string)

  return rv

# st = "alice and bob love leetcode  "
# rv = split_implm(st)
# print(rv)


# implement function that does factorial: 
  # with for-loop
  # with recursion
def factorial_with_loop(n):
  p = 1
  for idx in reversed(range(n+1)):
    if idx != 0:
      p = p * idx
  return p

def factorial_with_recursion(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial_with_recursion(n-1)

# n = 4
# factorial_value = factorial_with_loop(n)
# print(factorial_value)
# print(factorial_with_recursion(n))


# reverse prefix of word
def reverse_prefix(st, ch):
  idx = st.index(ch)
  return st[:idx+1][::-1] + st[idx+1:]


# st = 'abcdefd'
# ch = 'd'
# print(reverse_prefix(st, ch))


# reverse a string 
def reverse_string_trivial(st: str) -> str:
  if isinstance(st, str):
    new_st = ''
    for s in st:
      new_st = s + new_st
    return new_st
  else:
    # raise TypeError()
    return "Incorrect Type"

# st = 'abcd'
# st = ''
# st = 4
# print(reverse_string_trivial(st))


# reverse a string 
def reverse_string_fast(st):
  if len(st) <= 1:
    return st

  start_idx = 0
  new_st = ''
  for idx in range(2, len(st)+2, 2): # O(log(n))
    subst = st[start_idx:idx]
    if len(subst) == 1:
      reversed_subst = subst
    else:
      reversed_subst = subst[1] + subst[0] # O(1)
    new_st = reversed_subst + new_st
    start_idx += 2
  
  return new_st


# reverse string inplace
def reverse_string_inplace(st):
  if len(st) == 1:
    return st
  else:
    return st[-1] + reverse_string_inplace(st[:-1])



# reverse string fast with recursion
def reverse_string_fast_recursion(st):
  if len(st) == 1:
    return st
  elif len(st) == 2:
    return st[1] + st[0]
  else:
    idx = math.ceil(len(st) / 2)
    return reverse_string_fast_recursion(st[idx:]) + reverse_string_fast_recursion(st[:idx])


# st = 'ab'
# print(reverse_string_fast(st))
# print(reverse_string_inplace(st))
# print(reverse_string_fast_recursion(st))


# # # binary search; assumes sorted-list
# def binary_search(li, elem):  
#   if len(li) == 1:
#     if li[0] == elem:
#       return 0
#     else:
#       return -1

#   idx = math.floor(len(li) / 2)
#   middle_elem = li[idx]
#   if middle_elem == elem:
#     return idx
#   else:
#     if elem < middle_elem:
#       return binary_search(li[:idx], elem)
#     elif elem > middle_elem:
#       return idx + binary_search(li[idx:], elem)


def binary_search(li, main_idx, elem):
  if main_idx >= len(li):
    return -1
  middle_elem = li[main_idx]
  if middle_elem == elem:
    return main_idx
  else:
    if elem < middle_elem:
      return binary_search(li, main_idx-1, elem)
    elif elem > middle_elem:
      return binary_search(li, main_idx+1, elem)


# li = [1,2,3,4,5]
# elm = 6
# idx = math.floor(len(li) / 2)
# print(binary_search(li, idx, elm))










