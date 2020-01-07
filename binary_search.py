# Binary Search Algorithm #
# Goal: Within a given list; Return index position of arg_value. If not found, return -1. #

ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 53]

def binary_search(arg_value, arg_ordered_list): 
	''' Return index position of arg_value within sorted list using binary search algorithm. If arg_value not found, return -1.
		arg_value = int to be found within the list
		first_pos = first position in range
		last_pos = last position in range
		mid_pos = mid position in range '''  
	
	first_pos = 0 
  
	last_pos = arg_ordered_list.__len__() - 1 

	while first_pos <= last_pos:    
		mid_point = first_pos + last_pos // 2 # Find the mid point.
		
		print('\n', 'List: ', arg_ordered_list, '\n', 'Length of List: ', arg_ordered_list.__len__(), '\n', 'Looking for int: ', arg_value, '\n', 'First Position: ', first_pos, '\n', 'Last Position: ', last_pos, '\n', 'Mid Point: ', mid_point)
		
		if arg_ordered_list[mid_point] == arg_value:
			return arg_value

		elif arg_ordered_list[mid_point] > arg_value:
			last_pos = mid_point - 1

		else:
	  		first_pos = mid_point + 1
	print('Failed to locate int')
	return -1

binary_search(11, ordered_list)
