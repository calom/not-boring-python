print('Enter a list')
initial_list = []
while True:
    print('Submit items to a list, submit 1 item and press enter to submit another, if not more items to submit, press enter with empty value')
    spam = input()
    if spam == '':
        break
    else:
        initial_list.append(spam)

list_as_string = ''
for (index, value) in enumerate(initial_list):
    if index == len(initial_list)-1:
        list_as_string += 'and ' + value   
    else:
        list_as_string += value + ', '

print(list_as_string)