# Binary Search Algorithm #
# Goal: Within a given list; Return index position of arg_value. If not found, return -1. #

ordered_list = list(range(-543,2345))

def binary_search(arg_value, arg_ordered_list): 
	''' Return index position of arg_value within sorted list using binary search algorithm. If arg_value not found, return -1.\n
		arg_value = int being scanned for\n
		first_pos = first position in rang\n
		last_pos = last position in range\n
		mid_pos = mid position in range '''  
	
	first_pos = 0 # was the item at location zero: list[0]
   
	last_pos = arg_ordered_list.__len__() - 1
 
	while first_pos <= last_pos:    
		mid_point = (first_pos + last_pos) // 2 # added parentheses to equation. Oops
		
		print('\n', 'List: ', arg_ordered_list[first_pos : last_pos], '\n', 'Length of List: ', arg_ordered_list.__len__(), '\n', 'Looking for int: ', arg_value, '\n', 'First Position: ', first_pos, '\n', 'Last Position: ', last_pos, '\n', 'Mid Point: ', mid_point)
		
		if arg_ordered_list[mid_point] == arg_value:
			return mid_point # was arg_value

		elif arg_ordered_list[mid_point] > arg_value:
			last_pos = mid_point - 1

		else:
	  		first_pos = mid_point + 1
	print('Failed to locate int')
	return -1

def _run():
    print('Item in index location: ', binary_search(475, ordered_list))

_run()
