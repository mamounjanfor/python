
from num2words import num2words


print("Insert the numbers, and i will write in letters:\n")

while True:
    insert = input("> ").lower()

    if(insert == 'h'):
        print('insert numbers to convert a letters or \ninsert [q] to quit')

    elif(insert == 'q'):
        print('closing program...')
        exit()

    elif(insert.isnumeric()):
        for val in insert:
            print('number/s inserted : {}'.format(num2words(val), end =" "))

    else:
        print('unknow input! digit [h] for help')



