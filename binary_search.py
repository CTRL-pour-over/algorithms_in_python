# Binary Search Algorithm #
# Goal: Within a given list; Return index position of arg_value. If not found, return -1. #
a = list(range(-928293,9992345)) 

def binary_search(arg_value, arg_ordered_list):  
	first_pos = 0 
	last_pos = len(a) - 1

	while first_pos <= last_pos: 
		mid = (first_pos + last_pos) // 2		
		if a[mid] == arg_value:
			return mid
		elif a[mid] > arg_value:
			last_pos = mid - 1
		else:
	  		first_pos = mid + 1
	return False

def _run(arg_value):
    print('Item in index location: ', binary_search(arg_value, a))

_run(555)
