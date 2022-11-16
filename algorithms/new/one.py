import math


def runningSum(nums):
  running_sum = [nums[0]]
  for idx in range(1, len(nums)):
    val = nums[idx]
    prev_sum = running_sum[idx-1]
    running_sum.append( prev_sum + val )           

  return running_sum


# print( runningSum([1,2,3,4]) )



# TODO: 
  # implement recursive, trivial solution first 
    # then, improve and get 'best' solution, before doing any other problem

def find_pivot_index_trivial(nums, pivot_idx):
  left_arr, right_arr = nums[0:pivot_idx], nums[pivot_idx:]
  sum_left, sum_right = sum(left_arr), sum(right_arr)

  if sum_left == sum_right:
    return pivot_idx
  else:
    return None

  # if (pivot_idx+1) < len(nums):
  #   return find_pivot_index_trivial(nums, pivot_idx+1)
  


nums = [1,7,3,6,5,6]
middle_idx = math.floor( len(nums) / 2 )

val = find_pivot_index_trivial(nums, middle_idx)
left_search = False
if val is None:
  new_val = (middle_idx - 1)
  while ( new_val >= 0 ):
    found_value = find_pivot_index_trivial(nums, middle_idx)
    if found_value != None:
      print("found pivot index:", found_value)
      left_search = True
      break
    
    new_val -= 1

right_search = False
if left_search is False and val is None:
  new_val = (middle_idx + 1)
  while ( new_val <= len(nums) ):
    found_value = find_pivot_index_trivial(nums, middle_idx)
    if found_value != None:
      print("found pivot index:", found_value)
      right_search = True
      break
    
    new_val += 1


if left_search is False and right_search is False:
  print('pivot index:', -1)



# # https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
# def find_pivot_index(nums, pivot_idx):
#   left_arr, right_arr = nums[0:pivot_idx], nums[pivot_idx:]
#   sum_left, sum_right = sum(left_arr), sum(right_arr)

#   if sum_left > sum_right:
#     if (pivot_idx+1) < len(nums):
#       if nums[pivot_idx+1] >= 0:
#         if (pivot_idx-1) > 0:
#           return find_pivot_index(nums, pivot_idx-1)
#         else:
#           return -1
#       elif nums[pivot_idx+1] < 0:
#         return find_pivot_index(nums, pivot_idx+1)
      

#     # if (pivot_idx + 1) == len(nums) - 1:
#     #   return -1
#     # else:
#     #   pass

#   # if sum_left == sum_right:
#   #   return pivot_idx
#   # else:
#   #   if sum_left > sum_right:
#   #     if (pivot_idx+1) < len(nums): # couldn't find
#   #       if nums[pivot_idx+1] < 0:



#   #     return find_pivot_index(nums, pivot_idx+1)
#   #   else:
#   #     return find_pivot_index(nums, pivot_idx-1)


# # middle_idx = len(nums) / 2


