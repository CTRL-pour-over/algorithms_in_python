
ordered_list = list(range(-999, 999))

def linear_search():
    value = 9999
    last = ordered_list.__len__() -1
    position = -999
    while position < last:
        print('\n', 'Position: ', position, '\n', 'Last Item: ', last, '\n', 'Value: ', value, '\n')
        if position == value:
            print('\n\nSUCCESS! Value found at\nIndex Position: ', ordered_list[position])
            return True
        else:
            position += 1
    print('item not found')

linear_search()
