def main():
    list = listing_nums()
    items_in_list(list)
    num = dividible_num(list)
    print('From the', str(len(list)), 'items, there is ' + str(num) + ' items which are dividible by 2 maximum 2 times')

def listing_nums():
    list = []
    for num in range(1, 8):
        list.append(num)
    print('Our list is ' + str(len(list)) + ' long.')
    print('It have the following items: ')
    return list


def items_in_list(list): # mivel a mainbe lett kitéve!
    for item in list:
        print(item)


def dividible_num(list):
    num = 0
    for i in list:
        if i // 2 <= 2:
            num += 1
    return num



if __name__== "__main__":
    main()